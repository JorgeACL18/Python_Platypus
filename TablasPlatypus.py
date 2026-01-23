from reportlab.lib import colors
from reportlab.platypus import Paragraph, Image, Spacer, SimpleDocTemplate, Table
from reportlab.lib.pagesizes import A4

guion = []

titulo = ['Horario','','','','','','','']
cab = ['', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
actM = ['Mañana', 'Cole', 'Correr', '-', '-', '-', 'Estudiar', 'Trabajar']
actT = ['Tarde', 'Trabajar', 'Clases', 'Clases', 'Trabajar', 'Trabajar', 'Leer', '-']
actN = ['Noche', '-', 'Trabajar', 'Trabajar', 'Trabajar', '-', '-', '-']

tabla = Table ([titulo, cab, actM, actT, actN])
tabla.setStyle([('TEXTCOLOR', (1,1), (7,1), colors.red),
                ('TEXTCOLOR', (0,0), (0,3), colors.blue),
                ('BACKGROUND', (1,1), (7,1), colors.cyan),
                ('INNERGRID', (0,0), (7,4), 1, colors.lightgrey),
                ('LINEABOVE', (1,2), (7, 2), 1.5, colors.red),
                ('LINEAFTER', (0,0), (0,0), 1.5, colors.violet),
                ('LINEBEFORE', (1,2), (1,4), 1.5, colors.red),
                ("BOX", (0,0), (7,4), 10, colors.blue),
                ('SPAN', (0, 0), (7, 0)),
                ('ALIGN', (0,0), (0,0), 'CENTER'),
                ('SPAN', (1, 1), (-2, 1)),
                ('ALIGN', (1, 1), (1, 1), 'CENTER'),
                ])

esp = Spacer(100, 100)
guion.append(esp)
guion.append(tabla)

doc = SimpleDocTemplate("EjemploPlaypus_Tabla.pdf", pagesize=A4, showBoundary=0)
doc.build (guion)