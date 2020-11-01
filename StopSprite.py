"""
	StopSprite.py

	defines the StopSprite class, which is a subclass of
	FullSprite with a stopping boundary behavior
"""

class WrapSprite (FullSprite)
	def __init__ (self,

			#Scene on which the sprite will be rendered
			#no default value; sprites must be provided a Scene
			scene,
		
			#image
			image = "",

			#kinematics
			#these will accept any type that can be accepted by the Vector2 constructor
			position     = (0, 0),
			velocity     = (0, 0),
			acceleration = (0, 0),

			ang_pos = 0, #angular position (degrees)
			ang_vel = 0, #angular velocity (degrees per frame)
			ang_acc = 0, #angular acceleration (degrees per frame per frame)

			visible  = True,
			tangible = True,

			#Groups to which the sprite belongs
			groups = []
	):
		#initialize parent class
		super().__init__(self,
			image,
			position, velocity, acceleration,
			ang_pos, ang_vel, ang_acc,
			visible, tangible,
			groups, scene)
		
	#boundary behavior: scroll
	def boundary ():
		hit_bounds = bounds_check()
		
		#for each dimension
		for i in range(2):
			if hit_bounds[i]:
				self.velocity[i] = 0;
				self.acceleration[i] = 0;

	#end def boundary()

#end class WrapSprite
