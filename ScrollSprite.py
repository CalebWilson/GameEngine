"""
	ScrollSprite.py

	defines the ScrollSprite class, which is a subclass of
	FullSprite with a scrolling boundary behavior
"""

from ScrollScene import ScrollScene
from FullSprite  import FullSprite

class ScrollSprite (FullSprite):
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
		
	"""
		No action is required when a Sprite hits a boundary here, because the Sprite
		is either the focus sprite of the ScrollScene, and will therefore never
		touch the boundary, or it is just another sprite, and will therefore
		continue and not care if it hits the boundary. The scrolling behavior is
		instead implemented in the update() function by subtracting the
		ScrollScene's velocity (equal to the focus sprite's velocity when it is near
		the boundary and 0 otherwise) from the positions of all ScrollSprites on
		every frame.
	"""
	def boundary():
		pass

	#end def boundary()

	#account for normal kinematics as well as ScrollScene velocity
	def update():
		super().update()
		self.position -= scene.velocity
		self.rect.center = (self.position.x, self.position.y)

	#handle events received from ScrollScene
	def handle_event (event):
		pass

#end class ScrollSprite
