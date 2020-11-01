import Track
import Car

cars  = pygame.sprite.Group()
roads = pygame.sprite.Group()
walls = pygame.sprite.Group()

track = Track (
	image = pygame.image.load("Track.png"),
	screen_size = (640, 640),
	fs_image = pygame.image.load("Car.png"), 
	fs_pos = (320, 160), #other kinematics left at 0
	fs_groups = [cars]
)

#add car to cars
cars.add (track.focus_sprite)

#add elbow roads
roads.add (
	[
		#upper left elbow
		ScrollSprite (
			scene = track,
			image = pygame.image.load ("ElbowRoad.png"),
			position = ,#TODO:insert position here
			ang_pos = 0,
			tangible = False,
			groups = [roads]
		),

		#upper right elbow
		ScrollSprite (
			scene = track,
			image = pygame.image.load ("ElbowRoad.png"),
			position = ,#TODO:insert position here
			ang_pos = 90,
			tangible = False,
			groups = [roads]
		),

		#bottom right elbow
		ScrollSprite (
			scene = track,
			image = pygame.image.load ("ElbowRoad.png"),
			position = ,#TODO:insert position here
			ang_pos = 180,
			tangible = False,
			groups = [roads]
		),

		#bottom left elbow
		ScrollSprite (
			scene = track,
			image = pygame.image.load ("ElbowRoad.png"),
			position = ,#TODO:insert position here
			ang_pos = 270,
			tangible = False,
			groups = [roads]
		),
	]
) #end roads.add()

#add top roads
for i in range(): #TODO:insert width here
	roads.add (
		ScrollSprite (
			scene = track,
			image = pygame.image.load ("StraightRoad.png"),
			position = + ( * i) #TODO:insert initial position and image width
			ang_pos = 0,
			tangible = False,
			groups = [roads]
		)
	) #end roads.add

#end for each top road

#add bottom roads
for i in range(): #TODO:insert width here
	roads.add (
		ScrollSprite (
			scene = track,
			image = pygame.image.load ("StraightRoad.png"),
			position = + ( * i) #TODO:insert initial position and image width
			ang_pos = 0,
			tangible = False,
			groups = [roads]
		)
	) #end roads.add

#end for each bottom road

#add left roads
for i in range(): #TODO:insert height here
	roads.add (
		ScrollSprite (
			scene = track,
			image = pygame.image.load ("StraightRoad.png"),
			position = + ( * i) #TODO:insert initial position and image width
			ang_pos = 90,
			tangible = False,
			groups = [roads]
		)
	) #end roads.add

#end for each left road

#add right roads
for i in range(): #TODO:insert height here
	roads.add (
		ScrollSprite (
			scene = track,
			image = pygame.image.load ("StraightRoad.png"),
			position = + ( * i) #TODO:insert initial position and image width
			ang_pos = 90,
			tangible = False,
			groups = [roads]
		)
	) #end roads.add

#end for each right road

#add top wall

