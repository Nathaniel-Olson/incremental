import pygame

# for font in pygame.font.get_fonts():
# 	if font[0] == 'c':
# 		print(font)

fonts = [
"cambria",
"cambriamath",
"constantia",
"javanesetext",
"timesnewroman",
"bookantiqua",
"baskervilleoldface",
"bell",
"calisto",
"centuryschoolbook",
"centaur",
"century",
"engravers",
"felixtitling",
"garamond",
"lucidafax",
"modernno20",
"perpetua",
"perpetuatitling"
]

pygame.init()

screen = pygame.display.set_mode((1600, 980))

clock = pygame.time.Clock()

iterator = 1

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	font0 = pygame.font.SysFont(fonts[0], 40)
	font1 = pygame.font.SysFont(fonts[1], 40)
	font2 = pygame.font.SysFont(fonts[2], 40)
	font3 = pygame.font.SysFont(fonts[3], 40)
	font4 = pygame.font.SysFont(fonts[4], 40)
	font5 = pygame.font.SysFont(fonts[5], 40)
	font6 = pygame.font.SysFont(fonts[6], 40)
	font7 = pygame.font.SysFont(fonts[7], 40)
	font8 = pygame.font.SysFont(fonts[8], 40)
	font9 = pygame.font.SysFont(fonts[9], 40)
	font10 = pygame.font.SysFont(fonts[10], 40)
	font11 = pygame.font.SysFont(fonts[11], 40)
	font12 = pygame.font.SysFont(fonts[12], 40)
	font13 = pygame.font.SysFont(fonts[13], 40)
	font14 = pygame.font.SysFont(fonts[14], 40)
	font15 = pygame.font.SysFont(fonts[15], 40)
	font16 = pygame.font.SysFont(fonts[16], 40)
	font17 = pygame.font.SysFont(fonts[17], 40)
	font18 = pygame.font.SysFont(fonts[17], 40)





	text = "Sphinx of Black Quartz, Judge my Vow. 1.2345e6789"
	surf0 = font0.render(text, False, (255,255,255))
	surf1 = font1.render(text, False, (255,255,255))
	surf2 = font2.render(text, False, (255,255,255))
	surf3 = font3.render(text, False, (255,255,255))
	surf4 = font4.render(text, False, (255,255,255))
	surf5 = font5.render(text, False, (255,255,255))
	surf6 = font6.render(text, False, (255,255,255))
	surf7 = font7.render(text, False, (255,255,255))
	surf8 = font8.render(text, False, (255,255,255))
	surf9 = font9.render(text, False, (255,255,255))
	surf10 = font10.render(text, False, (255,255,255))
	surf11 = font11.render(text, False, (255,255,255))
	surf12 = font12.render(text, False, (255,255,255))
	surf13 = font13.render(text, False, (255,255,255))
	surf14 = font14.render(text, False, (255,255,255))
	surf15 = font15.render(text, False, (255,255,255))
	surf16 = font16.render(text, False, (255,255,255))
	surf17 = font17.render(text, False, (255,255,255))
	surf18 = font18.render(text, False, (255,255,255))

	screen.fill((0,0,0))

	screen.blit(surf0, (20, 20))
	screen.blit(surf1, (20, 70))
	screen.blit(surf2, (20, 120))
	screen.blit(surf3, (20, 170))
	screen.blit(surf4, (20, 220))
	screen.blit(surf5, (20, 270))
	screen.blit(surf6, (20, 320))
	screen.blit(surf7, (20, 370))
	screen.blit(surf8, (20, 420))
	screen.blit(surf9, (20, 470))
	screen.blit(surf10, (20, 520))
	screen.blit(surf11, (20, 570))
	screen.blit(surf12, (20, 620))
	screen.blit(surf13, (20, 670))
	screen.blit(surf14, (20, 720))
	screen.blit(surf15, (20, 770))
	screen.blit(surf16, (20, 820))
	screen.blit(surf17, (20, 870))
	screen.blit(surf18, (20, 920))

	pygame.display.update()
	clock.tick(1)