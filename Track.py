"""
	Track.py

	defines the Track class, which is a subclass of
	ScrollScene modified for the race game.
"""

import pygame
from ScrollScene import ScrollScene

class Track (ScrollScene):
	#initialize game engine
	def __init__ (self,

			#full background image
			image = "",

			#screen
			screen_size = (320, 320),

			#sprite groups in the scene
			groups = [],

			#focus sprite to track
			fs_image = pygame.image.load("Car.png"),
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
		self.image = pygame.Surface(screen_size)
		self.image.fill ((0, 255, 0)) #green

		#initialize parent class
		super().__init__(image, screen_size, groups)

		#initialize focus sprite
		self.focus_sprite = Car (
			fs_image,
			fs_pos,
			fs_vel,
			fs_acc,
			fs_ang_pos,
			fs_ang_vel,
			fs_ang_acc,
			fs_groups
		)

		#initialize screen velocity to be subtracted from sprites
		velocity = Vector()

	#end __init__()

	#boundary management
	def update():
		#run normal update code
		super().update()

		#find collisions
		collisions = self.detect_collisions()

		#detect and resolve collisions
		for collision in collisions:
			collide (collision)

		#write controls to screen
		font = pygame.font.SysFont(None, 24)
		k_text = font.render("K: Accelerate", True, WHITE)
		j_text = font.render("J: Decelerate", True, WHITE)
		d_text = font.render("D: Steer Left", True, WHITE)
		f_text = font.render("K: Steer Right", True, WHITE)
		screen.blit(k_text, (0,  0))
		screen.blit(j_text, (0, 10))
		screen.blit(d_text, (0, 20))
		screen.blit(f_text, (0, 30))

	#end def update()

	#if the car hits the wall
	def collide (collision):
		#kill the car
		collision[0].die()

	#end def collide()

#end class Scene
