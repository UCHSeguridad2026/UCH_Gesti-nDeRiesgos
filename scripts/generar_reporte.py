from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import HexColor
import os


# ============================================================
# CONFIGURACIÓN
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(BASE_DIR, "reporte-ejecutivo", "reporte.pdf")

os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

PAGE_WIDTH, PAGE_HEIGHT = A4


# ============================================================
# ESTILOS
# ============================================================

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "ReportTitle",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=20,
    leading=23,
    alignment=TA_CENTER,
    spaceAfter=5 * mm,
)

subtitle_style = ParagraphStyle(
    "Subtitle",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=10,
    leading=13,
    alignment=TA_CENTER,
    textColor=HexColor("#555555"),
    spaceAfter=7 * mm,
)

section_style = ParagraphStyle(
    "Section",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=12,
    leading=14,
    spaceBefore=3 * mm,
    spaceAfter=2 * mm,
    textColor=HexColor("#1F2937"),
)

body_style = ParagraphStyle(
    "Body",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=8.7,
    leading=11.5,
    spaceAfter=2.5 * mm,
)

small_style = ParagraphStyle(
    "Small",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=7.5,
    leading=9.5,
    spaceAfter=1.5 * mm,
)

bullet_style = ParagraphStyle(
    "Bullet",
    parent=body_style,
    leftIndent=4 * mm,
    firstLineIndent=-3 * mm,
    spaceAfter=1.5 * mm,
)


# ============================================================
# ENCABEZADO Y PIE DE PÁGINA
# ============================================================

def header_footer(canvas, doc):
    canvas.saveState()

    # Encabezado
    canvas.setFont("Helvetica-Bold", 7.5)
    canvas.setFillColor(HexColor("#555555"))
    canvas.drawString(
        18 * mm,
        PAGE_HEIGHT - 12 * mm,
        "SEGURIDAD DE SISTEMAS · GESTIÓN DE RIESGOS"
    )

    # Línea superior
    canvas.setStrokeColor(HexColor("#CCCCCC"))
    canvas.line(
        18 * mm,
        PAGE_HEIGHT - 14 * mm,
        PAGE_WIDTH - 18 * mm,
        PAGE_HEIGHT - 14 * mm,
    )

    # Pie
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(HexColor("#666666"))
    canvas.drawString(
        18 * mm,
        9 * mm,
        "Reporte ejecutivo · Clínica Privada"
    )

    canvas.drawRightString(
        PAGE_WIDTH - 18 * mm,
        9 * mm,
        f"Página {doc.page}"
    )

    canvas.restoreState()


# ============================================================
# DOCUMENTO
# ============================================================

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=18 * mm,
    leftMargin=18 * mm,
    topMargin=20 * mm,
    bottomMargin=16 * mm,
    title="Reporte Ejecutivo - Gestión de Riesgos de Seguridad de la Información",
    author="Camila Olivera",
)

story = []


# ============================================================
# PORTADA / IDENTIFICACIÓN
# ============================================================

story.append(Spacer(1, 3 * mm))

story.append(
    Paragraph(
        "REPORTE EJECUTIVO",
        title_style
    )
)

story.append(
    Paragraph(
        "Gestión de Riesgos de Seguridad de la Información",
        subtitle_style
    )
)

info_data = [
    [
        Paragraph("<b>Organización</b>", small_style),
        Paragraph("Clínica Privada", small_style),
        Paragraph("<b>Destinatario</b>", small_style),
        Paragraph("Directorio de la Clínica", small_style),
    ],
    [
        Paragraph("<b>Alcance</b>", small_style),
        Paragraph("Sistemas de información, datos e infraestructura crítica", small_style),
        Paragraph("<b>Fecha</b>", small_style),
        Paragraph("Septiembre 2026", small_style),
    ],
]

info_table = Table(
    info_data,
    colWidths=[25 * mm, 62 * mm, 25 * mm, 62 * mm],
)

info_table.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BOX", (0, 0), (-1, -1), 0.5, HexColor("#CCCCCC")),
            ("INNERGRID", (0, 0), (-1, -1), 0.25, HexColor("#DDDDDD")),
            ("BACKGROUND", (0, 0), (0, -1), HexColor("#F3F4F6")),
            ("BACKGROUND", (2, 0), (2, -1), HexColor("#F3F4F6")),
            ("LEFTPADDING", (0, 0), (-1, -1), 3 * mm),
            ("RIGHTPADDING", (0, 0), (-1, -1), 3 * mm),
            ("TOPPADDING", (0, 0), (-1, -1), 2 * mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
        ]
    )
)

