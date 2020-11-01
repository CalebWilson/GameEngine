"""
	Car.py

	defines the Car class, which is a subclass of
	ScrollSprite
"""

import Engine.ScrollSprite

class Car (ScrollSprite)
	def __init__ (self,

		#Scene on which the sprite will be rendered
		#no default value; sprites must be provided a Scene
		scene,

		#image
		image = "Car.py",

		#kinematics
		#these will accept any type that can be accepted by the Vector2 constructor
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
		max_acc   =  1, #how fast the car speeds up (pixels per frame per frame)
		max_speed = 20, #fastest speed the car can go
		turn_rad  = 20, #turning radius

	): #how I feel right now trying to make this work

		#initialize parent class
		super().__init__(self,
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

		#whether the car will accept inputs
		self.alive = True

	#end def __init__()

	#respond to inputs
	def update():
		#don't do anything if car is dead
		if not self.alive:
			return

		#turning: omega = v / r
		self.ang_vel  = self.velocity.magnitude() / turn_rad #magnitude
		self.ang_vel *= (self.right - self.left) #direction

		#tangential acceleration = acceleration in direction of motion
		tangent_acc = Vector()
		tangent_acc.from_polar (
			(max_acc * (self.forward - self.backward), #magnitude
			self.ang_pos) #direction
		)

		#centripetal acceleration = v^2 / r, perpendicular to direction of motion
		centrip_acc = Vector()
		centrip_acc.from_polar (
			(self.velocity.magnitude_squared() / turn_rad,  #magnitude
			self.ang_pos + (90 * (self.right - self.left))) #direction
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
	def handle_event (event):
		if
		#if a key is pressed, set its value to 1
		if event.event_name == "KEYDOWN":
			#k
			if event.key == "K_k":
				self.forward = 1
			#j
			elif event.key == "K_j":
				self.backward = 1
			#f
			elif event.key == "K_f":
				self.right = 1
			#d
			elif event.key == "K_d":
				self.left = 1

		#end if a key is pressed

		#if a key is released, set its value to 0
		elif event.event_name == "KEYUP":
			#k
			if event.key == "K_k":
				self.forward = 0
			#j
			elif event.key == "K_j":
				self.backward = 0
			#f
			elif event.key == "K_f":
				self.right = 0
			#d
			elif event.key == "K_d":
				self.left = 0

		#end if a key is released

	#end def handle_event()

	#destroy car when it hits something
	def die():
		self.alive = False
		self.image = pygame.image.load ("blast.png")

#end class Car
