"""
	ScrollScene.py

	defines the ScrollScene class, which is a subclass of
	Scene that scrolls to track a primary Sprite.
"""
from Scene import Scene

class ScrollScene (Scene):
	#initialize game engine
	def __init__ (self,

			#full background image
			image = "",

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
		super().__init__(image, screen_size, groups)

		#how close the focus sprite can get to the edge of the screen
		focus_distance = (screen_size[x] // 5, screen_size[y] // 5)

		#initialize focus sprite
		self.focus_sprite = ScrollSprite (
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
		#for each dimension
		for i in range(2):
			if self.focus_sprite.rect.center[i] <= focus_distance[i]:
				self.focus_sprite.rect.center = focus_distance[i]
				self.velocity[i] = self.focus_sprite.velocity[i]
			else:
				self.velocity[i] = 0

		#end for each dimension
	
	#end def update()

	#pass event handling to focus sprite
	def handle_event (event):
		self.focus_sprite.handle_event (event)

	#end def handle_event()


#end class Scene
