"""
	ScrollScene.py

	defines the ScrollScene class, which is a subclass of
	Scene that scrolls to track a primary Sprite.
"""

class ScrollScene (object):
	#initialize game engine
	def __init__ (self,
		#full background image
		image = "",

		#screensize
		screen_size = (640, 480),

		#sprite groups in the scene
		groups = [],

		#focus sprite to track
		fs_image = "",
		fs_pos = (0, 0),
		fs_vel = (0, 0),
		vs_acc = (0, 0),
		vs_ang_pos = 0,
		vs_ang_vel = 0,
		vs_ang_acc = 0,
		fs_groups = []
	):
		#initialize parent class
		super().__init__(image, screen_size, groups[])

	#end __init__()

	#misc
	def update():
		pass

#end class Scene

mysprite = FullSprite (velocity = (5, 5)); 


