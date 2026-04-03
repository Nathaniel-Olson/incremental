import pygame

# COLORS
class Color:
	def __init__(self) -> None:
		self.WHITE = (255, 255, 255, 0)
		self.BLACK = (0, 0, 0, 0)
		self.RED = (255, 0, 0, 0)
		self.GREEN = (0, 255, 0, 0)
		self.BLUE = (0, 0, 255, 0)
		self.GREY = (127, 127, 127, 0)

		### BLUE COLORWAVE
		# self.BACKGROUND = (13, 27, 42, 0)
		# self.GROUP = (27, 38, 59, 0)
		# self.TEXTBOX = (65, 90, 119, 0)
		# self.TEXTBOX_LIGHT = (119, 141, 169, 0)
		# self.TEXT = (224, 225, 221, 0)

		### PURPLE COLORWAVE
		# self.BACKGROUND = (47, 24, 75, 0)
		# self.GROUP = (83, 43, 136, 0)
		# self.TEXTBOX = (155, 114, 207, 0)
		# self.TEXTBOX_LIGHT = (200, 177, 228, 0)
		# self.TEXT = (244, 239, 250, 0)

		### BLACK COLORWAVE
		self.BACKGROUND = (33, 37, 41, 0)
		self.GROUP = (52, 58, 64, 0)
		self.TEXTBOX = (73, 80, 87, 0)
		self.TEXTBOX_LIGHT = (108, 117, 125, 0)
		self.TEXT = (222, 226, 230, 0)

# FONTS
class Font:
	def __init__(self, anti_aliasing = True):
		self.ANTI_ALIASING = anti_aliasing

	def initialize_all(self) -> None:
		self.CENTURY40 = pygame.font.SysFont("century", 40)
		self.CENTURY20 = pygame.font.SysFont("century", 20)

		self.SYMBOL40 = pygame.font.SysFont("symbol", 40)
		self.SYMBOL20 = pygame.font.SysFont("symbol", 20)


