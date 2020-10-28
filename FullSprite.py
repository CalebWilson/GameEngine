"""
	FullSprite.py

	defines the FullSprite class, which is a fleshed-out version
	of pygame.sprite.Sprite
"""
#rename vector class
Vector = pygame.math.Vector2

class FullSprite (pygame.sprite.Sprite)
	def __init__ (self,
		#image
		img = "",

		#kinematics
		    position = Vector(),
		    velocity = Vector(),
		acceleration = Vector(),
		     ang_pos = 0, #angular position (degrees)
			  ang_vel = 0, #angular velocity (degrees per frame)
			  ang_acc = 0, #angular acceleration (degrees per frame per frame)

		#Groups to which the sprite belongs
		groups = []
	):
		#initialize parent class
		pygame.sprite.Sprite.__init__(self)
		
		#source master copy of image
		if img == "":
			#default sprite image is a white box
			self.master_img = pygame.Surface ((25, 25))
			self.master_img.fill ((255, 255, 255))
		else:
			self.master_img = img
		
		#initialize viewable image
		self.img = self.master_img

		#hitbox
		self.rect = self.image.get_rect()

		#kinematics
		self.position     = position
		self.velocity     = velocity
		self.acceleration = acceleration
		self.ang_pos      = ang_pos
		self.ang_vel      = ang_vel
		self.ang_acc      = ang_acc

	#end def __init__()

	#update sprite for next frame
	def update():
		#update kinematics
		self.velocity += self.acceleration
		self.position += self.velocity

		self.ang_vel  += self.ang_acc
		self.ang_pos  += self.ang_vel

		#update orientation
		og_center = self.rect.center #save original center
		self.img = transform.rotate (self.master_img, self.ang_pos) #rotate
		self.rect = self.image.get_rect(center = og_center) #recenter

	#end def update()

#end class FullSprite
