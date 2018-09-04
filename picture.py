"""
picture.py
Author: Nick Lee
Credit: https://html-color-codes.info/ for HTML color codes

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
red = Color(0xff0000, 0.7)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
brown = Color(0xB45F04, 1.0)
tree = Color(0x04B404, 1.0)
sky = Color(0x2EFEF7, 1.0)

thinline = LineStyle (1,black)


background = RectangleAsset(1500, 600, thinline, sky)
hill = EllipseAsset(600, 100, thinline, tree)
treeleaves = CircleAsset(50, thinline, tree)
treetrunk = RectangleAsset(30, 100, thinline, brown)



Sprite(background, (-1, -1))
Sprite(hill, (-300, 400))
Sprite(treetrunk, (200, 350))
Sprite(treeleaves, (165, 300))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
