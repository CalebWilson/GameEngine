import Track
import Car

cars = pygame.sprite.Group()
road = pygame.sprite.Group()

track = Track (
	image = pygame.image.load("track.png",
	screen_size = (640, 640),
	groups = [cars, road], 
	fs_image = pygame.image.load("Car.png"), 
	fs_pos = (320, 160), #other kinematics left at 0
	fs_groups = 

 
