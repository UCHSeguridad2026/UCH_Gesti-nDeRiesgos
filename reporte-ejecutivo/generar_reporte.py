# -*- coding: utf-8 -*-
"""Genera el Reporte Ejecutivo (máx. 3 páginas) para la dirección de la clínica."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TituloPortada", fontSize=20, leading=24,
                           alignment=TA_CENTER, spaceAfter=6, textColor=colors.HexColor("#1a3a5c")))
styles.add(ParagraphStyle(name="Subtitulo", fontSize=12, leading=16,
                           alignment=TA_CENTER, textColor=colors.HexColor("#555555")))
styles.add(ParagraphStyle(name="H2", fontSize=13, leading=16, spaceBefore=10, spaceAfter=6,
                           textColor=colors.HexColor("#1a3a5c"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="Cuerpo", fontSize=9.5, leading=13, alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name="CuerpoChico", fontSize=8.5, leading=11, alignment=TA_JUSTIFY))

doc = SimpleDocTemplate(
    "reporte.pdf", pagesize=A4,
    topMargin=1.6*cm, bottomMargin=1.6*cm, leftMargin=1.8*cm, rightMargin=1.8*cm,
    title="Reporte Ejecutivo de Gestión de Riesgos - Centro Médico del Valle",
)

story = []

# ---------- PÁGINA 1 ----------
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("Reporte Ejecutivo de Gestión de Riesgos", styles["TituloPortada"]))
story.append(Paragraph("Centro Médico del Valle · Clínica Privada", styles["Subtitulo"]))
story.append(Paragraph("Preparado con SimpleRisk · Septiembre 2026", styles["Subtitulo"]))
story.append(Spacer(1, 0.6*cm))

story.append(Paragraph("Resumen ejecutivo", styles["H2"]))
story.append(Paragraph(
    "A raíz de una auditoría externa reciente que identificó debilidades en la gestión de riesgos, "
    "se llevó a cabo un relevamiento integral utilizando la herramienta SimpleRisk. Se identificaron "
    "<b>9 riesgos</b> específicos para la operación de la clínica (120 empleados, ~800 pacientes/día), "
    "abarcando amenazas técnicas (ransomware, exfiltración de datos), factores humanos (phishing) y "
    "debilidades organizativas (backups, gestión de accesos, cumplimiento normativo). Se definieron "
    "<b>3 planes de acción prioritarios</b> para mitigar los riesgos de mayor severidad, con responsables, "
    "plazos y presupuesto estimado asignados.",
    styles["Cuerpo"]))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("Distribución de riesgos por nivel", styles["H2"]))
dist_data = [
    ["Nivel", "Cantidad", "Riesgos"],
    ["Alto (High)", "1", "R01 · Ransomware sobre historias clínicas"],
    ["Medio (Medium)", "6", "R02, R03, R04, R05, R06, R07"],
    ["Bajo (Low)", "2", "R08, R09"],
]
t = Table(dist_data, colWidths=[3.2*cm, 2.4*cm, 9.4*cm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a3a5c")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8.5),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.white]),
]))
story.append(t)
story.append(Spacer(1, 0.35*cm))

story.append(Paragraph(
    "<i>Nota metodológica:</i> el análisis documentado por el equipo (ver informe técnico, Anexo) clasifica "
    "los riesgos en una escala 1-25 (Crítico/Alto/Medio/Bajo) basada en probabilidad e impacto justificados "
    "con evidencia del sector (Verizon DBIR). SimpleRisk aplica su propio método de puntuación ponderado "
    "(\"Classic\"), cuyos resultados (arriba) son consistentes en la priorización: el riesgo de ransomware "
    "es, en ambos esquemas, el de mayor severidad.",
    styles["CuerpoChico"]))

story.append(PageBreak())

# ---------- PÁGINA 2 ----------
story.append(Paragraph("Top 5 riesgos por nivel de severidad", styles["H2"]))
top5_data = [
    ["ID", "Riesgo", "Riesgo Inherente", "Nivel"],
    ["R01", "Ransomware sobre servidores de historias clínicas", "8.0", "High"],
    ["R03", "Phishing dirigido al personal administrativo", "6.4", "Medium"],
    ["R02", "Exfiltración de datos de pacientes (PHI)", "6.0", "Medium"],
    ["R04", "Ausencia de backups probados y plan de recuperación", "6.0", "Medium"],
    ["R05", "Accesos con privilegios excesivos y cuentas compartidas", "4.8", "Medium"],
]
t2 = Table(top5_data, colWidths=[1.4*cm, 9.6*cm, 2.4*cm, 1.6*cm])
t2.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a3a5c")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.white]),
    ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#f8d7da")),
]))
story.append(t2)
story.append(Spacer(1, 0.4*cm))

story.append(Paragraph("Estado de los planes de acción", styles["H2"]))
planes_data = [
    ["Plan", "Riesgo asociado", "Responsable", "Vencimiento", "Avance"],
    ["PA-01", "R01 - Ransomware", "Gerencia de TI", "90 días", "0%"],
    ["PA-02", "R02 - Exfiltración de datos", "Resp. de Seguridad", "120 días", "0%"],
    ["PA-03", "R03 - Phishing / MFA", "Resp. de Seguridad", "60 días", "25% (en curso)"],
]
t3 = Table(planes_data, colWidths=[1.6*cm, 4.6*cm, 3.4*cm, 2.6*cm, 2.8*cm])
t3.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a3a5c")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.white]),
]))
story.append(t3)
story.append(Spacer(1, 0.4*cm))

story.append(Paragraph("Principales hallazgos", styles["H2"]))
story.append(Paragraph(
    "• El mayor riesgo es el <b>ransomware sobre los servidores de historias clínicas</b>, agravado por la "
    "ausencia de backups probados (R04): hoy un incidente de este tipo dejaría a la clínica sin capacidad "
    "de atención y sin forma de recuperar la información.<br/>"
    "• El <b>phishing</b> (R03) es el vector de entrada más probable hacia los riesgos de mayor impacto, "
    "favorecido por la falta de capacitación formal y de autenticación multifactor.<br/>"
    "• Existen <b>debilidades organizativas</b> (privilegios excesivos, cuentas compartidas, ausencia de "
    "política formal de datos personales) que, si bien no son las de mayor puntaje individual, aumentan la "
    "probabilidad e impacto de los demás riesgos.",
    styles["Cuerpo"]))

story.append(PageBreak())

# ---------- PÁGINA 3 ----------
story.append(Paragraph("Recomendaciones prioritarias para la Dirección", styles["H2"]))
recs = [
    ("1. Aprobar y financiar el Plan PA-01 (defensa contra ransomware)",
     "Es la inversión de mayor impacto: reduce el riesgo más severo identificado. Presupuesto estimado: USD 12.000."),
    ("2. Implementar backups probados con restauración periódica (R04)",
     "Complemento indispensable de PA-01: sin backups verificados, cualquier incidente grave implica pérdida "
     "irreversible de historias clínicas."),
    ("3. Priorizar el despliegue de MFA y la capacitación anti-phishing (PA-03)",
     "Es la medida de menor costo relativo (USD 4.000) con mayor efecto en reducir la probabilidad de "
     "incidentes, dado que el factor humano es la puerta de entrada más común."),
    ("4. Revisar la política de accesos (R05) y las interfaces con obras sociales (R06)",
     "Acciones de bajo costo (ajustes de configuración y procesos) que reducen significativamente la "
     "superficie de exposición."),
    ("5. Iniciar un programa formal de cumplimiento de la Ley 25.326 (R07)",
     "Designar un responsable de protección de datos y documentar las medidas de seguridad exigidas para "
     "datos de salud, dado que la clínica maneja datos sensibles a diario."),
]
for titulo, detalle in recs:
    story.append(Paragraph(f"<b>{titulo}</b>", styles["Cuerpo"]))
    story.append(Paragraph(detalle, styles["CuerpoChico"]))
    story.append(Spacer(1, 0.15*cm))

story.append(Spacer(1, 0.3*cm))
story.append(Paragraph("Próximos pasos", styles["H2"]))
story.append(Paragraph(
    "Se solicita a la Dirección la aprobación del presupuesto conjunto de los 3 planes de acción "
    "(USD 24.000 estimados) y la designación formal de los responsables mencionados. El seguimiento del "
    "avance se realizará mensualmente en SimpleRisk, con reportes de estado a esta Dirección cada 30 días.",
    styles["Cuerpo"]))
story.append(Spacer(1, 0.6*cm))
story.append(Paragraph(
    "<i>Documento preparado a partir del registro de riesgos cargado en SimpleRisk como parte del Trabajo "
    "Práctico de la cátedra Seguridad de Sistemas. Ver informe técnico completo (informe/informe.md) para "
    "el detalle metodológico y la justificación de cada riesgo.</i>",
    styles["CuerpoChico"]))

doc.build(story)
print("PDF generado: reporte.pdf")
