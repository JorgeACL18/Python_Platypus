from reportlab.lib import colors
from reportlab.platypus import Paragraph, Image, Spacer, SimpleDocTemplate, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

guion = []

imagen = Image("800px-Cleffa.png", width=50,height=50)
img = [imagen]
titulo = ['Horario','','','','','','','']
cab = ['', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
actM = ['Mañana', 'Cole', 'Correr', '-', '-', '-', 'Estudiar', 'Trabajar']
actT = ['Tarde', 'Trabajar', 'Clases', 'Clases', 'Trabajar', 'Trabajar', 'Leer']
actN = ['Noche', '-', 'Trabajar', 'Trabajar', 'Trabajar', '-', '-', '-']

tabla = Table ([titulo, cab, actM, actT, actN])
tabla.setStyle([('TEXTCOLOR', (1,-4), (7,-4), colors.red),
                ('TEXTCOLOR', (0,0), (0,3), colors.blue),
                ('BACKGROUND', (1,-4), (-1,-4), colors.cyan),
                ('INNERGRID', (0,1), (-1,-1), 0.25, colors.lightgrey),
                ('LINEABOVE', (1, 1), (-1, 1), 1.5, colors.red),
                ('LINEAFTER', (0,1), (0,-1), 0.25, colors.lightgrey),
                ('LINEBEFORE', (1, 0), (1, -1), 1.5, colors.red),
                ("BOX", (0,0), (-1,-1), 1, colors.blue),
                ('SPAN', (0, 0), (-1, 0)),
                ('ALIGN', (0,0), (-1,0), 'CENTER'),
                ])


guion.append(tabla)
doc = SimpleDocTemplate("EjemploPlaypus_Tabla.pdf", pagesize=A4, showBoundary=0)
doc.build (guion)