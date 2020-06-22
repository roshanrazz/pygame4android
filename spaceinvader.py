import pygame
import random as rd
from pygame import mixer

pygame.init()


screen=pygame.display.set_mode((940,2200))

pygame.display.set_caption('space invadors')

icon=pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

bltstate='ready'

game_start=False

def start_screen():
	startscreen=pygame.image.load('startscreen.jpg')
	startgame=pygame.image.load('rocket.png')
	quitgame=pygame.image.load('close.png')
	screen.blit(startscreen,(0,0))
	screen.blit(startgame,(100,800))
	screen.blit(quitgame,(730,800))
	txt=pygame.font.Font(None,88)
	text1=txt.render('Click on SPACESHIP to start game',True,(25,246,46))
	text2=txt.render('         or CROSS to quit game',True,(25,246,23))
	dev=txt.render('Developed By',True,(25,255,12))
	dev2=txt.render('Roshan Razz',True,(15,255,0))
	screen.blit(dev,(600,1800))
	screen.blit(dev2,(600,1900))
	screen.blit(text1,(20,200))
	screen.blit(text2,(20,300))
	try:
		f=open('highscore.txt','r')
		hs=f.read()
		f.close()
	except:
		hs=0
	finally:
		text3=txt.render(f'High Score : {hs}',True,(214,241,123))
		screen.blit(text3,(300,500))
	
	while True:
		for event in pygame.event.get():
			if event.type==pygame.MOUSEBUTTONDOWN:
				mpos=pygame.mouse.get_pos()
				x,y=mpos
				if (x>50 and x<300) and (y>680 and y<950):
		
					playgame()
				elif (x>580 and x<900) and (y>680 and y<950):
					quit()
		
		pygame.display.update()
	
	
def playgame():
	global bltstate
	shipimg=pygame.image.load('space-invaders.png')
	shipx,shipy=(465,1800)
	shipchange=0

	def ship(x,y):
		
		screen.blit(shipimg,(x,y))
		
	enm=[]
	enmx=[]
	enmy=[]
	enmxchange=4
	enmychange=1
	for i in range (6):
			
		enm.append(pygame.image.load('alien.png'))
		enm.append(pygame.image.load('ufo.png'))
		enmx.append(rd.randint(0,940))
		enmy.append(rd.randint(60,820))
	
	bckimg=pygame.image.load('bgr.jpg')
	
	def enemy(x,y,i):
			screen.blit(enm[i],(x,y))
		
	blt=pygame.image.load('bullet.png')
	bltx,blty=0,1800
	bltchange=0
	
	def bullet(x,y):
		global bltstate
		bltstate='fire'
		screen.blit(blt,(x+30,y-20))
	
	score=0
	kill=0
	level=1
	target=5
	
	font=pygame.font.Font(None,65)
	
	def display_score():
		
		kil=font.render(f'Killed : {kill}',True,(0,255,255))
		lvl=font.render(f'Level : {level}',True,(0,255,255))
		trgt=font.render(f'Kill {target} Enemies',True,(0,255,255))
		screen.blit(kil,(10,10))
		screen.blit(lvl,(800,10))
		screen.blit(trgt,(330,10))
	
	font_game=pygame.font.Font(None,230)
	play_again=pygame.font.Font(None,100)
	hscr=pygame.font.Font(None,130)
	
	def display_over():
		def nhs(x):
			newhighscr=hscr.render(f'{x}: {hs} ',True,(14,215,255))
			screen.blit(newhighscr,(200,480))
		
		try:
			f=open('highscore.txt','x')
			f.close()
		except:
			pass
		finally:
			f=open('highscore.txt','r+')
			try:
				hs=int(f.read())
			except:
				hs=0
			f.close()
			f=open('highscore.txt','r+')
			if score>hs:
				hs=score
				f.write(str(score))
			
			if score<hs:
				nhs('High Score ')
			else:
				nhs('New High Score ')
				
			f.close()
			
		over=font_game.render('Game Over',True,(0,255,0))
		scr=play_again.render(f'Your Score : {score}',True,(146,246,143))
		screen.blit(over,(130,200))
		screen.blit(scr,(285,650))
		
		mixer.music.load('nomusic.ogg')
		mixer.music.play()
		plag=play_again.render('Do You Want To Play Again?',True,(0,255,22))
		screen.blit(plag,(100,900))
		yes=pygame.image.load('yes.png')
		no=pygame.image.load('close2.png')
		screen.blit(yes,(350,1060))
		screen.blit(no,(650,1060))
	
	mixer.music.load('backgroundmusic.mp3')
	mixer.music.play(-1)
	
	game_over=False

	left=pygame.image.load('back.png')
	right=pygame.image.load('next.png')
	bltbtn=pygame.image.load('bullet2.png')
	
	while True:
		
		screen.fill((0,0,0))
		screen.blit(bckimg,(0,0))
		screen.blit(left,(10,2100))
		screen.blit(right,(950,2100))
		screen.blit(bltbtn,(465,2100))
	
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				False
			if event.type==pygame.MOUSEBUTTONDOWN:
				pos=pygame.mouse.get_pos()
				x,y=pos
				if (x>0 and x<150) and (y>2000 and y<2300) and shipx>30:
					shipchange=-30
					
				elif (x>850 and x<1100) and (y>2000 and y<2300) and shipx<910:
					shipchange=30
	
				elif game_over and (x>250 and x<450) and (y>960 and y<1160):
					playgame()
				
				elif game_over and (x>550 and x<750) and (y>960 and y<1160):
					quit()

				else:
					shipchange=0
					
				if (x>265 and x<700) and (y>1800 and y<2300) and not game_over:
					if bltstate is 'ready':
						bltsound=mixer.Sound('shoot.wav')
						bltsound.play()
						bltx=shipx
						bullet(bltx,blty)
					
			shipx+=shipchange		
		for i in range(6):
			if enmx[i]>940:
				while not enmx[i]<0:
					enmx[i]=enmx[i]-enmxchange
			else:
				enmx[i]+=enmxchange
				enmy[i]+=enmychange
			
			killdist=((enmx[i]-bltx)**2+(enmy[i]-blty)**2)**(1/2)
		
			if killdist<90:
				enmsound=mixer.Sound('explosion.wav')
				enmsound.play()
				blty=1800
				bltstate='ready'
				bltchange=0
				enmx[i],enmy[i]=rd.randint(20,940),rd.randint(60,820)
				score+=1
				kill+=1
				if kill==target:
					target=target+5
					level=level+1
					kill=0

					enmxchange+=2
					enmychange+=1
			elif enmy[i]>1700:
				game_over=True
				display_over()
				
				for j in range(6):
					enmx[j],enmy[j]=3000,3000
				break
			else:
				pass
			enemy(enmx[i],enmy[i],i)
			
		
		blty+=bltchange	
		ship(shipx,shipy)
		if bltstate is 'fire':
			bltchange=-35
			bullet(bltx,blty)
			
		if blty<150:
			bltstate='ready'
			bltchange=0
			blty=1800
	
		else:
			pass
			
		if not game_over:
				
			display_score()

		pygame.display.update()	

if not game_start:
	start_screen()

if game_start:		
	playgame()