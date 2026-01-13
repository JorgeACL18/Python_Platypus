import os

from reportlab.lib.colors import blueviolet
from reportlab.platypus import Paragraph, Image, Spacer, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

guion = []
hojaEstilo = getSampleStyleSheet()

cabecera = hojaEstilo["Heading2"]
cabecera.fontSize=18
cabecera.alignment=2

tit = ['Nombre de tu empresa', '', 'Logo de la Empresa']
inf1 = ['Dirección', '', '']
inf2 = ['Ciudad y País', '', '']
inf3 = ['CIF/NIF', 'Fecha Emisión', 'DD/MM/AAA']
inf4 = ['Teléfono', 'Número de Factura', 'A0001']
inf5 = ['Mail', '', '']
tabla = Table ([tit, inf1, inf2, inf3, inf4, inf5])


titulo=Paragraph("FACTURA SIMPLIFICADA", cabecera)
guion.append(titulo)

guion.append(tabla)

doc = SimpleDocTemplate("Factura1.pdf", pagesize=A4, showBoundary=0)
doc.build (guion)