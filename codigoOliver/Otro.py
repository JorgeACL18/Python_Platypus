from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Table, Spacer
from reportlab.rl_settings import showBoundary
from reportlab.lib import  colors

from reportlab.graphics.charts.barcharts import VerticalBarChart

d = Drawing(800,100)
guion = []

fila0 = ['FACTURA Proforma','']
fila1 = ['FACTURAR A:','Nº DE FACTURA']
fila2 = ['','Fecha']
fila3 = ['Cliente', '']
fila4 = ['Domicilio','Nº de pedido']
fila5 = ['Código postal/ciudad', '']
fila6 = ['(NIF)','Fecha de vencimiento']
fila7 = ['', 'Condiciones de pago']


alturas = [100,20,15,15,15,15,15,15]
anchos = [150,150] #Total 300

tabla1 = Table([fila0,fila1,fila2,fila3,fila4,fila5,fila6,fila7],hAlign='LEFT')
tabla1.setStyle([
    ('BACKGROUND',(0,1),(-1,-1),colors.lightgrey),
    ('ALIGN',(1,1),(-1,1),'RIGHT'),
    ('ALIGN', (1, 2), (-1, 2), 'RIGHT'),
    ('ALIGN', (1, 4), (-1, 4), 'RIGHT'),
    ('ALIGN', (1, 6), (-1, 6), 'RIGHT'),
    ('ALIGN', (1, 7), (-1, 7), 'RIGHT'),
    ('FONTSIZE',(0,0),(-1,0),16),
    ('BOTTOMPADDING',(0,0),(-1,0),60),
    ('FONTNAME',(0,0),(-1,-1),'Helvetica-Bold')
])

guion.append(tabla1)
anchos2 = [30, 100, 45, 40, 45, 40]

fila_vacia = ['','','','','','']
fila8 = ['Pos.','Concepto/Descripción','Cantidad','Unidad','Precio \n unitario', 'Importe']
fila9 = ['1','','','','','']
fila10 = ['2','','','','','']
fila11 = ['','','','','','']


tabla2 = Table([fila_vacia,fila8,fila9,fila10,fila11],colWidths=47,rowHeights=[15,15,15,15,15],hAlign='LEFT')
tabla2.setStyle([
    ('TOPPADDING',(0,0),(-1,0),30),
    ('BOX',(0,1),(-1,-1),0.2,colors.black),
    ('BACKGROUND',(0,1),(-1,1),colors.grey),
    ('BOTTOMPADDING',(0,6),(-1,-1),10),
    ('INNERGRID', (0, 1), (-1, -1), 0.7, colors.black),
    ('FONTSIZE',(0,0),(-1,-1),6),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'), # Mueve todo el texto al borde superior


])

guion.append(tabla2)

guion.append(Spacer(1,30))

alturas2 = [150,150]

fila12 = ['Método de pago']
tabla3 = Table([fila12],alturas2,hAlign='LEFT')
tabla3.setStyle([
    ('TOPPADDING',(0,0),(-1,0),40),
    ('ALIGN',(0,0),(-1,-1),'LEFT'),
    ('BOX',(0,0),(-1,-1),0.7,colors.black),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Mueve todo el texto al borde superior

])

guion.append(tabla3)


grafica = VerticalBarChart()

datos = [(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)]
dat = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15')
grafica.x = 50
grafica.y = 50
grafica.data = datos
grafica.valueAxis.valueMin = 0
grafica.valueAxis.valueMax = 15
grafica.valueAxis.valueStep = 3

grafica.categoryAxis.categoryNames = dat

guion.append(Spacer(1,60))

d.add(grafica)
guion.append(d)



doc = SimpleDocTemplate('Otro.pdf',pagesize = A4, showBoundary = 1)
doc.build(guion)