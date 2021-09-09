import pygame
import random
import sys


pygame.init()

pygame.display.set_caption("Dodge The Blocks")


height=600
width=800

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
background_color=(0,255,255)

player_size=50
player_post=[width/2,height-2*player_size] #(x,y)format

enemy_size=50
enemy_post=[random.randint(0,width-enemy_size),0]  #we set to 0 (0,width) to make it appear at the top,subtracting to make sure the block stays between the screen
enemy_clone=[enemy_post]
screen=pygame.display.set_mode((width,height))

game_over=False

score=0

clock=pygame.time.Clock()

myfont=pygame.font.SysFont("monospace" ,35)

speed=10

def level_change(score,speed):
	if score < 15 :
		speed=5

	elif score < 25 :
		speed=8
	
	elif score < 50 :
		speed=11

	else:
		speed=14

	return speed

def drop_enemies(enemy_clone): #falling of enemies from the top
	delay = random.random() #pace falling from the top
	if len(enemy_clone) < 25 and delay < 0.1:
		x_post = random.randint(0,width-enemy_size)
		y_post = 0
		enemy_clone.append([x_post,y_post]) #as list is mutable,it will automatically update new value
 

def draw_enemies(enemy_clone): #creating more enemies
	for enemy_post in enemy_clone:
		pygame.draw.rect(screen,red, (enemy_post[0],enemy_post[1],enemy_size,enemy_size))

def update_enemy_position(enemy_clone,score): #updation 
	for idx, enemy_post in enumerate(enemy_clone):
		if enemy_post[1] >= 0 and enemy_post[1] < height: #get checks if enemy is on the screen
			enemy_post[1] +=speed  
		else: #checks if enemy is off the screen
			enemy_clone.pop(idx)
			score +=1
	return score

		    
def collision_check(enemy_clone,player_post): #to check collision
	for enemy_post in enemy_clone:
		if detect_collision(enemy_post,player_post):
			return True
	return False

def detect_collision(player_post,enemy_post):
	p_x=player_post[0]
	p_y=player_post[1]

	e_x=enemy_post[0]
	e_y=enemy_post[1]

	if (e_x >= p_x and e_x < (p_x+player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)) :            #overlappping of x coordinates
		if (e_y >= p_y and e_y < (p_y+player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)) :        #overlapping of y coordinates
			return True
	return False #it comes to false condition when the player block and enemy block doesnt collide

def more_clones(score,enemy_clone):
	if score < 15 :
		enemy_clone = 10

	elif score < 20 :
		enemy_clone = 15

	elif score < 30 :
		enemy_clone = 20

	elif score < 40 :
		enemy_clone = 25

	elif score < 50 :
		enemy_clone = 30

	else:
		enemy_clone = 35

	return score	

#game loop

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			x=player_post[0]
			y=player_post[1]


			if event.key == pygame.K_LEFT:
				x-=35
				pass
			elif event.key == pygame.K_RIGHT: #mentioned elif to prevent other key to get opted
				x+=35
				pass

			player_post=[x,y] #updation
 
	screen.fill((background_color)) #to make the black color follow the movement of the block

	if detect_collision(player_post,enemy_post): #updation of the real enemy
		game_over = True
		break #faster and smoother exit

	
	drop_enemies(enemy_clone)
	score = update_enemy_position(enemy_clone,score)
	speed = level_change(score,speed)
	score = more_clones(score,more_clones)


	text = "Score:" + str(score)
	label= myfont.render(text,1,black)
	screen.blit(label,(width-400,height-40))
	
	if collision_check(enemy_clone,player_post): #updation of the clone enemies
		game_over = True
		break

	draw_enemies(enemy_clone)

	pygame.draw.rect(screen,white,(player_post[0],player_post[1],player_size,player_size))

	clock.tick(30)
	

	pygame.display.update()
	
	


