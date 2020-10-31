"""
	Scene.py

	defines the Scene class, which has an array of Sprite Groups.
"""
import pygame

class Scene (object):
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

	#misc
	def update():
		pass

#end class Scene

mysprite = FullSprite (velocity = (5, 5)); 
