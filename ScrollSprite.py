"""
	ScrollSprite.py

	defines the ScrollSprite class, which is a subclass of
	FullSprite with a scrolling boundary behavior
"""

import Engine.ScrollScene

class ScrollSprite (FullSprite)
	def __init__ (self,
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
		groups = [],

		#Scene on which the sprite will be rendered
		#no default value; sprites must be provided a Scene
		scene

		#how close the sprite can get to the edge of the screen before the
		#scrolling behavior activates
	):
		#initialize parent class
		super().__init__(self,
			image,
			position, velocity, acceleration,
			ang_pos, ang_vel, ang_acc,
			visible, tangible,
			groups, scene)
		
	#boundary behavior: scroll
	def boundary():
		self.position -= scene.velocity

	#end def boundary()

#end class WrapSprite
