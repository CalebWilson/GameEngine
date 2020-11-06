"""
	Scene.py

	defines the Scene class, which has an array of Sprite Groups.
"""
import pygame
import FullSprite

#define framerate in frames per second
FPS = 50

class Scene (object):
	#initialize game engine
	def __init__ (self,

			#background image
			background = "",

			#screensize
			screen_size = (640, 480),

			#sprite groups in the scene
			#
			#The order in which Groups are added may have some significance,
			#depending on your implementation of collide(), as detect_collisions()
			#returns a list of tuples of colliding FullSprites wherein the
			#FullSprite belonging to the Group added earlier is element 0 and the
			#FullSprite belonging to the Group added later is element 1.
			groups = [],
	):
		pygame.init()

		#initialize screen
		self.screen = pygame.display.set_mode(screen_size)

		#initialize background
		if background == "":
			print ("No image")	
			self.background = pygame.Surface (screen_size)
			self.background.fill ((0, 0, 0))
		else:
			self.background = background

	#end __init__()

	#beginning of the loop
	def start (self):
		self.screen.blit (self.background, (0, 0))
		self.clock = pygame.time.Clock()
		self.go = True
		self.game_over = False
		while self.go:
			self.__mainLoop()

	#game loop
	def __mainLoop (self):
		self.clock.tick(FPS) #milliseconds per frame

		#handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.go = False
			self.handle_event (event)

		if (self.game_over == False):
			#abstract update
			self.update()

			#update Sprites
			for group in self.groups:
				group.clear(self.screen, self.background)
				group.update()
				group.draw (self.screen)

			#draw screen to display
			pygame.display.flip()

		#end if game_over == False

	#end def __mainLoop()

	#misc
	def update (self):
		pass

	#detect collisions
	def detect_collisions (self):

		#list of tuples containing colliding sprites
		collisions = []

		#for each group
		for group in range(len(self.groups)):
			#for each sprite in the group
			for sprite in self.groups[group]:
				#if the sprite is tangible
				if sprite.tangible:
					#for the rest of the groups
					for other_group in range(group + 1, len(self.groups)):
						#if the sprite is not also in that group
						if sprite not in self.groups[other_group]:
							#for each other sprite
							for other_sprite in self.groups[other_group]:
								#if the other sprite is tangible
								if other_sprite.tangible:
									#if the sprites' bounding rectangles intersect
									if sprite.rect.colliderect (other_sprite.rect):
										#add the collision to the list
										collisions.append ((sprite, other_sprite))
		#end for each group

		for collision in collisions:
			for entity in collision:
				print (entity)

		return collisions
	
	#end def detect_collisions()

	#resolve collisions
	def collide (self, sprite1, sprite2):
		pass

	#event handler
	def handle_event (self, event):
		pass

#end class Scene

#mysprite = FullSprite (velocity = (5, 5)); 
