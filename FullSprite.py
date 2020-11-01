"""
	FullSprite.py

	defines the FullSprite class, which is a fleshed-out version
	of pygame.sprite.Sprite
"""
import pygame
import Scene

#rename vector class
Vector = pygame.math.Vector2

#define coordinate constants
X = 0
Y = 1

class FullSprite (pygame.sprite.Sprite):
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
			groups = [],
	):
		#initialize parent class
		pygame.sprite.Sprite.__init__(self)
		
		#source master copy of image
		if image == "":
			#default sprite image is a white box
			self.master_image = pygame.Surface ((25, 25))
			self.master_image.fill ((255, 255, 255))
		else:
			self.master_image = image
		
		#initialize viewable image
		self.image = self.master_image

		#kinematics
		self.position     = Vector (position)
		self.velocity     = Vector (velocity)
		self.acceleration = Vector (acceleration)
		self.ang_pos      = ang_pos
		self.ang_vel      = ang_vel
		self.ang_acc      = ang_acc

		#hitbox
		self.rect = self.image.get_rect()
		self.rect.center = (self.position.x, self.position.y)

	#end def __init__()

	#update sprite for next frame
	def update():
		#update kinematics
		self.velocity += self.acceleration
		self.position += self.velocity
		self.rect.center = (self.position.x, self.position.y)

		self.ang_vel  += self.ang_acc
		self.ang_pos  += self.ang_vel

		#update orientation
		og_center = self.rect.center #save original center
		self.image = transform.rotate (self.master_image, self.ang_pos) #rotate
		self.rect = self.image.get_rect(center = og_center) #recenter

		#boundary behavior
		self.boundary();

	#end def update()

	#check whether at bounds
	def bounds_check():
		hit_bounds = (False, False)

		#for each dimension
		for i in range(2):
			if self.rect.center < 0 or self.rect.center[i] > scene.screen_size[i]:
				hit_bounds[i] = True

		#end for each dimesion

		return hit_bounds

	#end def bounds_check()

	#boundary behavior
	def boundary():
		pass

#end class FullSprite
