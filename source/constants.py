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

		self.INK_BLACK = (13, 27, 42, 0)
		self.PRUSSIAN_BLUE = (27, 38, 59, 0)
		self.DUSK_BLUE = (65, 90, 119, 0)
		self.DUSTY_DENIM = (119, 141, 169, 0)
		self.ALABASTER_GREY = (224, 225, 221, 0)

# FONTS
class Font:
	def __init__(self, anti_aliasing = True):
		self.ANTI_ALIASING = anti_aliasing

	def initialize_all(self) -> None:
		self.CENTURY40 = pygame.font.SysFont("century", 40)
		self.CENTURY20 = pygame.font.SysFont("century", 20)

		self.SYMBOL40 = pygame.font.SysFont("symbol", 40)
		self.SYMBOL20 = pygame.font.SysFont("symbol", 20)


