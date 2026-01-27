# Doc con Platypus
from reportlab.platypus import Paragraph # parágrafos
from reportlab.platypus import Image # imaxes
from reportlab.lib.styles import getSampleStyleSheet # folla de estilos
from reportlab.graphics.charts.barcharts import VerticalBarChart # gráfico de barras
from reportlab.graphics.charts.textlabels import Label # etiquetas de texto
from reportlab.graphics.shapes import Drawing # debuxos
from reportlab.lib import colors # cor
from reportlab.platypus import SimpleDocTemplate, Spacer # espazo
from reportlab.lib.pagesizes import A4 # tamaño da páxina A4

d = Drawing(400,200)




guion = []




follaEstilo = getSampleStyleSheet() # obtén a folla de estilos predeterminada
print(follaEstilo.list()) # amosa os estilos dispoñibles
cabeceira = follaEstilo["Heading4"] # copia da cabeceira

cabeceira.pageBreakBefore = 0 # non facer salto de páxina antes
cabeceira.backColor = colors.lightblue # cor de fondo

paragrafo = Paragraph("CABECEIRA DO DOCUMENTO", cabeceira) # crea un parágrafo coa cabeceira
guion.append(paragrafo)

texto = "Texto incluido no documento, e que forma o contido" * 1000 # texto longo

corpoTexto = follaEstilo['BodyText'] # copia do estilo de corpo de texto
corpoTexto.fontSize = 12 # tamaño da fonte
paragrafo2 = Paragraph(texto,corpoTexto) # crea un parágrafo co texto e o estilo de corpo de texto
guion.append(paragrafo2)

guion.append(Spacer(0,30))# espazo vertical
imaxe = Image("box-pixilart.png",width=400,height=400) # crea a imaxe
guion.append(imaxe) # engade a imaxe ao guion

cabeceiraCursiva = follaEstilo["Heading4"]  # copia da cabeceira
cabeceiraCursiva.fontName = 'Helvetica-Oblique' # fonte cursiva
cabeceiraCursiva.fontSize = 18 # tamaño da fonte
cabeceiraCursiva.alignment = 1 # aliñado ao centro
cabeceiraCursiva.borderColor = colors.blue # cor da borda

paragrafo3 = Paragraph("Cabezeira cursiva", cabeceiraCursiva)
guion.append(paragrafo3)

guion.append(Spacer(0,20))
guion.append(d)

doc = SimpleDocTemplate("4º ExemplosPlatypus.pdf", pagesize = A4,showBoundary = 1)
doc.build(guion)