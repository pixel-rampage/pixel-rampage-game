import pygame

pygame.init()
clock = pygame.time.Clock()
FPS = 60
#create game window
SCREEN_WIDTH = 1230
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("assets\Parallax")


#define game variables
scroll = 0


# images
ground_image = pygame.image.load("assets\Parallax\\aliens_ground_04-modified.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

bg_images = []
for i in range(1, 4):
#   bg_image = pygame.image.load(f"assets\Parallax/{i}.png").convert_alpha()
  bg_image = pygame.image.load(f"assets\Parallax\sky_{i}.png").convert_alpha()
  bg_image = pygame.transform.scale(bg_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
  bg_images.append(bg_image)
bg_width = bg_images[0].get_width()




def draw_bg():
  for x in range(11):
    speed = 1
    for i in bg_images:
      screen.blit(i, ((x * bg_width) - scroll * speed, 0))
      speed += 0.1



def image(direction):
	if direction == "left":
		image = pygame.image.load("assets\\character_animation\\blue\\idle\\idle1.png").convert_alpha()
		image = pygame.transform.scale2x(image)
		image = pygame.transform.flip(image,True,False)
	elif direction == "right":
		image = pygame.image.load("assets\\character_animation\\blue\\idle\\idle1.png").convert_alpha()
		image = pygame.transform.scale2x(image)
	elif direction == "tree":
		image = pygame.image.load("assets\Parallax\Alien_tileset_tree_06.png").convert_alpha()
		# image = pygame.transform.flip(image, True, False)
		# image = pygame.transform.scale2x(image)
	elif direction == "jump" :
		image = pygame.image.load("assets\character animation\jump\jump5.png").convert_alpha()
		image = pygame.transform.scale2x(image)
	elif direction == "land" :
		image = pygame.image.load("assets\Parallax\\aliens_ground_04-modified.png").convert_alpha()
	elif direction == 'door': 
		image = pygame.image.load("assets\Parallax\door_02-modified.png").convert_alpha()
	elif direction == "big_land" :
		image = pygame.image.load("assets\Parallax\\aliens_big_ground_7-modified.png").convert_alpha()
	elif direction == "eater":
		image = []
		for i in range(1,13):
			image.append(pygame.image.load(f"assets\Parallax\eater_{i}-modified.png").convert_alpha())
	elif direction == "flying":
		image = []
		for i in range(1,5):
			image.append(pygame.image.load(f"assets\Parallax\\flying_bot_{i}-modified.png").convert_alpha())
	elif direction == "slime":
		image = []
		for i in range(1,5):
			image.append(pygame.image.load(f"assets\Parallax\slime_{i}-modified.png").convert_alpha())
	return image
	
      
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = image("right")
		self.rect = self.image.get_rect(midbottom=(300, SCREEN_HEIGHT - (ground_height)))
		self.x_velocity = 0
		self.y_velocity = 0
		self.on_ground = True

	def update(self):
		self.x_velocity = 0
		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT]:
			self.x_velocity = -5
			self.image = image("left")
			
			
			
		if keys[pygame.K_RIGHT]:
			self.x_velocity = 5
			self.image = image("right")
			

		# Jumping
		if keys[pygame.K_SPACE] and self.on_ground:
			self.y_velocity = -18
			self.on_ground = False
			# self.image = image("jump")

		# Apply gravity
		self.y_velocity += 0.8

		# Limit the vertical speed
		if self.y_velocity > 10:
			self.y_velocity = 10

		self.rect.x += self.x_velocity
		self.rect.y += self.y_velocity			
			
		# fdsfsdf 
		if self.rect.left < 200 :
			self.rect.left = 200
		# dsfsdf 
		if self.rect.right > 1000 : 
			self.rect.right = 1000
		
class Obstacle(pygame.sprite.Sprite):
	def __init__(self,type,x_pos,y_pos):
		super().__init__()
		
		
		material = image(type)
		self.frames = [material]
		self.y_pos = y_pos
		self.x_pos = x_pos
                        
		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (self.x_pos,self.y_pos))
                
	def update(self):
           #get keypresses
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT] and player.sprite.rect.left < 201 and scroll > 0:
			self.rect.x += 5
		if key[pygame.K_RIGHT] and player.sprite.rect.right > 999 and scroll < 3000:
			self.rect.x -= 5

class Objects_to_draw(pygame.sprite.Sprite):
	def __init__(self,type,x_pos,y_pos):
		super().__init__()
		
		
		material = image(type)
		self.frames = [material]
		self.y_pos = y_pos
		self.x_pos = x_pos
                        
		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (self.x_pos,self.y_pos))
                
	def update(self):
           #get keypresses
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT] and player.sprite.rect.left < 201 and scroll > 0:
			self.rect.x += 5
		if key[pygame.K_RIGHT] and player.sprite.rect.right > 999 and scroll < 3000:
			self.rect.x -= 5




