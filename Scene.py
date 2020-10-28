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



	):
		pygame.init()

		#initialize screen
		self.screen = pygame.display.set_mode ((640, 480))  
		
		#source level background
		self.background = pygame.Surface (self.screen.get_size())
		self.background.fill ((0, 0, 0))

		#create sprites
		test_sprite = Sprite
		self.sprites = 

