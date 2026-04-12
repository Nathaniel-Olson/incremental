import pygame
import sys
import math
import gui
import constants
from calc import LongInt, UpgradeableParameter
from game import Game

game = Game()
color = constants.Color()
font = constants.Font()
font.initialize_all()

VIRTUAL_TICK_RATE = 30
TICK_RATE = 30
TICK_RATE_FACTOR = int(VIRTUAL_TICK_RATE / TICK_RATE)

dt = 1 / VIRTUAL_TICK_RATE

x = LongInt(1, 0)

v_i = LongInt(0, 0)
a_i = LongInt(0, 0)
j_i = LongInt(0, 0)
s_i = LongInt(0, 0)
c_i = LongInt(0, 0)
p_i = LongInt(0, 0)

v_c = LongInt(1, 0)
a_c = LongInt(10, 0)
j_c = LongInt(100, 0)
s_c = LongInt(1000, 0)
c_c = LongInt(10000, 0)
p_c = LongInt(100000, 0)

v_m = LongInt(1, 0)
a_m = LongInt(1, 0)
j_m = LongInt(1, 0)
s_m = LongInt(1, 0)
c_m = LongInt(1, 0)
p_m = LongInt(1, 0)

upgrade_factor = LongInt(1, 0)

velocity     = UpgradeableParameter(v_i, lambda i: i + upgrade_factor, v_c, lambda i: i * 2, v_m, lambda i: i)
acceleration = UpgradeableParameter(a_i, lambda i: i + upgrade_factor, a_c, lambda i: i * 2, a_m, lambda i: i)
jerk         = UpgradeableParameter(j_i, lambda i: i + upgrade_factor, j_c, lambda i: i * 2, j_m, lambda i: i)
snap         = UpgradeableParameter(s_i, lambda i: i + upgrade_factor, s_c, lambda i: i * 2, s_m, lambda i: i)
crackle      = UpgradeableParameter(c_i, lambda i: i + upgrade_factor, c_c, lambda i: i * 2, c_m, lambda i: i)
pop          = UpgradeableParameter(p_i, lambda i: i + upgrade_factor, p_c, lambda i: i * 2, p_m, lambda i: i)

### CREATING GROUPS, TEXTBOXES, AND TEXT
header_group = gui.Group((10, 10), (620, 80), color.GROUP)

textbox_a_locations = header_group.subdivide((2, 1), 10)

textbox_header1 = gui.Button(header_group, textbox_a_locations[0][0], (295, 60), color.TEXTBOX)
textbox_header2 = gui.Button(header_group, textbox_a_locations[0][1], (295, 60), color.GROUP)

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

upgrades_textbox_3.add_upgradeable_dependant(velocity)
upgrades_textbox_4.add_upgradeable_dependant(acceleration)
upgrades_textbox_5.add_upgradeable_dependant(jerk)
upgrades_textbox_6.add_upgradeable_dependant(snap)
upgrades_textbox_7.add_upgradeable_dependant(crackle)
upgrades_textbox_8.add_upgradeable_dependant(pop)

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

### GAME LOOP
while True:
	game.read_events()

	for _ in range(TICK_RATE_FACTOR):
		crackle.value += pop.value * dt
		snap.value += crackle.value * dt
		jerk.value += snap.value * dt
		acceleration.value += jerk.value * dt
		velocity.value += acceleration.value * dt
		x += velocity.value * dt

	for child in upgrades_group.children:
		if not isinstance(child, gui.Button):
			continue

		if child.check_point_intersect(game.mouse["pos"]) and game.mouse["1"]:
			child.color = color.TEXTBOX_LIGHT
			if x >= child.upgradeable_parameter.cost:
				x -= child.upgradeable_parameter.cost
				child.upgradeable_parameter.purchase(x)

		else:
			child.color = color.TEXTBOX

	text_upgrades11.set_string(f"${x}")
	

	text_upgrades32.set_string(f"{velocity.value}")
	text_upgrades42.set_string(f"{acceleration.value}")
	text_upgrades52.set_string(f"{jerk.value}")
	text_upgrades62.set_string(f"{snap.value}")
	text_upgrades72.set_string(f"{crackle.value}")
	text_upgrades82.set_string(f"{pop.value}")

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