"""
	ScrollScene.py

	defines the ScrollScene class, which is a subclass of
	Scene that scrolls to track a primary Sprite.
"""

import pygame
from Scene import Scene
from ScrollSprite import ScrollSprite

class ScrollScene (Scene):
	#initialize game engine
	def __init__ (self,

			#background image
			background = "",

			#screen
			screen_size = (640, 480),

			#sprite groups in the scene
			groups = [],

			#focus sprite to track
			fs_image = "",
			fs_pos = (0, 0),
			fs_vel = (0, 0),
			fs_acc = (0, 0),
			fs_ang_pos = 0,
			fs_ang_vel = 0,
			fs_ang_acc = 0,
			fs_groups = []
	):
		#initialize parent class
		super().__init__(background , screen_size, groups)

		#how close the focus sprite can get to the edge of the screen
		focus_distance = (screen_size[0] // 5, screen_size[1] // 5)

		#initialize screen velocity to be subtracted from sprites
		velocity = pygame.math.Vector2()

		print("ScrollScene fs_image:", fs_image)

		self.construct_focus_sprite (
			fs_image,
			fs_pos,
			fs_vel,
			fs_acc,
			fs_ang_pos,
			fs_ang_vel,
			fs_ang_acc,
			fs_groups
		)
	
	#end __init__()

	#initialize focus sprite
	#overwrite if using custom ScrollSprite
	def construct_focus_sprite (
			self,
			fs_image,
			fs_pos,
			fs_vel,
			fs_acc,
			fs_ang_pos,
			fs_ang_vel,
			fs_ang_acc,
			fs_groups
	):
		self.focus_sprite = ScrollSprite (
			self,
			fs_image,
			fs_pos,
			fs_vel,
			fs_acc,
			fs_ang_pos,
			fs_ang_vel,
			fs_ang_acc,
			fs_groups
		)

	#end def construct_focus_sprite()

	#boundary management
	def update(self):

		#assume focus_sprite not at edge
		self.velocity.update (0, 0)

		#left scrolling
		if self.focus_sprite.rect.center[0] <= self.focus_distance[0]:
			self.focus_sprite.rect.centerx = self.focus_distance[0]
			self.velocity[0] = self.focus_sprite.velocity[0]

		#right scrolling
		if self.focus_sprite.rect.center[1] <= self.focus_distance[1]:
			self.focus_sprite.rect.centery = self.focus_distance[1]
			self.velocity[1] = self.focus_sprite.velocity[1]

		#bottom 
		if self.screen.get_size()[0] - self.focus_sprite.rect.center[0] <= self.focus_distance[0]:
			self.focus_sprite.rect.centerx = self.focus_distance[0]
			self.velocity[0] = self.focus_sprite.velocity[0]

		if self.screen.get_size()[1] - self.focus_sprite.rect.center[1] <= self.focus_distance[1]:
			self.focus_sprite.rect.centery = self.focus_distance[1]
			self.velocity[1] = self.focus_sprite.velocity[1]

		#end for each dimension
	
	#end def update()

	#pass event handling to focus sprite
	def handle_event (self, event):
		if self.game_over == False:
			self.focus_sprite.handle_event (event)

	#end def handle_event()


#end class Scene
