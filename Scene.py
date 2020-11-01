"""
	Scene.py

	defines the Scene class, which has an array of Sprite Groups.
"""
import pygame
import FullSprite

#define framerate in milliseconds per frame
MPF = 40

class Scene (object):
	#initialize game engine
	def __init__ (self,
		#full background image
		image = "",

		#screensize
		screen_size = (640, 480),

		#sprite groups in the scene
		"""
			The order in which Groups are added may have some significance,
			depending on your implementation of collide(), as detect_collisions()
			returns a list of tuples of colliding FullSprites wherein the FullSprite
			belonging to the Group added earlier is element 0 and the FullSprite
			belonging to the Group added later is element 1.
		"""
		groups = [],
	):
		pygame.init()

		#initialize screen
		screen = pygame.display.set_mode (screen_size)

		#initialize background
		if image == "":
			self.background = pygame.Surface (screen_size)
			self.background.fill ((0, 0, 0))
		else:
			self.background = image

		self.start()

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
		self.clock.tick(MPF) #milliseconds per frame

		#handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.go = False
			self.handle_event (event)

		#update
		self.update()

		#update Sprites
		for group in self.groups:
			group.clear(self.screen, self.background)
			group.update()
			group.draw (self.screen)

		#draw screen to display
		pygame.display.flip()

	#end def __mainLoop()

	#misc
	def update():
		pass

	#detect collisions
	def detect_collisions():

		#list of tuples containing colliding sprites
		collisions = []

		#for each group
		for group in range(len(self.groups)):
			#for each sprite in the group
			for sprite in range(len(self.groups[group])):
				#if the sprite is tangible
				if self.groups[group][sprite].tangible:
					#for the rest of the groups
					for other_group in range(group + 1, len(self.groups)):
						#if the sprite is not also in that group
						if self.groups[group][sprite] not in self.groups[other_group]:
							#for each other sprite
							for other_sprite in range(len(self.groups[other_group])):
								#if the other sprite is tangible
								if self.groups[other_group][other_sprite].tangible:
									#if the sprites' bounding rectangles intersect
									if sprite.rect.colliderect (other_sprite.rect):
										#add the collision to the list
										collisions.append (
											(self.groups[group][sprite],
												self.groups[other_group][other_sprite])
										)
		#end for each group

		return collisions
	
	#end def detect_collisions()

	#resolve collisions
	def collide (sprite1, sprite2):
		pass

	#event handler
	def handle_event (event):
		pass

#end class Scene

#mysprite = FullSprite (velocity = (5, 5)); 
