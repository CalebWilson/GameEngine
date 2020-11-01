"""
	Track.py

	defines the Track class, which is a subclass of
	ScrollScene modified for the race game.
"""

import ScrollScene

class Track (ScrollScene):
	#initialize game engine
	def __init__ (self,
		#full background image
		image = "",

		#screen
		screen_size = (640, 640),

		#sprite groups in the scene
		groups = [],

		#focus sprite to track
		fs_image = "Car.png",
		fs_pos = (320, 480),
		fs_vel = (0, 0),
		fs_acc = (0, 0),
		fs_ang_pos = 0,
		fs_ang_vel = 0,
		fs_ang_acc = 0,
		fs_groups = [],

		#how close the focus sprite can get to the edge of the screen
		focus_distance = (screen_size[x] // 5, screen_size[y] // 5)
	):

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

	#end def update()

	#if the car hits the wall
	def collide ((car, wall)):
		#kill the car
		car.die()

	#end def collide()

#end class Scene
