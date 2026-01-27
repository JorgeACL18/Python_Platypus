import sqlite3

import self
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Paragraph, Image, Spacer, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.charts.piecharts import Pie


bbdd = "bdTendaOrdeadoresBig.bd"
def obtener_clientes_mayor_facturacion(limite = 10):
    conn = sqlite3.connect(bbdd)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT c.nome,
        COUNT(DISTINCT f.id_factura) as num_facturas,
        SUM(If.cantidade * If.prezo_unitario * (1- If.desconto/100) * (1 + p.iva/100)) as facturacion_total
    FROM clientes c
    JOIN facturas f ON c.id_cliente = f.id_cliente
    JOIN linhas_factura If ON f.id_factura = If.id_factura
    JOIN productos ON If.id_producto = p.id_producto
    GROUP BY c.id_cliente, c.nome
    ORDER BY facturacion_total DESC
    LIMIT ?"""), (limite,)

    resultados =cursor.fetchall()
    conn.close()

    return resultados

guion = []
d = Drawing(400, 200)
hoja = getSampleStyleSheet()
graf = Pie()

cabecera = hoja["Heading1"]
cabecera.fontName = 'Helvetica-Bold'
cabecera.fontSize=20
cabecera.alignment=0
cabecera.textColor = colors.black

subt = hoja["Heading2"]
subt.fontName = 'Helvetica'
subt.fontSize=14
subt.alignment=0
subt.textColor = colors.black

titulo=Paragraph("GRÁFICA", cabecera)
tit2 = Paragraph("TABLA", cabecera)
subt1=Paragraph("Aquí podemos ver la gráfica tarta de la facturación total de cada cliente", subt)
subt2=Paragraph("En este apartado podremos ver la tabla donde aparece el posicionamiento de los cliente según la cantidad de facturación total", subt)

graf.x = 140
graf.y = 15
graf.width = 170
graf.height = 170
graf.data = [50,40,30,20,10]
graf.labels = ['Tecnoloxía TIC Nordés SL','Comercial Informática SA','Empresa Solucións Galicia SL','Consultoría Galicia e Fillos','Sistemas Informáticos SL']
graf.sideLabels = 1

colores = [colors.pink, colors.blueviolet, colors.rosybrown, colors.lightsalmon, colors.lightgoldenrodyellow]
for i, color in enumerate(colores):
    graf.slices[i].fillColor = color

d.add(graf)



blank = ['','','','']
lin = ['Pos.', 'Cliente', 'Nº Factura', 'Facturación total']
inf1 = ['1', 'Tecnoloxía TIC Nordés SL', '3', '5036.42 EUR.']
inf2 = ['2', 'Comercial Informática SA', '2', '4239.63 EUR.']
inf3 = ['3', 'Empresa Solucións Galicia SL', '3', '901.37 EUR.']
inf4 = ['4', 'Consultoría Galicia e Fillos', '2', '865.84 EUR.']
inf5 = ['5', 'Sistemas Informáticos SL', '2', '108.92 EUR.']

tab = Table([blank, lin, inf1, inf2, inf3, inf4, inf5, blank], colWidths=[50, 230, 60, 110], hAlign='CENTER')
tab.setStyle([
    ('INNERGRID', (0,1), (3,6), 1, colors.black),
    ('SPAN', (0,0), (3,0)),
    ('LEFTPADDING', (0,0), (0,0), 60),
    ('BOX', (0,1), (3,6), 1, colors.black),
    ('ALIGN', (0,1), (3,1), 'CENTER'),
    ('ALIGN', (0,2), (0,6), 'CENTER'),
    ('ALIGN', (2,2), (3, 6), 'CENTER'),
    ('BACKGROUND', (0,1), (3,1), colors.deeppink),
    ('BACKGROUND', (0,3), (3,3), colors.lightpink),
    ('BACKGROUND', (0, 5), (3, 5), colors.lightpink),
    ('TEXTCOLOR', (0,1),(3,1), colors.white),
    ('LINEBELOW', (0,7), (3,7), 1, colors.black),
    ('BOTTOMPADDING', (0,7), (3,7), 10)
])

cuerpoTexto = hoja['BodyText']
cuerpoTexto.fontSize = 12
cuerpoTexto.fontName = 'Helvetica-Oblique'
texto = "El cliente que más ha facturado es Solucións TIC Nordés SL, con 5036.42 EUR. Tods los clientes en total sumán una cantidad de 11852.18 EUR. Amedia de facturas por cliente de los 5 primeros clientes es de 2.2 facturas"
parrafo2 = Paragraph(texto, cuerpoTexto)

guion.append(titulo)
guion.append(subt1)
guion.append(Spacer(50, 50))
guion.append(d)
guion.append(Spacer(50, 50))
guion.append(tit2)
guion.append(subt2)
guion.append(tab)
guion.append(Spacer(50, 15))
guion.append(parrafo2)

doc = SimpleDocTemplate("EXAMEN.pdf", pagesize=A4, showBoundary=0)
doc.build (guion)



