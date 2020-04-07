import pygame
import sys
import math

running = 1
x = y = 0
xList = []
yList = []
bgcolor = 0, 0, 0
circColourA = 0, 0, 255
circColourB = 255,127,0
gdClr = 0,255,0
bdClr = 255,0,0
tempColour = 0,255,0
baseCirc = 255,255,255
goodCirc = 1
colorTog = 1

if len(sys.argv) < 2:
	radius = 40
else:
	radius = int(sys.argv[1])

screen = pygame.display.set_mode((800, 800))

def inMain(x,y):
	distToCentre = math.sqrt((x-400)*(x-400)+(y-400)*(y-400))
	if distToCentre + radius < 401:
		return 1
	else:
		return 0

def circClash(x,y,xList,yList):
	for i in range(len(xList)):
		dist = math.sqrt((x-xList[i])*(x-xList[i])+(y-yList[i])*(y-yList[i]))
		if dist < radius * 2:
			return 1
	return 0
		
pygame.font.init()
		
while running:
	event = pygame.event.poll()
	goodCirc = 0
	screen.fill(bgcolor)

	font = pygame.font.Font(None, 24)
	
	text1 = font.render("You           Devil", 1, (255, 255, 255))
	textpos1 = text1.get_rect()
	background1 = pygame.Surface(screen.get_size())
	textpos1.centerx = 90
	textpos1.centery = 15
	background1.blit(text1, textpos1)
	screen.blit(background1, (0, 0))

	pygame.draw.circle(screen, baseCirc, (400,400), 400, 0)
	if colorTog == 1:
		pygame.draw.circle(screen, circColourA, (12,12), 12, 0)
		pygame.draw.circle(screen, circColourB, (90,12), 6, 0)
	else:
		pygame.draw.circle(screen, circColourA, (12,12), 6, 0)
		pygame.draw.circle(screen, circColourB, (90,12), 12, 0)

	if event.type == pygame.QUIT:
		running = 0
	elif event.type == pygame.MOUSEMOTION:
		x, y = event.pos

	# draw red circle
	pygame.draw.circle(screen, bdClr, (x,y), radius, 0)
	if inMain(x,y) == 1 and circClash(x,y,xList,yList) == 0: # draw green if good
		pygame.draw.circle(screen, gdClr, (x,y), radius, 0)
		goodCirc = 1

	if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and goodCirc == 1:
		#print "You pressed the left mouse button at (%d, %d)" % event.pos
		# add x,y pair to end of array
		xList.append(x)
		yList.append(y)
	
	# draw many circles
	colorTog = 1
	for i in range(len(xList)):
		if colorTog == 1:
			pygame.draw.circle(screen, circColourA, (xList[i], yList[i]), radius, 0)
		else:
			pygame.draw.circle(screen, circColourB, (xList[i], yList[i]), radius, 0)
		colorTog = colorTog * -1
	
	pygame.display.flip()
