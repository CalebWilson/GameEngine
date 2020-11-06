"""
	Car.py

	defines the Car class, which is a subclass of
	ScrollSprite
"""

from ScrollSprite import ScrollSprite
import pygame
import math #degrees()

class Car (ScrollSprite):
	def __init__ (self,

			#Scene on which the sprite will be rendered
			#no default value; sprites must be provided a Scene
			scene,

			#image
			image = pygame.image.load ("Car.png"),

			#kinematics accept any type accepted by Vector2 constructor
			position     = (0, 0),
			velocity     = (0, 0),
			acceleration = (0, 0),

			ang_pos = -90, #angular position (degrees)
			ang_vel =   0, #angular velocity (degrees per frame)
			ang_acc =   0, #angular acceleration (degrees per frame per frame)

			visible  = True,
			tangible = True,

			#Groups to which the sprite belongs
			groups = [],

			#Car specs
			max_acc   = 0.05, #how fast the car speeds up (pixels per frame per frame)
			max_speed = 5, #fastest speed the car can go
			turn_rad  = 40, #turning radius

	): #how I feel right now trying to make this work

		#initialize parent class
		super().__init__ (
			scene,
			image,
			position, velocity, acceleration,
			ang_pos, ang_vel, ang_acc,
			visible, tangible,
			groups)

		"""
			Inputs will be either a 1 or 0 depending on whether their corresponding
			key is pressed. Before use, they will be subtracted (right - left,
			forward - backward) so as to cancel out conflicting inputs and calculate
			accelerations in the correct directions.
		"""
		self.left     = 0 #steer left
		self.right    = 0 #steer right
		self.forward  = 0 #accelerate forwards
		self.backward = 0 #decelerate backwards

		#Car specs
		self.max_acc   = max_acc
		self.max_speed = max_speed
		self.turn_rad  = turn_rad

		#whether the car is alive to accept inputs
		self.alive = True

	#end def __init__()

	#respond to inputs
	def update(self):
		#don't do anything if car is dead
		if not self.alive:
			return

		#turning: omega = v / r
		self.ang_vel  = math.degrees (self.velocity.magnitude() / self.turn_rad) #magnitude
		self.ang_vel *= (self.right - self.left) #direction

		#tangential acceleration = acceleration in direction of motion
		tangent_acc = pygame.math.Vector2()
		tangent_acc.from_polar (
			(self.max_acc * (self.forward - self.backward), #magnitude
			self.ang_pos) #direction
		)

		#centripetal acceleration = v^2 / r, perpendicular to direction of motion
		centrip_acc = pygame.math.Vector2()

		#check whether car is moving forwards or backwards
		direction = pygame.math.Vector2()
		direction.from_polar ((1, self.ang_pos))
		direction = direction.dot (self.velocity)
		#direction = (1 if direction > 0 else -1)
		if direction > 0:
			direction = 1
		else:
			direction = -1

		centrip_acc.from_polar (
			(self.velocity.magnitude_squared()
				/ self.turn_rad
				* (self.right - self.left),  #magnitude
			self.ang_pos + (90 * direction))
		)

		#combine tangential and centripetal acceleration
		self.acceleration = tangent_acc + centrip_acc

		#apply kinematics and scrolling
		super().update()

		#restrict speed
		if self.velocity.magnitude() > self.max_speed:
			self.velocity.scale_to_length (self.max_speed)

	#end def up update()

	#handle inputs
	def handle_event (self, event):
		#if a key is pressed, set its value to 1
		if event.type == pygame.KEYDOWN:
			print(event.key, "down")
			#k
			if event.key == 107:
				self.forward = 1
			#j
			elif event.key == 106:
				self.backward = 1
			#f
			elif event.key == 102:
				self.right = 1
			#d
			elif event.key == 100:
				self.left = 1

		#end if a key is pressed

		#if a key is released, set its value to 0
		elif event.type == pygame.KEYUP:
			print(event.key, "up")
			#k
			if event.key == 107:
				self.forward = 0
			#j
			elif event.key == 106:
				self.backward = 0
			#f
			elif event.key == 102:
				self.right = 0
			#d
			elif event.key == 100:
				self.left = 0

		#end if a key is released

	#end def handle_event()

	#destroy car when it hits something
	def die (self):
		#set velocity and acceleration to 0
		self.acceleration.update (0, 0)
		self.velocity.update (0, 0)

		self.alive = False

#end class Car
