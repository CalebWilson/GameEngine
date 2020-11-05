import pygame

from Track import Track
from Car import Car
from ScrollSprite import ScrollSprite

#establish groups
cars  = pygame.sprite.Group()
roads = pygame.sprite.Group()
walls = pygame.sprite.Group()

#create scene
#Track constructor automatically creates car with default argument values
track = Track (fs_groups = [cars])

#add car to cars
cars.add (track.focus_sprite)

#add roads
def add_road (x, y, angle, image_name):
	roads.add (
		ScrollSprite (
			scene = track,
			image = pygame.image.load (image_name),
			position = (x, y),
			ang_pos = angle,
			tangible = False,
			groups = [roads]
		) #end ScrollSprite()
	) #end roads.add()
#end def add_road()

#elbows
add_road (-80, 200,   0, "ElbowRoad.png") #upper  left
add_road (720, 200,  90, "ElbowRoad.png") #upper  right
add_road (720, 680, 180, "ElbowRoad.png") #bottom right
add_road (-80, 680, 270, "ElbowRoad.png") #bottom left

#straights
#horizontal
for i in range(4):
	add_road (80 + (160 * i), 160, 0, "StraightRoad.png") #top
	add_road (80 + (160 * i), 720, 0, "StraightRoad.png") #bottom

#vertical
for i in range(2):
	add_road (-120, 360 + (160 * i), 90, "StraightRoad.png") #left
	add_road ( 760, 360 + (160 * i), 90, "StraightRoad.png") #right

#add walls
def add_wall (dimensions, center):
	walls.add (
		ScrollSprite (
			scene = track,
			image = pygame.Surface (dimensions),
			position = center,
			tangible = True,
			groups = [walls]
		) #end ScrollSprite
	) #end walls.add
#end def add_wall

add_wall ((1440, 80),  (320, -80)) #top
add_wall ((1440, 80),  (320, 960)) #bottom
add_wall ((80, 1120), (-360, 440)) #left
add_wall ((80, 1120), (1000, 440)) #right

#paint walls black
for wall in walls:
	wall.image.fill((0, 0, 0))

#add groups to track
track.groups = [roads, cars, walls]

#begin the game
track.start()
