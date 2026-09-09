# -*- coding: utf-8 -*-
"""Genera la Matriz de Riesgos completada (Actividad A03) reutilizando el escenario
de la clínica 'Centro Médico del Valle' ya cargado en SimpleRisk."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Titulo", fontSize=16, leading=20, alignment=TA_CENTER,
                           textColor=colors.HexColor("#1a3a5c"), spaceAfter=4))
styles.add(ParagraphStyle(name="Subt", fontSize=10.5, leading=14, alignment=TA_CENTER,
                           textColor=colors.HexColor("#555555")))
styles.add(ParagraphStyle(name="H1", fontSize=13, leading=16, spaceBefore=14, spaceAfter=6,
                           textColor=colors.HexColor("#1a3a5c"), fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="H2", fontSize=10.5, leading=13, spaceBefore=8, spaceAfter=4,
                           fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(name="Cuerpo", fontSize=9.5, leading=13, alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name="Chico", fontSize=8, leading=10.5))

NIVEL_COLOR = {
    "Bajo": colors.HexColor("#c6efce"),
    "Medio": colors.HexColor("#ffeb9c"),
    "Alto": colors.HexColor("#ffd28a"),
    "Crítico": colors.HexColor("#ffc7ce"),
}

def tabla_estandar(data, col_widths, header_bg="#1a3a5c", font_size=7.5):
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(header_bg)),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), font_size),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.white]),
    ]))
    return t

doc = SimpleDocTemplate(
    "matriz_riesgos_A03.pdf", pagesize=A4,
    topMargin=1.4*cm, bottomMargin=1.4*cm, leftMargin=1.6*cm, rightMargin=1.6*cm,
    title="Matriz de Riesgos - Actividad A03 - Centro Médico del Valle",
)
story = []

# ---------- PORTADA / DATOS GENERALES ----------
story.append(Paragraph("Matriz de Riesgos — Actividad A03", styles["Titulo"]))
story.append(Paragraph("Administración de Riesgos · Seguridad Aplicada a Sistemas de Información", styles["Subt"]))
story.append(Spacer(1, 0.5*cm))

story.append(Paragraph("1. Datos Generales", styles["H1"]))
datos = [
    ["Nombre de la empresa / organización", "Centro Médico del Valle (clínica privada, nombre ficticio)"],
    ["Rubro / Industria", "Salud — atención médica privada"],
    ["Tamaño (empleados / facturación)", "120 empleados · ~800 pacientes/día"],
    ["Alumno(s) / Grupo", "Juan Narváez (Juanchi) — Comisión 4°G"],
    ["Legajo(s)", "31631196"],
    ["Fecha de elaboración", "Septiembre 2026"],
    ["Responsable del análisis", "Juan Narváez"],
]
story.append(tabla_estandar(datos, [6.5*cm, 10.5*cm], font_size=8.5))
story.append(Spacer(1, 0.4*cm))

story.append(Paragraph("2. Objetivo y Alcance del Análisis", styles["H1"]))
story.append(Paragraph(
    "<b>Objetivo:</b> identificar, valorar y tratar los riesgos de seguridad de la información más "
    "relevantes para la operación de la clínica, a raíz de una auditoría externa que detectó debilidades "
    "en su gestión de riesgos, con el fin de priorizar inversiones de seguridad y reducir la exposición "
    "sobre los datos de pacientes y la continuidad de la atención.",
    styles["Cuerpo"]))
story.append(Spacer(1, 0.15*cm))
story.append(Paragraph(
    "<b>Alcance:</b> sistemas de historias clínicas digitales, base de datos de pacientes, módulo de "
    "facturación e interfaz con obras sociales, correo corporativo y estaciones de trabajo administrativas, "
    "infraestructura de servidores y dispositivos móviles del personal. No incluye equipamiento médico "
    "biomédico ni sistemas de terceros fuera del control directo de la clínica.",
    styles["Cuerpo"]))

story.append(PageBreak())

# ---------- 3. INVENTARIO DE ACTIVOS ----------
story.append(Paragraph("3. Inventario y Clasificación de Activos", styles["H1"]))
activos = [
    ["ID", "Descripción del Activo", "Tipo", "Responsable", "Clasif.", "Criticidad"],
    ["A01", "Servidor de historias clínicas (HCE)", "Información", "Gerencia de TI", "Restringida", "Alta"],
    ["A02", "Base de datos de pacientes (MySQL)", "Información", "Gerencia de TI", "Restringida", "Alta"],
    ["A03", "Almacenamiento de estudios por imágenes", "Información", "Gerencia de TI", "Restringida", "Alta"],
    ["A04", "Credenciales de usuarios y accesos", "Información", "Adm. de Sistemas", "Confidencial", "Alta"],
    ["A05", "Estaciones de trabajo administrativas", "Hardware", "Adm. de Sistemas", "Interna", "Media"],
    ["A06", "Correo corporativo", "Software", "Adm. de Sistemas", "Interna", "Media"],
    ["A07", "Módulo de facturación / interfaz obras sociales", "Software", "Jefe de Facturación", "Confidencial", "Alta"],
    ["A08", "Dispositivos móviles del personal (notebooks/tablets)", "Hardware", "Adm. de Sistemas", "Confidencial", "Media"],
    ["A09", "Infraestructura de servidores (sala, energía)", "Hardware/Red", "Gerencia de TI", "Interna", "Alta"],
    ["A10", "Personal médico y administrativo", "Humano", "Dirección Médica", "Interna", "Media"],
]
story.append(tabla_estandar(activos, [1.2*cm, 6.6*cm, 2.2*cm, 2.9*cm, 2.2*cm, 1.9*cm]))
story.append(Spacer(1, 0.3*cm))

# ---------- 4. AMENAZAS ----------
story.append(Paragraph("4. Identificación de Amenazas y Vulnerabilidades", styles["H1"]))
amenazas = [
    ["ID", "Activo", "Descripción de la Amenaza", "Tipo", "Vulnerabilidad Asociada"],
    ["T01", "A01,A03", "Ataque de ransomware que cifra los servidores de HCE", "Intencional", "Falta de EDR y segmentación de red"],
    ["T02", "A02,A04", "Exfiltración de datos de pacientes por acceso no autorizado", "Intencional", "Sin cifrado en reposo ni DLP"],
    ["T03", "A05,A06", "Phishing dirigido al personal administrativo", "Intencional", "Falta de capacitación formal y de MFA"],
    ["T04", "A01,A02", "Pérdida irreversible de datos ante incidente mayor", "Accidental", "Backups sin prueba de restauración"],
    ["T05", "A04", "Uso indebido de privilegios excesivos / cuentas compartidas", "Intencional", "Falta de RBAC y revisión de accesos"],
    ["T06", "A07", "Exposición de datos en la interfaz con obras sociales", "Accidental", "Falta de cifrado TLS extremo a extremo"],
    ["T07", "A02,A10", "Incumplimiento de la Ley 25.326 de Datos Personales", "Accidental", "Sin política formal de datos ni DPO"],
    ["T08", "A08", "Robo o pérdida de dispositivos móviles sin cifrado", "Intencional", "Sin cifrado de disco ni MDM"],
    ["T09", "A09", "Falla de infraestructura por falta de redundancia", "Natural/Accidental", "UPS insuficiente, sin generador"],
]
story.append(tabla_estandar(amenazas, [1.2*cm, 1.9*cm, 6.3*cm, 2.6*cm, 4.9*cm], font_size=7))

story.append(PageBreak())

# ---------- 5. ESCALAS ----------
story.append(Paragraph("5. Escalas de Valoración", styles["H1"]))
story.append(Paragraph("5.1. Escala de Probabilidad", styles["H2"]))
prob = [
    ["Valor", "Nivel", "Descripción"],
    ["1", "Raro", "El evento solo ocurriría en circunstancias excepcionales."],
    ["2", "Improbable", "Podría ocurrir, pero no se espera que suceda."],
    ["3", "Posible", "Existe una posibilidad real de que ocurra."],
    ["4", "Probable", "Es muy probable que ocurra en algún momento."],
    ["5", "Casi seguro", "Se espera que ocurra frecuentemente / ha ocurrido recientemente."],
]
story.append(tabla_estandar(prob, [1.5*cm, 3*cm, 11.5*cm], font_size=8.5))
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("5.2. Escala de Impacto", styles["H2"]))
imp = [
    ["Valor", "Nivel", "Descripción"],
    ["1", "Insignificante", "Impacto mínimo, sin consecuencias operativas ni económicas relevantes."],
    ["2", "Menor", "Alteración leve de la operación, costo bajo."],
    ["3", "Moderado", "Impacto operativo y económico apreciable, recuperable."],
    ["4", "Mayor", "Impacto significativo, pérdida de operación o datos, costo alto."],
    ["5", "Catastrófico", "Paralización total, pérdida crítica de datos, daño reputacional o legal severo."],
]
story.append(tabla_estandar(imp, [1.5*cm, 3*cm, 11.5*cm], font_size=8.5))
story.append(Spacer(1, 0.4*cm))

# ---------- 6. MATRIZ DE CALOR ----------
story.append(Paragraph("6. Matriz de Calor (Probabilidad × Impacto)", styles["H1"]))
story.append(Paragraph(
    "Se ubican los 9 riesgos identificados (R01–R09) según su probabilidad (eje vertical) e impacto "
    "(eje horizontal). El color de cada celda indica el nivel de riesgo resultante.",
    styles["Cuerpo"]))
story.append(Spacer(1, 0.2*cm))

# posiciones: prob(1-5) x impacto(1-5) -> lista de IDs en esa celda
ubic = {
    (4,5): "R01", (4,4): "R03", (3,5): "R02,R04", (4,3): "R05",
    (3,4): "R06,R07", (3,3): "R08,R09",
}
def color_de_valor(v):
    if v <= 4: return NIVEL_COLOR["Bajo"]
    if v <= 9: return NIVEL_COLOR["Medio"]
    if v <= 15: return NIVEL_COLOR["Alto"]
    return NIVEL_COLOR["Crítico"]

header = ["P \\ I"] + [str(i) for i in range(1,6)]
matriz_data = [header]
for p in range(5, 0, -1):
    fila = [str(p)]
    for i in range(1, 6):
        v = p*i
        etiqueta = f"{v}"
        if (p,i) in ubic:
            etiqueta += f"\n{ubic[(p,i)]}"
        fila.append(etiqueta)
    matriz_data.append(fila)

tm = Table(matriz_data, colWidths=[1.6*cm]+[3*cm]*5, rowHeights=[0.9*cm]+[1.6*cm]*5)
style_cmds = [
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1a3a5c")),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("BACKGROUND", (0,1), (0,-1), colors.HexColor("#1a3a5c")),
    ("TEXTCOLOR", (0,1), (0,-1), colors.white),
    ("FONTNAME", (0,1), (0,-1), "Helvetica-Bold"),
    ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("FONTSIZE", (0,0), (-1,-1), 8),
]
for r in range(1, 6):
    p = 6 - r  # fila r corresponde a probabilidad p
    for c in range(1, 6):
        i = c
        v = p*i
        style_cmds.append(("BACKGROUND", (c, r), (c, r), color_de_valor(v)))
tm.setStyle(TableStyle(style_cmds))
story.append(tm)
story.append(Spacer(1, 0.3*cm))

story.append(Paragraph("6.1. Niveles de Riesgo", styles["H2"]))
niveles = [
    ["Nivel", "Rango (P×I)", "Color", "Acción requerida"],
    ["Bajo", "1 – 4", "Verde", "Monitorear. Puede aceptarse."],
    ["Medio", "5 – 9", "Amarillo", "Plan de acción a mediano plazo."],
    ["Alto", "10 – 15", "Naranja", "Tratamiento prioritario a corto plazo."],
    ["Crítico", "16 – 25", "Rojo", "Acción inmediata. Escalar a dirección."],
]
tn = tabla_estandar(niveles, [2.6*cm, 2.8*cm, 2.4*cm, 8.2*cm], font_size=8.5)
tn.setStyle(TableStyle([
    ("BACKGROUND", (0,1),(-1,1), NIVEL_COLOR["Bajo"]),
    ("BACKGROUND", (0,2),(-1,2), NIVEL_COLOR["Medio"]),
    ("BACKGROUND", (0,3),(-1,3), NIVEL_COLOR["Alto"]),
    ("BACKGROUND", (0,4),(-1,4), NIVEL_COLOR["Crítico"]),
]))
story.append(tn)

story.append(PageBreak())

# ---------- 7. EVALUACIÓN DE RIESGOS ----------
story.append(Paragraph("7. Evaluación de Riesgos", styles["H1"]))
riesgos = [
    ["ID","Activo","Amenaza","Prob.","Imp.","Valor","Nivel","Justificación breve"],
    ["R01","A01","T01","4","5","20","Crítico","Sector salud muy golpeado por ransomware (DBIR); paraliza la atención."],
    ["R02","A02","T02","3","5","15","Alto","Datos de salud son sensibles (Ley 25.326); fuga con sanciones severas."],
    ["R03","A05","T03","4","4","16","Crítico","Elemento humano en la mayoría de brechas; 120 empleados sin MFA."],
    ["R04","A01","T04","3","5","15","Alto","Debilidad ya detectada por auditoría; agrava cualquier incidente."],
    ["R05","A04","T05","4","3","12","Alto","Práctica habitual sin gestión de identidades; facilita fraude interno."],
    ["R06","A07","T06","3","4","12","Alto","Integraciones externas con configuraciones heredadas sin cifrado."],
    ["R07","A02","T07","3","4","12","Alto","Brechas de cumplimiento frecuentes; auditoría señaló debilidades."],
    ["R08","A08","T08","3","3","9","Medio","Movilidad del personal aumenta exposición de dispositivos."],
    ["R09","A09","T09","3","3","9","Medio","Cortes de energía habituales sin redundancia adecuada."],
]
t7 = Table(riesgos, colWidths=[1.1*cm,1.4*cm,1.6*cm,1.2*cm,1.2*cm,1.3*cm,1.6*cm,7.6*cm], repeatRows=1)
style7 = [
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1a3a5c")),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 7.3),
    ("GRID", (0,0), (-1,-1), 0.4, colors.grey),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
]
for idx, fila in enumerate(riesgos[1:], start=1):
    nivel = fila[6]
    style7.append(("BACKGROUND", (6, idx), (6, idx), NIVEL_COLOR[nivel]))
t7.setStyle(TableStyle(style7))
story.append(t7)

story.append(PageBreak())

# ---------- 8. TRATAMIENTO Y RESIDUAL ----------
story.append(Paragraph("8. Tratamiento de Riesgos y Riesgo Residual", styles["H1"]))
tratamiento = [
    ["Riesgo","Estrategia","Salvaguardas propuestas","Tipo","Prob.\nresid.","Imp.\nresid.","Val.\nresid.","Nivel\nresid."],
    ["R01","Mitigar","EDR en endpoints/servidores, segmentación de red, parcheo mensual (PA-01)","Técnica","2","4","8","Medio"],
    ["R02","Mitigar","Cifrado en reposo, mínimo privilegio, logging y DLP (PA-02)","Técnica","2","4","8","Medio"],
    ["R03","Mitigar","Capacitación trimestral y MFA en correo/sistema clínico (PA-03)","Admin.","2","3","6","Medio"],
    ["R04","Mitigar","Backups 3-2-1 con pruebas periódicas de restauración","Técnica","2","3","6","Medio"],
    ["R05","Mitigar","RBAC con mínimo privilegio, baja de cuentas compartidas","Admin.","2","3","6","Medio"],
    ["R06","Mitigar","Cifrado TLS extremo a extremo, validación y monitoreo","Técnica","2","3","6","Medio"],
    ["R07","Mitigar","Programa de cumplimiento y designación de responsable de datos","Admin.","2","3","6","Medio"],
    ["R08","Mitigar","Cifrado de disco (BitLocker/LUKS) y MDM básico","Técnica","2","2","4","Bajo"],
    ["R09","Mitigar/Aceptar","UPS dimensionada, generador, alta disponibilidad","Física","2","2","4","Bajo"],
]
t8 = Table(tratamiento, colWidths=[1.4*cm,2.2*cm,7.2*cm,1.7*cm,1.3*cm,1.3*cm,1.3*cm,1.6*cm], repeatRows=1)
style8 = [
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1a3a5c")),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE", (0,0), (-1,-1), 7),
    ("GRID", (0,0), (-1,-1), 0.4, colors.grey),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
]
for idx, fila in enumerate(tratamiento[1:], start=1):
    nivel = fila[7]
    style8.append(("BACKGROUND", (7, idx), (7, idx), NIVEL_COLOR[nivel]))
t8.setStyle(TableStyle(style8))
story.append(t8)
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph(
    "Tipo de salvaguarda: Técnica / Física / Administrativa. Con el tratamiento propuesto, ningún riesgo "
    "permanece en nivel Alto o Crítico: los dos riesgos originalmente críticos (R01, R03) bajan a Medio, "
    "y los cinco riesgos Altos también bajan a Medio, mientras que R08 y R09 bajan de Medio a Bajo.",
    styles["Chico"]))

story.append(PageBreak())

# ---------- 9. RESUMEN ----------
story.append(Paragraph("9. Resumen de Resultados", styles["H1"]))
resumen = [
    ["Nivel", "Cantidad de riesgos", "% del total"],
    ["Crítico", "2", "22,2 %"],
    ["Alto", "5", "55,6 %"],
    ["Medio", "2", "22,2 %"],
    ["Bajo", "0", "0 %"],
    ["Total", "9", "100 %"],
]
tr = tabla_estandar(resumen, [4*cm, 6*cm, 6*cm], font_size=9)
tr.setStyle(TableStyle([
    ("BACKGROUND", (0,1),(-1,1), NIVEL_COLOR["Crítico"]),
    ("BACKGROUND", (0,2),(-1,2), NIVEL_COLOR["Alto"]),
    ("BACKGROUND", (0,3),(-1,3), NIVEL_COLOR["Medio"]),
    ("BACKGROUND", (0,4),(-1,4), NIVEL_COLOR["Bajo"]),
    ("FONTNAME", (0,5),(-1,5), "Helvetica-Bold"),
]))
story.append(tr)
story.append(Spacer(1, 0.4*cm))

story.append(Paragraph("10. Conclusiones y Recomendaciones", styles["H1"]))
story.append(Paragraph(
    "El análisis muestra que más del 77% de los riesgos identificados se ubican en niveles Alto o Crítico, "
    "lo que confirma las debilidades detectadas por la auditoría externa y justifica una intervención "
    "prioritaria. Los dos riesgos críticos (ransomware y phishing) comparten una causa raíz común: la "
    "ausencia de controles técnicos básicos (EDR, MFA) y de concientización del personal, por lo que "
    "atacarlos en conjunto (planes PA-01 y PA-03) genera el mayor retorno en reducción de riesgo. "
    "Se recomienda a la Dirección aprobar el presupuesto conjunto de los tres planes de acción "
    "(aproximadamente USD 24.000), designar formalmente a los responsables de cada plan y establecer "
    "una revisión trimestral del registro de riesgos en SimpleRisk para verificar que el riesgo residual "
    "se mantenga dentro de los niveles Bajo/Medio proyectados.",
    styles["Cuerpo"]))
story.append(Spacer(1, 0.4*cm))

story.append(Paragraph("11. Declaración de Buenas Prácticas", styles["H1"]))
decl_data = [[Paragraph(
    "<b>Compromiso profesional:</b> Como estudiante de Seguridad Aplicada a Sistemas de Información, "
    "declaro que el presente análisis de riesgos fue elaborado aplicando las buenas prácticas de la "
    "disciplina, con criterio ético, fundamentos técnicos y respetando el marco normativo vigente.",
    styles["Chico"])]]
td = Table(decl_data, colWidths=[16.5*cm])
td.setStyle(TableStyle([
    ("BOX", (0,0), (-1,-1), 1, colors.HexColor("#1a3a5c")),
    ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#eef3f8")),
    ("TOPPADDING", (0,0), (-1,-1), 10),
    ("BOTTOMPADDING", (0,0), (-1,-1), 10),
    ("LEFTPADDING", (0,0), (-1,-1), 10),
]))
story.append(td)
story.append(Spacer(1, 1.2*cm))
firma = Table([["_"*35, "_"*20]], colWidths=[9*cm, 6*cm])
story.append(firma)
story.append(Table([["Firma del alumno/a", "Fecha"]], colWidths=[9*cm, 6*cm]))
story.append(Spacer(1, 0.4*cm))

story.append(Paragraph("12. Referencias Bibliográficas", styles["H1"]))
refs = [
    "Chicano Tejada, E. (2023). <i>Auditoría de seguridad informática</i>. IFCT0109 (2.ª ed.). IC Editorial — eLibro.",
    "ISO/IEC (2005). <i>Information security management 27001</i>.",
    "ISO/IEC (2018). <i>ISO/IEC 27005: Information security risk management</i>.",
    "NIST (2012). <i>Guide for Conducting Risk Assessments (SP 800-30 Rev. 1)</i>.",
    "OWASP Risk Rating Methodology: https://owasp.org/www-community/OWASP_Risk_Rating_Methodology",
    "Verizon (2025/2026). <i>Data Breach Investigations Report (DBIR)</i>.",
]
for r in refs:
    story.append(Paragraph(f"• {r}", styles["Chico"]))

doc.build(story)
print("PDF generado: matriz_riesgos_A03.pdf")
