from reportlab.platypus import Paragraph, Image, Spacer, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

guion = []

hojaEstilo = getSampleStyleSheet()

cabecera = hojaEstilo["Heading1"]
cabecera.fontName='Helvetica-Oblique'
cabecera.pageBreakBefore = 0
cabecera.backColor = colors.lightblue
cabecera.fontSize=22
cabecera.alignment=1

cabecera2 = hojaEstilo["Heading2"]
cabecera2.fontName='Helvetica-Oblique'
cabecera2.fontSize=18
cabecera2.alignment=2

titulo= Paragraph("Titulo del documento", cabecera)
guion.append(titulo)

parrafo = Paragraph("Cabecera del documento", cabecera2)
guion.append (parrafo)

texto = "Texto incluido en el documento, y que forma el contenido. " * 10

cuerpoTexto = hojaEstilo['BodyText']
cuerpoTexto.fontSize = 12
parrafo2 = Paragraph(texto, cuerpoTexto)
guion.append(parrafo2)
guion.append(Spacer(0,200))

imagen = Image("800px-Cleffa.png", width=100,height=100)
guion.append(imagen)

doc = SimpleDocTemplate("EjemploPlaypus.pdf", pagesize=A4, showBoundary=1)
doc.build (guion)