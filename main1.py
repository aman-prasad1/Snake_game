import pygame
import random

pygame.init()

#COLORS
white = [255 , 255 , 255]
red = [255 , 0 ,0]
black = [0 , 0 ,0]
blue =[0 , 0 , 255]

gameWindow = pygame.display.set_mode()

bg_image = pygame.image.load('background.jpg')

font = pygame.font.SysFont(None, 55)

clock = pygame.time.Clock()

#TO DISPLAY TEXT ON SCREEN
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
    
    
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

#GAME LOOP
def mainloop():
	exit_game = False
	game_over = False
	music_play = False
	snake_x = 350
	snake_y = 312
	snake_size = 20
	
	velocity_x = 0
	velocity_y = 0
	
	width = 350
	height = 625
	
	speed = 5
	inc_speed = 0
	fps = 45
	score = 0
	with open("highscore.txt",'r') as f:
		hiscore = f.read()	
	food_x = random.randrange(10,width)
	food_y = random.randrange(10,height-20)
	
	snk_list = []
	snk_length = 1

	while not exit_game:
		if game_over==True:
			gameWindow.fill(black)
			text_screen("HIGH SCORE: "+str(hiscore), red,210,250)
			text_screen("YOUR SCORE- "+str(score), red,210,312)
			text_screen("GAME OVER.  PRESS BACKSPACE ", red , 50 , 390 )
			text_screen("TO RESTART",red,230,450)
			with open("highscore.txt",'w') as f:
				f.write(str(hiscore))
				
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					exit_game = True
				else:
					if event.type==pygame.KEYDOWN:
						if event.key==pygame.K_BACKSPACE:
								mainloop()
		else:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					exit_game = True
				if event.type==pygame.KEYDOWN:
					if event.key ==pygame.K_d or event.key == pygame.K_RIGHT:
						snake_x = snake_x +10
						velocity_x = speed
						velocity_y = 0
			
					if event.key == pygame.K_a or event.key == pygame.K_LEFT:
						snake_x = snake_x -10
						velocity_x = -speed
						velocity_y = 0
					if event.key == pygame.K_w or event.key == pygame.K_UP:
						snake_y = snake_y -10
						velocity_y = -speed
						velocity_x = 0
					if event.key == pygame.K_s or event.key == pygame.K_DOWN:
						snake_y = snake_y +10
						velocity_y = speed
						velocity_x = 0
				
					
			#gameWindow.fill(black)
			gameWindow.blit(bg_image,(0,0))
			#WHEN SNAKE TOUCH BOUNDARY
			if (snake_x < 0 or snake_y< 0):
				game_over = True
				pygame.mixer.init()
				pygame.mixer.music.load('gameover1.mp3')
				pygame.mixer.music.play()
			if (snake_x > 710 or snake_y > 635):
				game_over = True
				pygame.mixer.init()
				pygame.mixer.music.load('gameover1.mp3')
				pygame.mixer.music.play()
						
			pygame.draw.rect(gameWindow,red,[5,5,710,650],5)
				
				
			if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:
				pygame.mixer.init()
				pygame.mixer.music.load("point.ogg")
				pygame.mixer.music.play()
				food_x = random.randrange(20,width,20)
				food_y = random.randrange(20,height,20)
				score += 10
				inc_speed += 1
				snk_length += 5
				if score>int(hiscore):
					hiscore = score
					
				
		 #	if inc_speed == 1:
   #	speed += 1
   # inc_speed = 0
				
			text_screen("Score: " + str(score)+" High score: "+str(hiscore), red, 5, 5)
				
			pygame.draw.rect(gameWindow , blue , [food_x , food_y,snake_size,snake_size])
				
				
			snake_x += velocity_x
			snake_y += velocity_y
				
			head = []
			head.append(snake_x)
			head.append(snake_y)
			snk_list.append(head)
			if len(snk_list)>snk_length:
				del snk_list[0]
			plot_snake(gameWindow,white, snk_list, snake_size)
			if head in snk_list[:-1]:
				game_over = True
				pygame.mixer.init()
				pygame.mixer.music.load('gameover1.mp3')
				pygame.mixer.music.play()
		pygame.display.update()
		clock.tick(fps)
		
	pygame.quit()
	quit()

mainloop()
	