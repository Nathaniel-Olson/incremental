import pygame

class Button:
	def __init__(self, width: int, height: int, location: tuple[int], color: tuple[int]) -> None:
		self.rect = pygame.Rect(location, (width, height))
		self.shown = False
		self.color = color
		self.text1 = None
		self.text2 = None

		self.text1_coordinate = None
		self.text2_coordinate = None

	def check_point_intersect(self, click_coordinate: tuple[int]) -> bool:
		if self.shown:
			return self.rect.collidepoint(click_coordinate)

		else:
			return False

	def show(self) -> None:
		self.shown = True
		return None

	def hide(self) -> None:
		self.shown = False
		return None

	def write(self, string: str, font: pygame.Font, color: tuple[int]) -> None:
		self.text_surface = font.render(string, False, color)

	def text(self, text: str,
				   font: pygame.Font,
				   color: tuple[int],
				   text2: str | None = None,
				   font2: pygame.Font | None = None,
				   x_alignment: str = "left",
				   x_alignment_spacing: int = 8) -> None:

		text_size = font.size(text)
		text_width, text_height = text_size[0], text_size[1]

		if self.rect.height < text_height:
			raise ValueError(f"Text too tall for button, {text_height=}, {self.rect.height=}, {self}")

		if self.rect.width < text_width:
			raise ValueError(f"Text too wide for button, {text_width=}, {self.rect.width=}, {self}")

		y_text_spacing = (text_height - self.rect.height) / 2

		y_coordinate = int(self.rect.top - y_text_spacing)

		if x_alignment == "left":
			if text2 != None:
				raise ValueError(f"only 1 text can be passed in to use the 'left' keyword. {self}")
			x_coordinate = int(self.rect.left + x_alignment_spacing)

		elif x_alignment == "right":
			if text2 != None:
				raise ValueError(f"only 1 text can be passed in to use the 'right' keyword. {self}")
			x_coordinate = int(self.rect.right - (x_alignment_spacing + text_width))

		elif x_alignment == "split":

			if text2 == None:
				raise ValueError(f"2 texts must be passed in to use the 'split' keyword. {self}")

			text2_size = font2.size(text2)
			text2_width, text2_height = text2_size[0], text2_size[1]

			if self.rect.width < text_width + text2_width:
				raise ValueError(f"the width of these two texts is too large. sorry dawg. {self}")

			x_coordinate = int(self.rect.left + x_alignment_spacing)
			x2_coordinate = int(self.rect.right - (x_alignment_spacing + text2_width))

			self.text2 = font2.render(text2, True, color)
			self.text2_coordinate = (x2_coordinate, y_coordinate)

		else:
			raise ValueError(f"invalid identifier. must be one of left, right, split. chosen: {x_alignment}")

		self.text1 = font.render(text, True, color)
		self.text1_coordinate = (x_coordinate, y_coordinate)
		return None

	def render(self, surface: pygame.Surface) -> None:
		if self.shown:
			pygame.draw.rect(surface, self.color, self.rect)
			if self.text1 != None:
				surface.blit(self.text1, self.text1_coordinate)
			if self.text2 != None:
				surface.blit(self.text2, self.text2_coordinate)
			return None
		else:
			return None



