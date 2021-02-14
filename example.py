import portal

window = portal.display.size()
x = 10

surf = portal.surface.create(100,100)

while True:
	portal.draw.rect(surf,0,0,300,250)
	portal.draw.line(surf,x,10,100,100)
	portal.surface.pack(surf)
	x += 1

	portal.display.update(window)
