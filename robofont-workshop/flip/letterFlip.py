# get the current font
font = CurrentFont()


for glyph in font.glyphs:
    width = glyph.width
    
    for contour in glyph.contours:
        for point in contour.points:
            point.x = width - point.x
    glyph.update()

print("done")