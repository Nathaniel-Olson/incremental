import pygame
import sys
import math
import gui
import constants
from calc import LongInt, UpgradeableParameter
from game import Game

# initialize game, color and font modules.
game = Game()

color = constants.Color()
color.set_black_colorwave()

font = constants.Font()
font.initialize_all()

VIRTUAL_TICK_RATE = 30
TICK_RATE = 30
TICK_RATE_FACTOR = int(VIRTUAL_TICK_RATE / TICK_RATE)

dt = 1 / VIRTUAL_TICK_RATE

# create game variables
x = LongInt(1, 0)

v_i = LongInt(1, 0)
a_i = LongInt(1, 0)
j_i = LongInt(1, 0)
s_i = LongInt(1, 0)
c_i = LongInt(1, 0)
p_i = LongInt(1, 0)

v_c = LongInt(1, 0)
a_c = LongInt(5, 1)
j_c = LongInt(1, 3)
s_c = LongInt(5, 4)
c_c = LongInt(1, 6)
p_c = LongInt(5, 7)

v_m = LongInt(0, 0)
a_m = LongInt(0, 0)
j_m = LongInt(0, 0)
s_m = LongInt(0, 0)
c_m = LongInt(0, 0)
p_m = LongInt(0, 0)

velocity     = UpgradeableParameter(v_i, lambda i: i, v_c, lambda i: i * 2, v_m, lambda i: i + LongInt(1, 0))
acceleration = UpgradeableParameter(a_i, lambda i: i, a_c, lambda i: i * 2, a_m, lambda i: i + LongInt(1/2, 0))
jerk         = UpgradeableParameter(j_i, lambda i: i, j_c, lambda i: i * 2, j_m, lambda i: i + LongInt(1/6, 0))
snap         = UpgradeableParameter(s_i, lambda i: i, s_c, lambda i: i * 2, s_m, lambda i: i + LongInt(1/24, 0))
crackle      = UpgradeableParameter(c_i, lambda i: i, c_c, lambda i: i * 2, c_m, lambda i: i + LongInt(1/120, 0))
pop          = UpgradeableParameter(p_i, lambda i: i, p_c, lambda i: i * 2, p_m, lambda i: i + LongInt(1/720, 0))

### CREATING GROUPS, TEXTBOXES, AND TEXT
header_group = gui.Group((10, 10), (620, 80), color.GROUP)

textbox_a_locations = header_group.subdivide((2, 1), 10)

textbox_header1 = gui.Button(header_group, textbox_a_locations[0][0], (295, 60), color.TEXTBOX)
textbox_header2 = gui.Button(header_group, textbox_a_locations[0][1], (295, 60), color.GROUP)

text_header11 = gui.Text(textbox_header1, "center", "Upgrades", font.CENTURY40, color.TEXT)
text_header21 = gui.Text(textbox_header2, "center", "Research", font.CENTURY40, color.TEXT)

upgrades_group = gui.Group((10, 100), (620, 370), color.GROUP)

upgrades_textbox_locations = upgrades_group.subdivide((1, 10), 10)

upgrades_textbox_1 = gui.TextBox(upgrades_group, upgrades_textbox_locations[0][0], (600, 98), color.TEXTBOX)

upgrades_textbox_2 = gui.TextBox(upgrades_group, upgrades_textbox_locations[3][0], (600, 26), color.TEXTBOX)
upgrades_textbox_3 = gui.Button(upgrades_group, upgrades_textbox_locations[4][0], (600, 26), color.TEXTBOX)
upgrades_textbox_4 = gui.Button(upgrades_group, upgrades_textbox_locations[5][0], (600, 26), color.TEXTBOX)
upgrades_textbox_5 = gui.Button(upgrades_group, upgrades_textbox_locations[6][0], (600, 26), color.TEXTBOX)
upgrades_textbox_6 = gui.Button(upgrades_group, upgrades_textbox_locations[7][0], (600, 26), color.TEXTBOX)
upgrades_textbox_7 = gui.Button(upgrades_group, upgrades_textbox_locations[8][0], (600, 26), color.TEXTBOX)
upgrades_textbox_8 = gui.Button(upgrades_group, upgrades_textbox_locations[9][0], (600, 26), color.TEXTBOX)

text_upgrades11 = gui.Text(upgrades_textbox_1, "center", f"${x}", font.CENTURY40, color.TEXT)

text_upgrades21 = gui.Text(upgrades_textbox_2, "left", f"Type",         font.CENTURY20, color.TEXT)
text_upgrades31 = gui.Text(upgrades_textbox_3, "left", f"Velocity",     font.CENTURY20, color.TEXT)
text_upgrades41 = gui.Text(upgrades_textbox_4, "left", f"Acceleration", font.CENTURY20, color.TEXT)
text_upgrades51 = gui.Text(upgrades_textbox_5, "left", f"Jerk",         font.CENTURY20, color.TEXT)
text_upgrades61 = gui.Text(upgrades_textbox_6, "left", f"Snap",         font.CENTURY20, color.TEXT)
text_upgrades71 = gui.Text(upgrades_textbox_7, "left", f"Crackle",      font.CENTURY20, color.TEXT)
text_upgrades81 = gui.Text(upgrades_textbox_8, "left", f"Pop",          font.CENTURY20, color.TEXT)

