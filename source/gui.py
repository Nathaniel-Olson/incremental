import pygame
import constants
import sys

class Group:
	def __init__(self, location, size, color) -> None:
		self.rect = pygame.Rect(location, size)
		self.color = color
		self.shown = True
		self.children = list()

	def move_to(self, location) -> None:
		self.rect.left = location[0]
		self.rect.top = location[1]

	def render(self, surface) -> None:
		if not self.shown:
			return

		pygame.draw.rect(surface, self.color, self.rect, border_radius = 15)
		for child in self.children:
			child.render(surface)

	def add_child(self, child) -> None:
		self.children.append(child)

class TextBox:
	def __init__(self, group, location, size, color) -> None:
		self.group = group
		self.color = color
		self.relative_location = location
		self.absolute_location = (self.group.rect.left + location[0],
								  self.group.rect.top + location[1])

		self.rect = pygame.Rect(self.absolute_location, size)
		self.group.add_child(self)

		self.children = list()

	def realign(self) -> None:
		self.absolute_location = (self.group.rect.left + self.relative_location[0],
								  self.group.rect.top + self.relative_location[1])

		self.rect.topleft = self.absolute_location

	def render(self, surface) -> None:
		self.realign()
		pygame.draw.rect(surface, self.color, self.rect, border_radius = 5)
		for child in self.children:
			child.render(surface)

	def add_child(self, child) -> None:
		self.children.append(child)

class Text:
	def __init__(self, textbox, location, string, font, color) -> None:
		self.textbox = textbox
		self.string = string
		self.font = font
		self.color = color

		self.rendered_text = self.font.render(self.string, True, self.color)

		self.relative_location = location
		self.absolute_location = (self.textbox.absolute_location[0] + location[0],
								  self.textbox.absolute_location[1] + (self.textbox.rect.height - self.rendered_text.get_height()) / 2)
		self.textbox.add_child(self)


	def realign(self) -> None:
		self.absolute_location = (self.textbox.absolute_location[0] + self.relative_location[0],
								  self.textbox.absolute_location[1] + (self.textbox.rect.height - self.rendered_text.get_height()) / 2)

	def render(self, surface) -> None:
		self.realign()
		surface.blit(self.rendered_text, self.absolute_location)

	def set_string(self, string) -> None:
		if string != self.string:
			self.string = string
			self.rendered_text = self.font.render(self.string, True, self.color)

	def set_color(self, color) -> None:
		if color != self.color:
			self.color = color
			self.rendered_text = self.font.render(self.string, True, self.color)

class Button(TextBox):
	def check_point_intersect(self, point) -> bool:
		if not self.group.shown:
			return False
		return self.rect.collidepoint(point)

class Slider(TextBox):
	...


def main():
	pygame.init()

	screen = pygame.display.set_mode((640, 480))

	clock = pygame.time.Clock()

	color = constants.Color()
	font = constants.Font()
	font.initialize_all()

	group1 = Group((10, 10), (620, 460), color.PRUSSIAN_BLUE)
	textbox1a = TextBox(group1, (10, 10), (295, 60), color.DUSK_BLUE)
	textbox1b = TextBox(group1, (315, 10), (295, 60), color.DUSK_BLUE)
	text1a = Text(textbox1a, (10, 0), "I am text1a", font.CENTURY40, color.ALABASTER_GREY)
	text1b = Text(textbox1b, (10, 0), "I am text1b", font.CENTURY40, color.ALABASTER_GREY)

	button1a = Button(group1, (10, 80), (295, 60), color.DUSK_BLUE)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					text1a.set_string("I am evil text1a")
				if event.key == pygame.K_w:
					pass
				if event.key == pygame.K_d:
					pass
				if event.key == pygame.K_s:
					pass
				if event.key == pygame.K_SPACE:
					pass

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a:
					text1a.set_string("I am text1a")

			if event.type == pygame.MOUSEBUTTONDOWN:
				if button1a.check_point_intersect(pygame.mouse.get_pos()):
					button1a.color = color.DUSTY_DENIM

			if event.type == pygame.MOUSEBUTTONUP:
				button1a.color = color.DUSK_BLUE

		screen.fill(color.INK_BLACK)

		group1.render(screen)

		pygame.display.update()

if __name__ == "__main__":
	main()