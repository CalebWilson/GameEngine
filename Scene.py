import pygame

class Scene (object):
	"""
		The stage on which Sprites act.

		Contains array of Sprites.
	"""

	#initialize game engine
	def __init__ (self,
		#full background image
		img = "",

		#screensize
		screen_size = (640, 480),

		#sprite groups in the scene
		groups = [],
	):
		pygame.init()

		#initialize screen
		screen = pygame.display.set_mode (screen_size)

		#initialize background
		if img == "":
			self.background = pygame.Surface (screen_size)
			self.background.fill ((0, 0, 0))
		else:
			self.background = img

	#end __init__()

	#beginning of the loop
	def start():
		self.screen.blit (self.background, (0, 0))
		self.clock = pygame.time.Clock()
		self.go = True
		while self.go:
			self.__mainLoop()

	#game loop
	def __mainLoop():
		self.clock.tick(30)

		for event in pygame.event.get()
			if event.type == pygame.QUIT:
				self.go = False
			self.doEvents(event)

		#user-defined update
		self.update()

		for group in self.groups:
			group.clear(self.screen, self.background)
			group.update()
			group.draw (self.screen)
	
	#end def __mainLoop()

	#update and redraw sprites; collision detection
	def update():
		pass



