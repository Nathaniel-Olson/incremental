import pygame
import sys

class Game:
	def __init__(self, 
				 screen_size = (640, 480),
				 display_size = (640, 480)) -> None:

		pygame.init()

		self.screen = pygame.display.set_mode(screen_size)
		self.display = pygame.Surface(display_size)
		self.clock = pygame.time.Clock()

		self.key = {
		"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "0": 0,
		"q": 0, "w": 0, "e": 0, "r": 0, "t": 0, "y": 0, "u": 0, "i": 0, "o": 0, "p": 0,
		"a": 0, "s": 0, "d": 0, "f": 0, "g": 0, "h": 0, "j": 0, "k": 0, "l": 0,
		"z": 0, "x": 0, "c": 0, "v": 0, "b": 0, "n": 0, "m": 0,
		"space": 0
		}

		self.key_map = {
			pygame.K_1: "1", pygame.K_2: "2", pygame.K_3: "3", pygame.K_4: "4", pygame.K_5: "5", pygame.K_6: "6", pygame.K_7: "7", pygame.K_8: "8", pygame.K_9: "9", pygame.K_0: "0",
			pygame.K_q: "q", pygame.K_w: "w", pygame.K_e: "e", pygame.K_r: "r", pygame.K_t: "t", pygame.K_y: "y", pygame.K_u: "u", pygame.K_i: "i", pygame.K_o: "o", pygame.K_p: "p",
			pygame.K_a: "a", pygame.K_s: "s", pygame.K_d: "d", pygame.K_f: "f", pygame.K_g: "g", pygame.K_h: "h", pygame.K_j: "j", pygame.K_k: "k", pygame.K_l: "l",
			pygame.K_z: "z", pygame.K_x: "x", pygame.K_c: "c", pygame.K_v: "v", pygame.K_b: "b", pygame.K_n: "n", pygame.K_m: "m",
			pygame.K_SPACE: "space",
		}

		self.mouse = {
		"1": 0,
		"2": 0,
		"3": 0,
		"4": 0,
		"5": 0,
		"pos": (0,0)
		}

		self.mouse_map = {
		1 : "1",
		2 : "2",
		3 : "3",
		4 : "4",
		5 : "5"
		}

	def read_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == in self.key_map:
					self.key[self.key_map[event.key]] = 1

			if event.type == pygame.KEYUP:
				if event.key == in self.key_map:
					self.key[self.key_map[event.key]] = 1

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button in self.mouse_map:
					self.mouse[self.mouse_map[event.button]] = 1

			if event.type == pygame.MOUSEBUTTONUP:
				if event.button in self.mouse_map:
					self.mouse[self.mouse_map[event.button]] = 0

			if event.type == pygame.MOUSEMOTION:
				self.mouse["pos"] = pygame.mouse.get_pos()