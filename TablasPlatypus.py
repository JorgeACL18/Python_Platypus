from reportlab.platypus import Paragraph, Image, Spacer, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

guion = []

cab = ['', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
actM = ['Mañana', 'Cole', 'Correr', '-', '-', '-', 'Estudiar', 'Trabajar', 'Correr']
actT = ['Tarde', 'Trabajar', 'Clases', 'Clases', 'Trabajar', 'Trabajar', 'Leer']
actN = ['Noche', '-', 'Trabajar', 'Trabajar', 'Trabajar', '-', '-', '-']

tabla = Table ([cab, actM, actT, actN])
tabla.setStyle([('TEXTOCOLOR', (1,-4), (7,-4), colors.red), ('TEXTOCOLOR', (0,0), (0,3), colors.blue)])


guion.append(tabla)
doc = SimpleDocTemplate("EjemploPlaypus_Tabla.pdf", pagesize=A4, showBoundary=0)
doc.build (guion)