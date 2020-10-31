"""
	WrapSprite.py

	defines the WrapSprite class, which is a subclass of
	FullSprite with a wraparound boundary behavior
"""

class WrapSprite (FullSprite)
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
	):
		#initialize parent class
		super().__init__(self,
			image,
			position, velocity, acceleration,
			ang_pos, ang_vel, ang_acc,
			visible, tangible,
			groups, scene)
		
		"""
			Initialize array to store sprite images for use in
			wraparound boundary behavior. sprites[0] will appear
			on the opposite side of the screen when FullSprite
			passes an x boundary, sprites[1] will appear on the
			opposite top or bottom of the screen when FullSprite
			passes a y boundary, and sprites[2] will appear in
			the opposite corner when FullSprite passes both an x
			boundary and a y boundary.
		"""
		self.sprites = []
		for i in range(3):
			self.sprites.append (pygame.sprites.Sprite())

	#boundary behavior: wrap
	def boundary ():
		#if the center of the sprite has passed the edge of the screen,
		#wrap around to the opposite edge
		hit_bounds = self.bounds_check ((0, 0))
		if hit_bounds[i]:
			self.position[i] %= self.scene.screen_size[i]

		#if part of the sprite has passed through the left of the screen,
		#create a new sprite on the right side
		if self.rect.left < 0:
			self.sprites[0].image = self.image
			self.sprites[0].rect  = self.rect
			self.sprites[0].rect.center.x += self.scene.screen.get_width

		#if part of the sprite has passed through the right of the
		#screen, create a new sprite on the left side
		elif self.rect.right > self.scene.screen.get_width
			self.sprites[0].image = self.image
			self.sprites[0].rect = self.rect
			self.sprites[0].rect.center.x -= self.scene.screen.get_width

		#if part of the sprite has passed through the top of the screen,
		#create a new sprite on the bottom
		if self.rect.top < 0:
			self.sprites[1].image = self.image
			self.sprites[1].rect  = self.rect
			self.sprites[1].rect.center += self.scene.screen.get_height

		#if part of the sprite has passed through the bottom of the
		#screen, create a new sprite on the top
		elif self.rect.bottom > self.scene.screen.get_height
			self.sprites[1].image = self.image
			self.sprites[1].rect  = self.rect
			self.sprites[1].rect.center -= self.scene.screen.get_height

	#end def boundary()

#end class WrapSprite
