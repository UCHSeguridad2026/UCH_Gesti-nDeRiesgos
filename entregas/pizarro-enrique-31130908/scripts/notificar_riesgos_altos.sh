#!/usr/bin/env bash
#
# notificar_riesgos_altos.sh
#
# Consulta la base de datos de SimpleRisk y envia una notificacion a Discord
# con los riesgos cuyo score supera el umbral definido.
#
# Uso:  ./notificar_riesgos_altos.sh
# Requiere: un archivo .env en el mismo directorio (ver .env.example)

set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# --- Carga de configuracion -------------------------------------------------
# Las credenciales se leen desde .env y nunca se escriben en este script.
if [[ ! -f "$DIR/.env" ]]; then
    echo "ERROR: no se encontro el archivo .env" >&2
    echo "Copie .env.example a .env y complete los valores." >&2
    exit 1
fi

set -a
# shellcheck disable=SC1091
source "$DIR/.env"
set +a

: "${DISCORD_WEBHOOK_URL:?Falta definir DISCORD_WEBHOOK_URL en .env}"
: "${DB_PASSWORD:?Falta definir DB_PASSWORD en .env}"

CONTENEDOR="${CONTENEDOR:-simplerisk}"
DB_USER="${DB_USER:-simplerisk}"
DB_NAME="${DB_NAME:-simplerisk}"
UMBRAL="${UMBRAL:-6}"

# --- Consulta a la base -----------------------------------------------------
# Se unen las tablas risks y risk_scoring por id.
# calculated_risk contiene el score que SimpleRisk asigna al riesgo.
# Se excluyen los riesgos cerrados (close_id no nulo).
CONSULTA="SELECT r.id, r.subject, s.calculated_risk, s.CLASSIC_likelihood, s.CLASSIC_impact
          FROM risks r
          JOIN risk_scoring s ON r.id = s.id
          WHERE s.calculated_risk >= ${UMBRAL}
            AND r.close_id IS NULL
          ORDER BY s.calculated_risk DESC;"

RESULTADO=$(docker exec "$CONTENEDOR" \
    mysql -h 127.0.0.1 -u "$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" \
    -B -N -e "$CONSULTA" 2>/dev/null)

if [[ -z "$RESULTADO" ]]; then
    echo "No se encontraron riesgos con score mayor o igual a ${UMBRAL}."
    exit 0
fi

CANTIDAD=$(echo "$RESULTADO" | wc -l)

# --- Armado del mensaje -----------------------------------------------------
LINEAS=""
while IFS=$'\t' read -r id subject score likelihood impact; do
    LINEAS+="**[${id}] ${subject}**\\nScore: ${score}  ·  Probabilidad: ${likelihood}  ·  Impacto: ${impact}\\n\\n"
done <<< "$RESULTADO"

DESCRIPCION="Se detectaron **${CANTIDAD}** riesgos con score igual o superior a ${UMBRAL}.\\n\\n${LINEAS}"

PAYLOAD=$(cat <<JSON
{
  "username": "SimpleRisk",
  "embeds": [{
    "title": "Alerta de riesgos de nivel alto",
    "description": "${DESCRIPCION}",
    "color": 15158332,
    "footer": { "text": "Registro de riesgos - Clinica privada" }
  }]
}
JSON
)

# --- Envio ------------------------------------------------------------------
CODIGO=$(curl -s -o /dev/null -w "%{http_code}" \
    -H "Content-Type: application/json" \
    -X POST \
    -d "$PAYLOAD" \
    "$DISCORD_WEBHOOK_URL")

if [[ "$CODIGO" == "204" ]]; then
    echo "Notificacion enviada correctamente (${CANTIDAD} riesgos)."
else
    echo "ERROR: Discord respondio con codigo HTTP ${CODIGO}" >&2
    exit 1
fi
