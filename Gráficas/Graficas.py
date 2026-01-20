from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4

d = Drawing(400, 200)

# Ensure both tuples have the same number of elements (13 in this case)
datos = [
    (13.3, 8, 14.3, 25, 33.3, 37.5, 21.1, 28.6, 45.5, 38.1, 54.6, 36.0, 42.3),
    (67, 68, 81, 92, 90, 87, 82, 77, 79, 59, 69, 61, 0) # Added a 0 to reach 13 elements
]

# Ensure there are exactly 13 labels to match the data
lendaDatos = ['11/12', '12/13', '13/14', '14/15', '15/16', '16/17', '17/18', '18/19', '19/20', '20/21', '21/22', '22/23', '23/24']

graficoBarras = VerticalBarChart()

graficoBarras.x = 50
graficoBarras.y = 50
graficoBarras.height = 125
graficoBarras.width = 300
graficoBarras.data = datos
graficoBarras.valueAxis.valueMin = 0
graficoBarras.valueAxis.valueMax = 100 # Increased to 100 to fit your data (max is 92)
graficoBarras.valueAxis.valueStep = 10
graficoBarras.categoryAxis.labels.boxAnchor = 'ne'
graficoBarras.categoryAxis.labels.dx = 8
graficoBarras.categoryAxis.labels.dy = -2
graficoBarras.categoryAxis.labels.angle = 30
graficoBarras.categoryAxis.categoryNames = lendaDatos
graficoBarras.barSpacing = 1 # Reduced spacing so bars aren't too thin

d.add(graficoBarras)

doc = SimpleDocTemplate("graficos.pdf", pagesize=A4)
doc.build([d])