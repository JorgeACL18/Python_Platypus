import sqlite3

from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Paragraph, Image, Spacer, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.charts.piecharts import Pie


guion = []
bbdd = "bdTendaOrdeadoresBig.bd"
def obter_produtos_mais_vendidos(limite=10):
    conn = sqlite3.connect(bbdd)
    cursor = conn.cursor()

    cursor.execute("""
SELECT
p.nome,
SUM(if.cantidade) as total_vendido,
SUM(if.cantidade * if.prezo_unitario * (1 - if.desconto/100)) as facturacion
FROM linhas_factura if
JOIN produtos p ON if.id_produto = p.id_produto
GROUP BY p.id_produto, p.nome
ORDER BY total_vendido DESC
LIMIT ?""", (limite,))

    resultado = cursor.fetchall()
    conn.close()

    return resultado

def xerar_factura():
    hoja = getSampleStyleSheet()
    datos = obter_produtos_mais_vendidos(10)
    cabecera = ['Pos.', 'Cliente', 'Nº Factura', 'Facturación total']
    datosTaboa = []
    datosTaboa.append(cabecera)
    for orde, linha in enumerate (datos):
        datosTaboa.append([orde+1, linha[0], linha[1],f"{linha[2]:.3f}"])
    print(datosTaboa)

    t = Table (datosTaboa, colWidths=[50, 230, 60, 110], hAlign='CENTER')
    estilo = [
        # Cabeceira
        ('BACKGROUND', (0, 0), (-1, 0), colors.deeppink),
        ('TEXTCOLOR', (0, 0), (3, 0), colors.white),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),

        #
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (2, 1), (3, -1), 'CENTER'),
        ('ALIGN', (0, 1), (0, -1), 'CENTER'),
    ]
    for i in range(2, len(datosTaboa), 2):
        estilo.append(('BACKGROUND', (0, i), (-1, i), colors.lightpink))
    t.setStyle(estilo)


    facturacion = []
    etiquetas = []
    for linha in datos:
        facturacion.append(linha[-1])
        etiquetas.append(linha[0])
    ancho = 400
    alto = 350
    debuxo = Drawing (ancho, alto)
    tarta = Pie()
    tarta.x = 140
    tarta.y = 15
    tarta.width = 170
    tarta.height = 170
    tarta.data = facturacion
    tarta.labels = etiquetas

    cabecera = hoja["Heading1"]
    cabecera.fontName = 'Helvetica-Bold'
    cabecera.fontSize = 20
    cabecera.alignment = 0
    cabecera.textColor = colors.black

    subt = hoja["Heading2"]
    subt.fontName = 'Helvetica'
    subt.fontSize = 14
    subt.alignment = 0
    subt.textColor = colors.black

    titulo = Paragraph("GRÁFICA", cabecera)
    tit2 = Paragraph("TABLA", cabecera)
    subt1 = Paragraph("Aquí podemos ver la gráfica tarta de la facturación total de cada cliente", subt)
    subt2 = Paragraph(
        "En este apartado podremos ver la tabla donde aparece el posicionamiento de los cliente según la cantidad de facturación total",
        subt)

    guion.append(titulo)
    guion.append(subt1)
    guion.append(Spacer(50, 50))
    guion.append(debuxo)
    guion.append(Spacer(50, 50))
    guion.append(tit2)
    guion.append(subt2)
    guion.append(t)


    doc = SimpleDocTemplate("ejemplodetablaconbbdd.pdf", pagesize=A4)
    doc.build(guion)

xerar_factura()