story.append(info_table)
story.append(Spacer(1, 5 * mm))


# ============================================================
# 1. RESUMEN EJECUTIVO
# ============================================================

story.append(
    Paragraph("1. Resumen ejecutivo", section_style)
)

story.append(
    Paragraph(
        "La clínica privada cuenta con <b>120 empleados</b> y atiende aproximadamente "
        "<b>800 pacientes diarios</b>. El análisis inicial identificó siete riesgos "
        "asociados principalmente a historias clínicas digitales, datos personales y "
        "de seguros, facturación, infraestructura y continuidad operativa.",
        body_style
    )
)

story.append(
    Paragraph(
        "La evaluación determinó <b>3 riesgos Críticos y 4 riesgos Altos</b>, por lo "
        "que se recomienda priorizar acciones de mitigación sobre los eventos que "
        "puedan comprometer la confidencialidad de la información, la continuidad "
        "de la atención y la integridad de los datos.",
        body_style
    )
)


# Indicadores ejecutivos

indicator_data = [
    [
        Paragraph("<b>7</b><br/>Riesgos identificados", small_style),
        Paragraph("<b>3</b><br/>Riesgos Críticos", small_style),
        Paragraph("<b>4</b><br/>Riesgos Altos", small_style),
        Paragraph("<b>3</b><br/>Planes de acción", small_style),
    ]
]

indicator_table = Table(
    indicator_data,
    colWidths=[43 * mm, 43 * mm, 43 * mm, 43 * mm],
)

indicator_table.setStyle(
    TableStyle(
        [
            ("BOX", (0, 0), (-1, -1), 0.5, HexColor("#BBBBBB")),
            ("INNERGRID", (0, 0), (-1, -1), 0.5, HexColor("#BBBBBB")),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 3 * mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm),
        ]
    )
)

story.append(indicator_table)


# ============================================================
# 2. TOP 5 RIESGOS
# ============================================================

story.append(
    Paragraph("2. Top 5 riesgos por nivel", section_style)
)

story.append(
    Paragraph(
        "La priorización se realizó mediante la matriz de <b>Probabilidad × Impacto</b>, "
        "utilizando una escala de 1 a 5. Los niveles corresponden a: Bajo (1–4), "
        "Medio (5–9), Alto (10–15) y Crítico (16–25).",
        small_style
    )
)

risk_data = [
    [
        Paragraph("<b>ID</b>", small_style),
        Paragraph("<b>Riesgo</b>", small_style),
        Paragraph("<b>P</b>", small_style),
        Paragraph("<b>I</b>", small_style),
        Paragraph("<b>P×I</b>", small_style),
        Paragraph("<b>Nivel</b>", small_style),
        Paragraph("<b>Tratamiento</b>", small_style),
    ],
    [
        "R01",
        Paragraph("Acceso no autorizado a historias clínicas digitales", small_style),
        "4",
        "5",
        "20",
        "CRÍTICO",
        "Mitigar",
    ],
    [
        "R02",
        Paragraph("Ransomware sobre el sistema de historias clínicas", small_style),
        "4",
        "5",
        "20",
        "CRÍTICO",
        "Mitigar",
    ],
    [
        "R04",
        Paragraph("Indisponibilidad del sistema de historias clínicas", small_style),
        "4",
        "5",
        "20",
        "CRÍTICO",
        "Mitigar",
    ],
    [
        "R03",
        Paragraph("Pérdida o corrupción de historias clínicas digitales", small_style),
        "3",
        "5",
        "15",
        "ALTO",
        "Mitigar",
    ],
    [
        "R05",
        Paragraph("Filtración de datos personales y médicos de pacientes", small_style),
        "3",
        "5",
        "15",
        "ALTO",
        "Mitigar",
    ],
]

risk_table = Table(
    risk_data,
    colWidths=[12 * mm, 67 * mm, 9 * mm, 9 * mm, 13 * mm, 18 * mm, 24 * mm],
    repeatRows=1,
)

risk_table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), HexColor("#E5E7EB")),
            ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#111827")),
            ("BOX", (0, 0), (-1, -1), 0.5, HexColor("#AAAAAA")),
            ("INNERGRID", (0, 0), (-1, -1), 0.25, HexColor("#CCCCCC")),
            ("ALIGN", (0, 0), (0, -1), "CENTER"),
            ("ALIGN", (2, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 2 * mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
        ]
    )
)

story.append(risk_table)


# ============================================================
# 3. PLANES DE ACCIÓN
# ============================================================

story.append(
    Paragraph("3. Estado de los planes de acción", section_style)
)

