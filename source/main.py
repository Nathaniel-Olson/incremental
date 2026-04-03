import pygame
import sys
import math
import gui
from constants import Color, Font
from calc import LongInt
from game import Game

def logistic_function(q,q1,q2,c1,c2,c3,dt) -> LongInt:
	dq = (c1 / c2) * q * (c3 - (q / c2)) * dt
	q += dq
	dx = q1 * q2 * q * dt
	return dx

game = Game()
color = Color()
font = Font()
font.initialize_all()

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

group_a = gui.Group((10, 10), (620, 225), color.GROUP)

textbox_a_locations = group_a.subdivide((2, 3), 10)

textbox_a1 = gui.TextBox(group_a, textbox_a_locations[0][0], (295, 60), color.TEXTBOX)
textbox_a2 = gui.TextBox(group_a, textbox_a_locations[0][1], (295, 60), color.TEXTBOX)

text_a11 = gui.Text(textbox_a1, "left", "X =", font.CENTURY40, color.TEXT)
text_a21 = gui.Text(textbox_a2, "left", "Q =", font.CENTURY40, color.TEXT)
text_a12 = gui.Text(textbox_a1, "right", str(x), font.CENTURY40, color.TEXT)
text_a22 = gui.Text(textbox_a2, "right", str(q), font.CENTURY40, color.TEXT)


group_b = gui.Group((10, 245), (620, 225), color.GROUP)

textbox_b_locations = group_b.subdivide((2,3), 10)

textbox_b1 = gui.Button(group_b, textbox_b_locations[0][0], (295, 60), color.TEXTBOX)
textbox_b2 = gui.Button(group_b, textbox_b_locations[1][0], (295, 60), color.TEXTBOX)
textbox_b3 = gui.Button(group_b, textbox_b_locations[2][0], (295, 60), color.TEXTBOX)
textbox_b4 = gui.Button(group_b, textbox_b_locations[0][1], (295, 60), color.TEXTBOX)
textbox_b5 = gui.Button(group_b, textbox_b_locations[1][1], (295, 60), color.TEXTBOX)

text_b11 = gui.Text(textbox_b1, "left", "C1", font.CENTURY40, color.TEXT)
text_b21 = gui.Text(textbox_b2, "left", "C2", font.CENTURY40, color.TEXT)
text_b31 = gui.Text(textbox_b3, "left", "C3", font.CENTURY40, color.TEXT)
text_b41 = gui.Text(textbox_b4, "left", "Q1", font.CENTURY40, color.TEXT)
text_b51 = gui.Text(textbox_b5, "left", "Q2", font.CENTURY40, color.TEXT)

text_b12 = gui.Text(textbox_b1, "right", str(c1_cost), font.CENTURY40, color.TEXT)
text_b22 = gui.Text(textbox_b2, "right", str(c2_cost), font.CENTURY40, color.TEXT)
text_b32 = gui.Text(textbox_b3, "right", str(c3_cost), font.CENTURY40, color.TEXT)
text_b42 = gui.Text(textbox_b4, "right", str(q1_cost), font.CENTURY40, color.TEXT)
text_b52 = gui.Text(textbox_b5, "right", str(q2_cost), font.CENTURY40, color.TEXT)

# GAME LOOP
while True:
	game.read_events()

	for _ in range(TICK_RATE_FACTOR):
		dx = logistic_function(q, q1, q2, c1, c2, c3, dt)
		x += dx

	for child in group_b.children:
		if not isinstance(child, gui.Button):
			continue

		if child.check_point_intersect(game.mouse["pos"]) and game.mouse["1"]:
			child.color = color.TEXTBOX_LIGHT
		else:
			child.color = color.TEXTBOX

	game.display.fill(color.BACKGROUND)

	group_a.render(game.display)
	group_b.render(game.display)

	# SCALING AND GAME SPEED
	game.screen.blit(pygame.transform.scale(game.display, game.screen.get_size()), (0, 0))
	pygame.display.update()
	game.clock.tick(TICK_RATE)