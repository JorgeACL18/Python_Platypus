import os

from reportlab.platypus import Paragraph, Image, Spacer, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

guion = []
hojaEstilo = getSampleStyleSheet()

cabecera = hojaEstilo["Heading2"]
cabecera.fontSize=18
cabecera.alignment=2
cabecera.textColor = colors.darkseagreen

blanc = ['', '', '', '']
tit = ['Nombre de tu empresa', '', '', 'Logo de la Empresa']
inf1 = ['Dirección', '', '', '']
inf2 = ['Ciudad y País', '', '', '']
inf3 = ['CIF/NIF', '', 'Fecha Emisión', 'DD/MM/AAA']
inf4 = ['Teléfono', '', 'Número de Factura', 'A0001']
inf5 = ['Mail', '', '', '']

tab = ['Descripción', 'Importe', 'Cantidad', 'Total']
pr1 = ['Producto 1', '3,2', '5', '16,00']
pr2 = ['Producto 2', '2,1', '3', '6,30']
pr3 = ['Producto 3', '2,9', '76', '220,40']
pr4 = ['Producto 4', '5', '23', '115,00']
pr5 = ['Producto 5', '4,95', '3', '14,85']
pr6 = ['Producto 6', '6', '2', '12']
total = ['', '', 'TOTAL', '385€']

men = ['Gracias por su confiaza', '', '', '']
tabla = Table ([blanc, tit, inf1, inf2, inf3, inf4, inf5, blanc, tab, pr1, pr2, pr3, pr4, pr5, pr6, blanc, total, blanc, men], colWidths=[195, 50, 95, 95])

tabla.setStyle([('FONTSIZE', (0,1),(0,1), 18),
                ('FONTSIZE', (3,1),(3,1), 13),
                ('FONTSIZE', (0, 18), (3, 18), 15),
                ('FONTSIZE', (2, 16), (3, 16), 15),
                ('FONTNAME', (2, 16), (3, 16), 'Helvetica-Bold'),
                ('FONTNAME', (0, 18), (3, 18), 'Helvetica-Bold'),
                ('BOTTOMPADDING' , (0,1), (3,1), 10),
                ('ALIGN', (2,4), (2,5), 'RIGHT'),
                ('ALIGN', (3, 4), (3, 5), 'CENTER'),
                #('BACKGROUND', (0,9), (3,14), colors.cyan),
                ('BACKGROUND', (0,9), (3,14), colors.palegreen),
                ('BACKGROUND', (0,8), (3,8), colors.green),
                ('ALIGN', (0,8), (2,15), 'CENTER'),
                ('ALIGN', (3,8), (3,8), 'CENTER'),
                ('ALIGN', (3,9), (3,14), 'RIGHT'),
                ('ALIGN', (2,16), (3,16), 'CENTER'),
                ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
                ('TOPPADDING', (2, 16), (3, 16), 11),
                ('BOTTOMPADDING', (2, 16), (3, 16), 18),
                ('BACKGROUND', (2, 16), (3, 16), colors.green),
                ('TEXTCOLOR' ,(0,8),(3,8), colors.white),
                ('TEXTCOLOR', (2, 16), (3, 16), colors.white),
                ('TEXTCOLOR', (0, 1), (3,7), colors.darkolivegreen ),
                ('SPAN', (0,18), (3,18)),
                ('ALIGN', (0,18), (0,18), 'CENTER'),
                ('TOPPADDING', (0, 17), (3, 17), 30),
                ('TOPPADDING', (0,18), (3,18), 15),
                ('LINEABOVE', (0,18), (3,18), 1, colors.black),
                ('RIGHTPADDING', (3,1),(3,1), 100)
                ])


titulo=Paragraph("FACTURA SIMPLIFICADA", cabecera)
guion.append(titulo)

guion.append(tabla)

doc = SimpleDocTemplate("Factura1.pdf", pagesize=A4, showBoundary=0)
doc.build (guion)