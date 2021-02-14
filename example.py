import portal,time

window = portal.display.size(600,400)
surf = portal.surface.create(portal.display.getwidth(window),portal.display.getheight(window))

while True:
	f=time.time()
	portal.draw.fill(surf)
	portal.draw.line(surf,10,10,100,100,"#fff")
	portal.surface.pack(surf)

	portal.surface.forgot(surf)
	portal.display.update(window)

	#keep this to avoid frame drops
	time.sleep(0.0)
	l=time.time()
	print(60/(l-f))
