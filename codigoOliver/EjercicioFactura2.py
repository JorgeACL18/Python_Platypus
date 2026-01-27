from reportlab.platypus import Table, Paragraph, Image, SimpleDocTemplate, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.graphics.shapes import Drawing
from reportlab.lib import   colors
from reportlab.rl_settings import showBoundary

guion = []
d = Drawing(600,300)

guion.append(Spacer(1,80))

imaxe = Image('img.png')

fila0 = ['FACTURA Proforma',imaxe]
fila1 = ['FACTURAR A:','Nº DE FACTURA']
fila2 = ['','Fecha']
fila3 = ['Cliente','']
fila4 = ['Domicilio','Nº de pedido']
fila5 = ['Código postal/ciudad']
fila6 = ['(NIF)','Fecha de vencimiento']
fila7 = ['','Condiciones de pago']

tabla1 = Table([fila0,fila1,fila2,fila3,fila4,fila5,fila6,fila7],[210],[30,15,15,15,15,15,15,15],hAlign='LEFT')
tabla1.setStyle([
    ('BACKGROUND',(0,1),(-1,-1),colors.lightgrey),
    ('FONTSIZE',(0,0),(-1,0),20),
    ('BOTTOMPADDING',(0,0),(-1,0),80),
    ('FONTSIZE',(1,1),(-1,1),15),
    ('FONTNAME',(0,0),(-1,-1),'Helvetica-Bold'),

])

guion.append(tabla1)

guion.append(Spacer(1,40))


fila2_0 = ['Pos.','Concepto/Descripción', 'Cantidad', 'Unidad', 'Precio\nunitario','Importe']
fila2_1 = ['1','','','','','']
fila2_2 = ['2','','','','','']
fila2_3 = ['','','','','','']



tabla2 = Table([fila2_0,fila2_1,fila2_2,fila2_3],[35,136,60,50,70,70],[30,20,20,20],hAlign='LEFT')

tabla2.setStyle([
    ('INNERGRID',(0,0),(-1,-1),0.7,colors.black),
    ('BOX',(0,0),(-1,-1),1,colors.black),
    ('BACKGROUND',(0,0),(-1,0),colors.lightgrey),
    ('VALIGN',(0,0),(-1,0),'TOP'),
    ('ALIGN',(0,0),(-1,0),'CENTRE')
])

guion.append(tabla2)

guion.append(Spacer(1,60))

fila3_0 = ['Método de pago:','','Importe neto']

fila4_1 = ['','','+ IVA de ... %', '']
fila4_2 = ['','','- IRPF de ... %', '']
fila4_3 = ['','','IMPORTE BRUTO','']


tabla3 = Table([fila3_0,fila4_1,fila4_2,fila4_3],hAlign='LEFT',colWidths= [270,30,None,30])

tabla3.setStyle([
    ('BOX',(0,0),(0,2),1,colors.black),
    ('VALIGN',(0,0),(-1,-1),'TOP'),
    ('BOX',(2,0),(3,3),1,colors.black),
    ('INNERGRID',(2,0),(3,3),1,colors.black),
    ('BACKGROUND',(2,3),(3,3),colors.lightgrey)

])

guion.append(tabla3)

txt1 = ['Gracias por su confianza']
txt2 = ['Atentamente, ']
tabla4 = Table([txt1,txt2],hAlign='LEFT')
tabla4.setStyle([
    ('BOTTOMPADDING',(0,0),(-1,0),40)
])

guion.append(tabla4)



doc = SimpleDocTemplate('Repaso.pdf',pagesize = A4, showBoundary = 0)
doc.build(guion)