story.append(
    Paragraph(
        "Se registraron tres planes de acción en SimpleRisk. Todos fueron "
        "<b>aceptados</b> y presentan un <b>avance inicial de 0%</b>, por lo que "
        "requieren seguimiento hasta verificar su implementación.",
        body_style
    )
)

plan_data = [
    [
        Paragraph("<b>Riesgo</b>", small_style),
        Paragraph("<b>Plan</b>", small_style),
        Paragraph("<b>Vencimiento</b>", small_style),
        Paragraph("<b>Presupuesto</b>", small_style),
        Paragraph("<b>Estado</b>", small_style),
    ],
    [
        "R02",
        Paragraph("Backups y recuperación", small_style),
        "31/10/2026",
        "$0–$100.000",
        "Aceptado · 0%",
    ],
    [
        "R01",
        Paragraph("MFA y revisión de permisos", small_style),
        "30/11/2026",
        "$0–$100.000",
        "Aceptado · 0%",
    ],
    [
        "R04",
        Paragraph("Redundancia y continuidad", small_style),
        "31/12/2026",
        "$100.001–$200.000",
        "Aceptado · 0%",
    ],
]

plan_table = Table(
    plan_data,
    colWidths=[15 * mm, 58 * mm, 28 * mm, 35 * mm, 26 * mm],
    repeatRows=1,
)

plan_table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), HexColor("#E5E7EB")),
            ("BOX", (0, 0), (-1, -1), 0.5, HexColor("#AAAAAA")),
            ("INNERGRID", (0, 0), (-1, -1), 0.25, HexColor("#CCCCCC")),
            ("ALIGN", (0, 0), (0, -1), "CENTER"),
            ("ALIGN", (2, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 2 * mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
        ]
    )
)

story.append(plan_table)


# ============================================================
# 4. RECOMENDACIONES PRIORITARIAS
# ============================================================

story.append(
    Paragraph("4. Recomendaciones prioritarias", section_style)
)

recommendations = [
    "<b>1. Proteger el acceso a la información sensible.</b> Implementar MFA, "
    "principio de mínimo privilegio, revisión periódica de permisos y revocación "
    "inmediata de cuentas de personal desvinculado.",

    "<b>2. Fortalecer la recuperación ante ransomware y pérdida de datos.</b> "
    "Mantener copias protegidas, preferentemente offline o inmutables, verificar "
    "su integridad y realizar pruebas periódicas de restauración.",

    "<b>3. Aplicar defensa en profundidad.</b> La estrategia puede representarse "
    "mediante la analogía de los <b>tres cerditos</b>: una primera capa de "
    "prevención mediante controles de acceso, una segunda capa de detección "
    "mediante monitoreo y registros, y una tercera capa de recuperación mediante "
    "backups, redundancia y continuidad operativa.",

    "<b>4. Considerar las amenazas externas.</b> El ejemplo de <b>Caperucita Roja "
    "y el lobo feroz</b> permite representar que una organización debe asumir la "
    "existencia de amenazas externas y establecer controles antes, durante y "
    "después de un incidente, en lugar de depender de una única barrera.",

    "<b>5. Proteger la infraestructura crítica.</b> Incorporar redundancia eléctrica "
    "y de conectividad, UPS, monitoreo y procedimientos de contingencia. Los centros "
    "de datos nunca deberían ubicarse junto a cocinas ni debajo de lavamanos, "
    "piletas o piscinas, debido al riesgo combinado de incendio e inundación.",

    "<b>6. Mantener actualizado el análisis.</b> Revisar los riesgos y planes de "
    "acción periódicamente y ante cambios relevantes en sistemas, procesos, "
    "infraestructura o amenazas.",
]

for item in recommendations:
    story.append(Paragraph("• " + item, bullet_style))


# ============================================================
# CONCLUSIÓN EJECUTIVA
# ============================================================

story.append(
    Paragraph("Conclusión para el Directorio", section_style)
)

story.append(
    Paragraph(
        "La gestión de riesgos debe mantenerse como un proceso continuo. La "
        "prioridad inmediata debe centrarse en proteger la información clínica "
        "sensible y asegurar la continuidad de los servicios esenciales. La "
        "implementación y seguimiento de los planes definidos permitirá mejorar "
        "progresivamente las capacidades de prevención, detección, respuesta y "
        "recuperación de la clínica.",
        body_style
    )
)


# ============================================================
# GENERACIÓN
# ============================================================

doc.build(
    story,
    onFirstPage=header_footer,
    onLaterPages=header_footer,
)

print(f"PDF generado correctamente en: {OUTPUT}")
