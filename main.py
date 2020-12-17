from cmu_graphics import *

p = Polygon(100, 300, 200, 100, 300, 300, fill='green')
r = Rect(175, 300, 50, 50, fill='brown')
l1 = Line(100, 300, 200, 100, fill = "black", lineWidth=2)
l2 = Line(200, 100, 300, 300, fill = "black", lineWidth=2)
l3 = Line(100, 300, 175, 300, fill = "black", lineWidth=2)
l4 = Line(175, 300, 175, 350, fill = "black", lineWidth=2)
l5 = Line(175, 350, 225, 350, fill = "black", lineWidth=2)
l6 = Line(225, 350, 225, 300, fill = "black", lineWidth=2)
l7 = Line(225, 300, 300, 300, fill = "black", lineWidth=2)
treeBorder = Group(l1, l2, l3, l4, l5, l6, l7)
tree = Group(p, r, treeBorder)
def onMouseMove(x_cor, y_cor):
    if(tree.hits(x_cor, y_cor)):
        treeBorder.fill = "gold"
    else:
        treeBorder.fill = "black"


cmu_graphics.loop()
