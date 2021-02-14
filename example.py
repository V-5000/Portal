import portal,time

window = portal.display.size(600,400)
surf = portal.surface.create(portal.display.getwidth(window),portal.display.getheight(window))
portal.surface.pack(surf)

x=10

while True:
	f=time.time()
	portal.draw.fill(surf)

	portal.draw.line(surf,x,10,100,100,"#fff")

	x+=1

	portal.display.update(window)
	portal.surface.forgot(surf)
	
	#keep this to avoid frame drops
	time.sleep(0.0)
	l=time.time()
	print(60/(l-f))