text_upgrades22 = gui.Text(upgrades_textbox_2, "center", f"Value",                  font.CENTURY20, color.TEXT)
text_upgrades32 = gui.Text(upgrades_textbox_3, "center", f"{velocity.value}",       font.CENTURY20, color.TEXT)
text_upgrades42 = gui.Text(upgrades_textbox_4, "center", f"{acceleration.value}",   font.CENTURY20, color.TEXT)
text_upgrades52 = gui.Text(upgrades_textbox_5, "center", f"{jerk.value}",           font.CENTURY20, color.TEXT)
text_upgrades62 = gui.Text(upgrades_textbox_6, "center", f"{snap.value}",           font.CENTURY20, color.TEXT)
text_upgrades72 = gui.Text(upgrades_textbox_7, "center", f"{crackle.value}",        font.CENTURY20, color.TEXT)
text_upgrades82 = gui.Text(upgrades_textbox_8, "center", f"{pop.value}",            font.CENTURY20, color.TEXT)

text_upgrades23 = gui.Text(upgrades_textbox_2, "right", f"Cost",   			     font.CENTURY20, color.TEXT)
text_upgrades33 = gui.Text(upgrades_textbox_3, "right", f"{velocity.cost}",      font.CENTURY20, color.TEXT)
text_upgrades43 = gui.Text(upgrades_textbox_4, "right", f"{acceleration.cost}",  font.CENTURY20, color.TEXT)
text_upgrades53 = gui.Text(upgrades_textbox_5, "right", f"{jerk.cost}",          font.CENTURY20, color.TEXT)
text_upgrades63 = gui.Text(upgrades_textbox_6, "right", f"{snap.cost}",          font.CENTURY20, color.TEXT)
text_upgrades73 = gui.Text(upgrades_textbox_7, "right", f"{crackle.cost}",       font.CENTURY20, color.TEXT)
text_upgrades83 = gui.Text(upgrades_textbox_8, "right", f"{pop.cost}",           font.CENTURY20, color.TEXT)

param_button_pairs = [(velocity, upgrades_textbox_3),
					  (acceleration, upgrades_textbox_4),
					  (jerk, upgrades_textbox_5),
					  (snap, upgrades_textbox_6),
					  (crackle, upgrades_textbox_7),
					  (pop, upgrades_textbox_8)]

### GAME LOOP
while True:
	game.read_events()

	for _ in range(TICK_RATE_FACTOR):
		crackle.value += pop.value * pop.multiplier * dt
		snap.value += crackle.value * crackle.multiplier * dt
		jerk.value += snap.value * snap.multiplier * dt
		acceleration.value += jerk.value * jerk.multiplier * dt
		velocity.value += acceleration.value * acceleration.multiplier * dt
		x += velocity.value * velocity.multiplier * dt

	for child in upgrades_group.children:
		if not isinstance(child, gui.Button):
			continue

	for index, pair in enumerate(param_button_pairs):
		param, button = pair
		key_id = str(index + 1)

		if (button.check_point_intersect(game.mouse["pos"]) and game.mouse["1"]):
			button.color = color.TEXTBOX_LIGHT
			if not game.mouse_cooldown["1"]:
				game.mouse_cooldown["1"] = 1
				if x >= param.cost:
					x -= param.cost
					param.purchase()

		if game.key[key_id]:
			button.color = color.TEXTBOX_LIGHT
			if not game.key_cooldown[key_id]:
				game.key_cooldown[key_id] = 1
				if x >= param.cost:
					x -= param.cost
					param.purchase()

		else:
			button.color = color.TEXTBOX

	text_upgrades11.set_string(f"${x}")
	
	text_upgrades32.set_string(f"{velocity.value * velocity.multiplier}")
	text_upgrades42.set_string(f"{acceleration.value * acceleration.multiplier}")
	text_upgrades52.set_string(f"{jerk.value * jerk.multiplier}")
	text_upgrades62.set_string(f"{snap.value * snap.multiplier}")
	text_upgrades72.set_string(f"{crackle.value * crackle.multiplier}")
	text_upgrades82.set_string(f"{pop.value * pop.multiplier}")

	text_upgrades33.set_string(f"{velocity.cost}")
	text_upgrades43.set_string(f"{acceleration.cost}")
	text_upgrades53.set_string(f"{jerk.cost}")
	text_upgrades63.set_string(f"{snap.cost}")
	text_upgrades73.set_string(f"{crackle.cost}")
	text_upgrades83.set_string(f"{pop.cost}")

	game.display.fill(color.BACKGROUND)

	header_group.render(game.display)
	upgrades_group.render(game.display)

	# SCALING AND GAME SPEED
	game.screen.blit(pygame.transform.scale(game.display, game.screen.get_size()), (0, 0))
	pygame.display.update()
	game.clock.tick(TICK_RATE)