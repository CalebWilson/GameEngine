"""
	Track.py

	defines the Track class, which is a subclass of
	ScrollScene modified for the race game.
"""

import pygame
from ScrollScene import ScrollScene
from Car import Car

Vector = pygame.math.Vector2

class Track (ScrollScene):
	#initialize game engine
	def __init__ (self,

			#background
			background = "",

			#screen
			screen_size = (320, 320),

			#sprite groups in the scene
			groups = [],

			#focus sprite to track
			fs_image = pygame.image.load ("Car.png"),
			fs_pos = (160, 160),
			fs_vel = (0, 0),
			fs_acc = (0, 0),
			fs_ang_pos = 0,
			fs_ang_vel = 0,
			fs_ang_acc = 0,
			fs_groups = [],

			#how close the focus sprite can get to the edge of the screen
			focus_distance = (120, 120)
	):

		#initialize image
		if background == "":
			background = pygame.Surface(screen_size)
			background.fill ((56, 150, 0)) #green

		self.groups = groups

		#initialize screen velocity to be subtracted from sprites
		self.velocity = Vector()
		self.focus_distance = focus_distance
		print(self.velocity)

		#initialize focus sprite in parent class
		super().__init__ (
			background,
			screen_size,
			groups,

			fs_image,
			fs_pos,
			fs_vel,
			fs_acc,
			fs_ang_pos,
			fs_ang_vel,
			fs_ang_acc,
			fs_groups
		)

		#initialize font
		self.font = pygame.font.SysFont(None, 24)

	#end __init__()

	#overwrite for custom focus sprite
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
		self.focus_sprite = Car (
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

	#boundary management
	def update (self):
		#run normal update code
		super().update()

		#find collisions
		collisions = self.detect_collisions()

		#detect and resolve collisions
		for collision in collisions:
			self.collide (collision)

		#write controls to screen
		k_text = self.font.render("K: Accelerate", True, (255, 255, 255))
		j_text = self.font.render("J: Decelerate", True, (255, 255, 255))
		d_text = self.font.render("D: Steer Left", True, (255, 255, 255))
		f_text = self.font.render("K: Steer Right", True, (255, 255, 255))
		self.screen.blit(k_text, (0,  0))
		self.screen.blit(j_text, (0, 20))
		self.screen.blit(d_text, (0, 40))
		self.screen.blit(f_text, (0, 60))

	#end def update()

	#if the car hits the wall
	def collide (self, collision):
		self.game_over = True
		#kill the car
		collision[0].die()
		self.screen.blit (self.font.render ("YOU CRASHED", True, (0, 0, 0)), (self.screen.get_rect().centerx, self.screen.get_rect().centery))

	#end def collide()

#end class Track