class Monsters(pygame.sprite.Sprite):
	def __init__(self,type,x_pos,y_pos,distance,speed):
		super().__init__()
		
		self.type = image(type)
		self.x_pos = objects.sprites()[x_pos].rect.x           
		self.y_pos = objects.sprites()[y_pos].rect.top
		self.start_point = x_pos
		self.animation_index = 0
		self.state = False
		self.speed = speed
		self.distance = distance
		self.image = self.type[int(self.animation_index)]
		self.rect = self.image.get_rect(bottomleft = (self.x_pos,self.y_pos))

                
	def update(self):
           #get keypresses
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT] and player.sprite.rect.left < 201 and scroll > 0:
			self.rect.x += 5
		if key[pygame.K_RIGHT] and player.sprite.rect.right > 999 and scroll < 3000:
			self.rect.x -= 5
		
        

		self.animation_index += 0.1
		self.image = self.type[int(self.animation_index)]
		if self.animation_index > len(self.type)-1 :
			self.animation_index = 0
		
		self.rect.x += self.speed
		
		
		if self.rect.x <= objects.sprites()[self.start_point].rect.x or self.rect.x >= objects.sprites()[self.start_point].rect.x + self.distance:
			self.speed *= -1  # Reverse the direction
			self.state = not(self.state)
				
		if self.state :
			self.image = pygame.transform.flip(self.image, True,False)

				

			
	

						
def collide():
	for i in range(len(objects.sprites())):
		if objects.sprites()[i].rect.colliderect(player.sprite.rect): 
			if player.sprite.x_velocity < 0  and player.sprite.on_ground == False:
				# player.sprite.rect.left = objects.sprites()[i].rect.right
				player.sprite.x_velocity = 0

			if player.sprite.x_velocity > 0 and player.sprite.on_ground == False:
				# player.sprite.rect.right = objects.sprites()[i].rect.left
				player.sprite.x_velocity = 0


			if player.sprite.y_velocity > 0 : 
				player.sprite.rect.bottom = objects.sprites()[i].rect.top 
				player.sprite.y_velocity = 0 
				player.sprite.on_ground = True

			if player.sprite.y_velocity < 0 : 
				player.sprite.rect.top = objects.sprites()[i].rect.bottom 
				player.sprite.y_velocity = 0
				player.sprite.on_ground = True
		for i in range(len(monsters.sprites())):
			if monsters.sprites()[i].rect.colliderect(player.sprite.rect):
				print('collide')

	    


   
# groups         these groups should be in the level class 

# player
player = pygame.sprite.GroupSingle()
player.add(Player())



# objects that the player collides with
objects = pygame.sprite.Group()
for i in range(3):
	objects.add(Obstacle('land',(ground_width * i), SCREEN_HEIGHT+20))
objects.add(Obstacle('land',1300, SCREEN_HEIGHT-150))
objects.add(Obstacle('land',1820, SCREEN_HEIGHT-320))
objects.add(Obstacle("big_land",2730,SCREEN_HEIGHT+500))
objects.add(Obstacle('land',(ground_width * 10)+20, SCREEN_HEIGHT-220))
for i in range(11,13):
	objects.add(Obstacle('land',(ground_width * i), SCREEN_HEIGHT+20))
objects.add(Obstacle('land',(ground_width * 13)+70, SCREEN_HEIGHT-150))
objects.add(Obstacle('land',(ground_width * 15)-50, SCREEN_HEIGHT-150))
for i in range(16,20):
	objects.add(Obstacle('land',(ground_width * i), SCREEN_HEIGHT+20))

# monsters 
monsters = pygame.sprite.Group()
monsters.add(Monsters('eater',2,2,300,3))
monsters.add(Monsters('eater',3,3,300,4))
monsters.add(Monsters('eater',4,4,300,4))
monsters.add(Monsters('flying',5,5,1000,2))
monsters.add(Monsters('slime',5,5,1000,4))
monsters.add(Monsters('eater',6,6,300,3))
monsters.add(Monsters('flying',7,7,620,2))
monsters.add(Monsters('slime',7,7,620,4))
monsters.add(Monsters('slime',9,9,300,4))
monsters.add(Monsters('eater',10,10,300,3))
monsters.add(Monsters('flying',11,11,500,2))
monsters.add(Monsters('flying',13,13,500,2))
monsters.add(Monsters('slime',11,11,1300,5))




# objects just to be drown
objects_d = pygame.sprite.Group()
objects_d.add(Objects_to_draw('tree',250,SCREEN_HEIGHT-ground_height+20))
objects_d.add(Objects_to_draw('door',(ground_width * 19)+130,SCREEN_HEIGHT - ground_height+20))



		

#game loop
run = True
while run:

	clock.tick(FPS)

	#draw world
	draw_bg()

	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT] and player.sprite.rect.left < 201 and scroll > 0:
		scroll -= 2
	elif key[pygame.K_RIGHT] and player.sprite.rect.right > 999 and scroll < 3000:
		scroll += 2
	
	

	
	objects_d.update()  
	objects_d.draw(screen) 
	objects.update()  
	objects.draw(screen) 
	monsters.update()
	monsters.draw(screen)
	player.update() 
	player.draw(screen) 
	collide()
	

	#event handlers
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()


pygame.quit()