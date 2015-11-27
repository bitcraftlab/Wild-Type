
import math
from fontTools.misc.transform import Identity

size(1500, 1500)

f = OpenFont("Roboto-Black.ufo", False)
glyph = f["A"]


m = Identity
rotation = 2

# iterate over all contours
for contour in glyph:

    # move to the starting point
    p = contour.points[0]

    # iterate over all the points
    for point in contour.points:

        # rotate each point a little bit more
        m = m.rotate(math.radians(rotation))
        point.transform(m)

# set stroke size
strokeWidth(40)

# sample a lot of random points on the plane
for i in range(5000):

    # random x position
    x = random() * width()

    # random y position
    y = random() * height()

    # random shade of green
    alpha = 0.2 + random() * 0.3 
    beta = 0.1 + random() * 0.5
    stroke(0, beta, 0, alpha)

    if glyph.pointInside((x, y)):
        oval(x, y, 40, 40)
        

