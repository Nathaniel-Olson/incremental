import pygame
import sys
import math
import gui
from constants import *
from calc import LongInt

class Game:
	def __init__(self, 
				 screen_size: tuple[int] = (640, 480),
				 display_size: tuple[int] = (640, 480)):

		pygame.init()

		self.screen = pygame.display.set_mode(screen_size)
		self.display = pygame.Surface(display_size)
		self.clock = pygame.time.Clock()

		self.key = {"1":False,"2":False,"3":False,"4":False,"5":False,
					"6":False,"7":False,"8":False,"9":False,"space":False}

		self.left_click = False
		self.left_click_cooldown = False

		self.right_click = False
		self.mouse_pos = (0, 0)

	def handle_io(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					self.key["1"] = True
				if event.key == pygame.K_2:
					self.key["2"] = True
				if event.key == pygame.K_3:
					self.key["3"] = True
				if event.key == pygame.K_4:
					self.key["4"] = True
				if event.key == pygame.K_5:
					self.key["5"] = True
				if event.key == pygame.K_6:
					self.key["6"] = True
				if event.key == pygame.K_7:
					self.key["7"] = True
				if event.key == pygame.K_8:
					self.key["8"] = True
				if event.key == pygame.K_9:
					self.key["9"] = True
				if event.key == pygame.K_SPACE:
					self.key["space"] = True

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_1:
					self.key["1"] = False
				if event.key == pygame.K_2:
					self.key["2"] = False
				if event.key == pygame.K_3:
					self.key["3"] = False
				if event.key == pygame.K_4:
					self.key["4"] = False
				if event.key == pygame.K_5:
					self.key["5"] = False
				if event.key == pygame.K_6:
					self.key["6"] = False
				if event.key == pygame.K_7:
					self.key["7"] = False
				if event.key == pygame.K_8:
					self.key["8"] = False
				if event.key == pygame.K_9:
					self.key["9"] = False
				if event.key == pygame.K_SPACE:
					self.key["space"] = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				self.left_click = True

			if event.type == pygame.MOUSEBUTTONUP:
				self.left_click = False

			if event.type == pygame.MOUSEMOTION:
				self.mouse_pos = pygame.mouse.get_pos()

def logistic_function(q,q1,q2,c1,c2,c3,dt) -> LongInt:
	dq = (c1 / c2) * q * (c3 - (q / c2)) * dt
	q += dq
	dx = q1 * q2 * q * dt
	return dx

game = Game()
c2_upgrade_button = gui.Button(width = 200, height = 40, location = (40, 250), color = DUSK_BLUE)
c1_upgrade_button = gui.Button(width = 200, height = 40, location = (40, 200), color = DUSK_BLUE)
c3_upgrade_button = gui.Button(width = 200, height = 40, location = (40, 300), color = DUSK_BLUE)
q1_upgrade_button = gui.Button(width = 200, height = 40, location = (40, 350), color = DUSK_BLUE)
q2_upgrade_button = gui.Button(width = 200, height = 40, location = (40, 400), color = DUSK_BLUE)

c1_upgrade_button.show()
c2_upgrade_button.show()
c3_upgrade_button.show()
q1_upgrade_button.show()
q2_upgrade_button.show()

VIRTUAL_TICK_RATE = 30
TICK_RATE = 30
TICK_RATE_FACTOR = int(VIRTUAL_TICK_RATE / TICK_RATE)

dt = 0.01

c1 = LongInt(1, 0)
c2 = LongInt(1, 0)
c3 = LongInt(1, 0)
q1 = LongInt(1, 0)
q2 = LongInt(1, 0)
q = LongInt(1, 0)

c1_cost = LongInt(1, 0)
c2_cost = LongInt(1, 0)
c3_cost = LongInt(1, 0)
q1_cost = LongInt(1, 0)
q2_cost = LongInt(1, 0)

x = LongInt(0, 0)

# GAME LOOP
while True:
	game.handle_io()

	for _ in range(TICK_RATE_FACTOR):
		dx = logistic_function(q, q1, q2, c1, c2, c3, dt)
		x += dx

	if x >= c1_cost:
		c1_upgrade_button.color = DUSTY_DENIM
	else:
		c1_upgrade_button.color = DUSK_BLUE

	if x >= c2_cost:
		c2_upgrade_button.color = DUSTY_DENIM
	else:
		c2_upgrade_button.color = DUSK_BLUE

	if x >= c3_cost:
		c3_upgrade_button.color = DUSTY_DENIM
	else:
		c3_upgrade_button.color = DUSK_BLUE

	if x >= q1_cost:
		q1_upgrade_button.color = DUSTY_DENIM
	else:
		q1_upgrade_button.color = DUSK_BLUE

	if x >= q2_cost:
		q2_upgrade_button.color = DUSTY_DENIM
	else:
		q2_upgrade_button.color = DUSK_BLUE

	if game.left_click and not game.left_click_cooldown:
		if c1_upgrade_button.check_point_intersect(game.mouse_pos) and x >= c1_cost:
			x -= c1_cost
			c1 *= 1.07
			c1_cost *= 1.25

		if c2_upgrade_button.check_point_intersect(game.mouse_pos) and x >= c2_cost:
			x -= c2_cost
			c2 *= 2
			c2_cost *= 4

		if c3_upgrade_button.check_point_intersect(game.mouse_pos) and x >= c3_cost:
			x -= c3_cost
			c3 *= 2
			c3_cost *= 500

		if q1_upgrade_button.check_point_intersect(game.mouse_pos) and x >= q1_cost:
			x -= q1_cost
			q1 *= 1.07
			q1_cost *= 1.25

		if q2_upgrade_button.check_point_intersect(game.mouse_pos) and x >= q2_cost:
			x -= q2_cost
			q2 *= 2
			q2_cost *= 50

		game.left_click_cooldown = True


	if game.left_click_cooldown and not game.left_click:

		game.left_click_cooldown = False

	q_surface = CENTURY_40.render(f"= {q}", True, ALABASTER_GREY)
	x_surface = CENTURY_40.render(f"= {x}", True, ALABASTER_GREY)

	q2_surface = CENTURY_40.render("Q", True, ALABASTER_GREY)
	x2_surface = SYMBOL_40.render("r", True, ALABASTER_GREY)
	
	game.display.fill(INK_BLACK)

	game.display.blit(x_surface, (90, 100))
	game.display.blit(q_surface, (90, 40))

	game.display.blit(x2_surface, (50, 100))
	game.display.blit(q2_surface, (40, 40))

	c1_upgrade_button.text(f"C1", CENTURY_20, ALABASTER_GREY, f"${c1_cost}", CENTURY_20, "split")
	c2_upgrade_button.text(f"C2", CENTURY_20, ALABASTER_GREY, f"${c2_cost}", CENTURY_20, "split")
	c3_upgrade_button.text(f"C3", CENTURY_20, ALABASTER_GREY, f"${c3_cost}", CENTURY_20, "split")
	q1_upgrade_button.text(f"Q1", CENTURY_20, ALABASTER_GREY, f"${q1_cost}", CENTURY_20, "split")
	q2_upgrade_button.text(f"Q2", CENTURY_20, ALABASTER_GREY, f"${q2_cost}", CENTURY_20, "split")

	c1_upgrade_button.render(surface = game.display)
	c2_upgrade_button.render(surface = game.display)
	c3_upgrade_button.render(surface = game.display)
	q1_upgrade_button.render(surface = game.display)
	q2_upgrade_button.render(surface = game.display)

	# SCALING AND GAME SPEED
	game.screen.blit(pygame.transform.scale(game.display, game.screen.get_size()), (0, 0))
	pygame.display.update()
	game.clock.tick(TICK_RATE)