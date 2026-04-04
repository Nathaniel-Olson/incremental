import pygame
import sys
import math
import gui
import constants
from calc import LongInt
from game import Game

game = Game()
color = constants.Color()
font = constants.Font()
font.initialize_all()

VIRTUAL_TICK_RATE = 30
TICK_RATE = 30
TICK_RATE_FACTOR = int(VIRTUAL_TICK_RATE / TICK_RATE)

dt = 1 / VIRTUAL_TICK_RATE

x = LongInt(0, 0)

v = LongInt(0, 0)
a = LongInt(0, 0)
j = LongInt(0, 0)
s = LongInt(0, 0)
c = LongInt(0, 0)
p = LongInt(1, -1)

v_c = LongInt(1, 0)
a_c = LongInt(10, 0)
j_c = LongInt(100, 0)
s_c = LongInt(1000, 0)
c_c = LongInt(10000, 0)
p_c = LongInt(100000, 0)

header_group = gui.Group((10, 10), (620, 80), color.GROUP)

textbox_a_locations = header_group.subdivide((2, 1), 10)

textbox_header1 = gui.Button(header_group, textbox_a_locations[0][0], (295, 60), color.TEXTBOX)
textbox_header2 = gui.Button(header_group, textbox_a_locations[0][1], (295, 60), color.TEXTBOX)

text_header11 = gui.Text(textbox_header1, "center", "Upgrades", font.CENTURY40, color.TEXT)
text_header21 = gui.Text(textbox_header2, "center", "Research", font.CENTURY40, color.TEXT)

upgrades_group = gui.Group((10, 100), (620, 370), color.GROUP)

upgrades_textbox_locations = upgrades_group.subdivide((1, 10), 10)
print(upgrades_textbox_locations)

upgrades_textbox_1 = gui.TextBox(upgrades_group, upgrades_textbox_locations[0][0], (600, 98), color.TEXTBOX)

upgrades_textbox_2 = gui.TextBox(upgrades_group, upgrades_textbox_locations[3][0], (600, 26), color.TEXTBOX)
upgrades_textbox_3 = gui.Button(upgrades_group, upgrades_textbox_locations[4][0], (600, 26), color.TEXTBOX)
upgrades_textbox_4 = gui.Button(upgrades_group, upgrades_textbox_locations[5][0], (600, 26), color.TEXTBOX)
upgrades_textbox_5 = gui.Button(upgrades_group, upgrades_textbox_locations[6][0], (600, 26), color.TEXTBOX)
upgrades_textbox_6 = gui.Button(upgrades_group, upgrades_textbox_locations[7][0], (600, 26), color.TEXTBOX)
upgrades_textbox_7 = gui.Button(upgrades_group, upgrades_textbox_locations[8][0], (600, 26), color.TEXTBOX)
upgrades_textbox_8 = gui.Button(upgrades_group, upgrades_textbox_locations[9][0], (600, 26), color.TEXTBOX)

text_upgrades11 = gui.Text(upgrades_textbox_1, "center", f"You have ${x}", font.CENTURY40, color.TEXT)

text_upgrades21 = gui.Text(upgrades_textbox_2, "left", f"Type",         font.CENTURY20, color.TEXT)
text_upgrades31 = gui.Text(upgrades_textbox_3, "left", f"Velocity",     font.CENTURY20, color.TEXT)
text_upgrades41 = gui.Text(upgrades_textbox_4, "left", f"Acceleration", font.CENTURY20, color.TEXT)
text_upgrades51 = gui.Text(upgrades_textbox_5, "left", f"Jerk",         font.CENTURY20, color.TEXT)
text_upgrades61 = gui.Text(upgrades_textbox_6, "left", f"Snap",         font.CENTURY20, color.TEXT)
text_upgrades71 = gui.Text(upgrades_textbox_7, "left", f"Crackle",      font.CENTURY20, color.TEXT)
text_upgrades81 = gui.Text(upgrades_textbox_8, "left", f"Pop",          font.CENTURY20, color.TEXT)

text_upgrades22 = gui.Text(upgrades_textbox_2, "center", f"Value", font.CENTURY20, color.TEXT)
text_upgrades32 = gui.Text(upgrades_textbox_3, "center", f"{v}",   font.CENTURY20, color.TEXT)
text_upgrades42 = gui.Text(upgrades_textbox_4, "center", f"{a}",   font.CENTURY20, color.TEXT)
text_upgrades52 = gui.Text(upgrades_textbox_5, "center", f"{j}",   font.CENTURY20, color.TEXT)
text_upgrades62 = gui.Text(upgrades_textbox_6, "center", f"{s}",   font.CENTURY20, color.TEXT)
text_upgrades72 = gui.Text(upgrades_textbox_7, "center", f"{c}",   font.CENTURY20, color.TEXT)
text_upgrades82 = gui.Text(upgrades_textbox_8, "center", f"{p}",   font.CENTURY20, color.TEXT)

text_upgrades23 = gui.Text(upgrades_textbox_2, "right", f"Cost", font.CENTURY20, color.TEXT)
text_upgrades33 = gui.Text(upgrades_textbox_3, "right", f"{v_c}",  font.CENTURY20, color.TEXT)
text_upgrades43 = gui.Text(upgrades_textbox_4, "right", f"{a_c}",  font.CENTURY20, color.TEXT)
text_upgrades53 = gui.Text(upgrades_textbox_5, "right", f"{j_c}",  font.CENTURY20, color.TEXT)
text_upgrades63 = gui.Text(upgrades_textbox_6, "right", f"{s_c}",  font.CENTURY20, color.TEXT)
text_upgrades73 = gui.Text(upgrades_textbox_7, "right", f"{c_c}",  font.CENTURY20, color.TEXT)
text_upgrades83 = gui.Text(upgrades_textbox_8, "right", f"{p_c}",  font.CENTURY20, color.TEXT)

# GAME LOOP
while True:
	game.read_events()

	for _ in range(TICK_RATE_FACTOR):
		c += p * dt
		s += c * dt
		j += s * dt
		a += j * dt
		v += a * dt
		x += v * dt

	for child in upgrades_group.children:
		if not isinstance(child, gui.Button):
			continue

		if child.check_point_intersect(game.mouse["pos"]) and game.mouse["1"]:
			child.color = color.TEXTBOX_LIGHT
		else:
			child.color = color.TEXTBOX

	text_upgrades11.set_string(f"You have ${x}")
	text_upgrades32.set_string(f"{v}")
	text_upgrades42.set_string(f"{a}")
	text_upgrades52.set_string(f"{j}")
	text_upgrades62.set_string(f"{s}")
	text_upgrades72.set_string(f"{c}")
	text_upgrades82.set_string(f"{p}")

	game.display.fill(color.BACKGROUND)

	header_group.render(game.display)
	upgrades_group.render(game.display)

	# SCALING AND GAME SPEED
	game.screen.blit(pygame.transform.scale(game.display, game.screen.get_size()), (0, 0))
	pygame.display.update()
	game.clock.tick(TICK_RATE)