#Chill n Soy.py
#By Norman and Ben

from pygame import *
from pygame.mixer import *
from pygame import *
from random import *



init()
mixer.init()

display.set_caption("Chilli' n Soy")

transition="Menu"

size = width, height =1280,720

screen = display.set_mode(size)

BLUE=(0,0,255)
GROUND=height
BLACK=(0,0,0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
GREEN=(0,255,0)

TUR=(106,214,247)

lives=3

font=font.SysFont(None,25)

background=image.load("background/intro.png").convert()
background=transform.scale(background,(1280,720))

introkeyss=image.load("instruction_keys.png")

#characters
HOTOIL=[210,450,102,108, 0, 0]
SOY=[20,450,150, 150, 0, 0]
#variables that represent items in the code...
jumpSpeed = -45 #jump power
gravity =4    #gravity
GROUND = 720
bottom = GROUND
playerRect1=0
playerRect2=1

X=0
Y=1
W=2
H=3

BOT=2

grav=1.2

X2=0
Y2=1
W2=2
H2=3

BOT2=2

ROW=4
COL=5

SCREENX=3

v=[0,0,bottom,200]
v2=[0,0,bottom,200]

gif=[image.load("gif/1.png"),image.load("gif/2.png"),image.load("gif/3.png"),image.load("gif/4.png"),
     image.load("gif/5.png"),image.load("gif/6.png")]
lol=0
#-----------------------------images and loading them-------------------------------------------------
m1=["Museback/s1.mp3","Museback/evil.mp3","Museback/menu.mp3","Museback/lost.mp3","Museback/l1.mp3","Museback/happy.mp3"
    ,"Museback/s2.mp3","Museback/s3.mp3","Museback/cred.mp3"]
back=image.load("background/n.png").convert()
mixer.music.load(m1[2])
mixer.music.play(-1)
b=(0,0,0)
c=(0,0,0)
jumping=False

#-------------------------------------------------------------------------------------------------------------
def tutorial_instruct(m,colour):
          screen_text=font.render(m,True,colour)
          screen.blit(screen_text,[10,40])

          
#------------------------------The transitions to the game--------------------------------------------------

def menu():
    global transition#I implemented the function becausewe need to transition between different scenes of the game
    #the function global works like this, variables inside a function are local and cannot be accessed from the ouside code,
    #by using global Keyword we can call on the specified function, for this game we need to transition between levels and menu screen
    #using global transition in this code everytime i make a level and put it in i can later on make if statements calling the "public" word (transition) to call on other functions to open
    # like calling if transition=="Menu":  menu() which means that it's going to run the function menu() which shows the menu screen because
    #the transition was already applied as "Menu" above. Also, if a button was pressed on the menu screen it would bring you to the next level using
    #the global transition will now be defined as the next level instead of "Menu" this is how you change a open variable in a function that only creates LOCAL variable that only work in that function
    #I found this wordkey while reasearching how to change screen on python on many websites, this one shows the different rules for global :
    #https://www.geeksforgeeks.org/global-keyword-in-python/
    menuB=image.load("background/MenuBack.png").convert()  
    menuB=transform.scale(menuB,(1280,720))
    screen.blit(menuB,(0,0))

    button_start=Rect(50,150,350,130)
    
    if button_start.collidepoint(mx,my) and mp:
        transition="story"        #"level1"
        mixer.music.load(m1[6])
        #mixer.music.play()          
    button_instructions=Rect(50,300,385,45)

    if button_instructions.collidepoint(mx,my) and mp:
        transition="intro"
        mixer.music.load(m1[0])
        mixer.music.play(-1)
    button_credit=Rect(150,380,365,87)

    if button_credit.collidepoint(mx,my) and mp:
        transition="credits"
        mixer.music.load(m1[8])
        mixer.music.play(-1)



def drawSceneMain():
    global b
    global c
    for plat in plats:
        draw.rect(screen, WHITE, plat)
    row=HOTOIL[ROW]
    col=int(HOTOIL[COL])
    pic=p[row][col]
    screen.blit(pic,(HOTOIL[X],HOTOIL[Y]))
    b=draw.rect(screen, WHITE, HOTOIL[:4], 2)
       
    row2=SOY[ROW]
    col2=int(SOY[COL])
    pic2=p2[row2][col2]
    screen.blit(pic2,(SOY[X],SOY[Y]))
    c=draw.rect(screen, RED, SOY[:4], 2)
    display.flip()


#-------------------------------all the scenes that will be transitioned-----------------------
def story():
    global transition
    screen.fill((0,0,0))
    storyy=image.load("story/story1.png").convert()
    storyy=transform.scale(storyy,(1280,720))
    screen.blit(storyy,(0,0))
    button_continue=Rect(915,650,362,130)
    if button_continue.collidepoint(mx,my) and mp:
        transition="story2"
        mixer.music.load(m1[1])
        #mixer.music.play(-1)

        
def story2():
    global transition
    screen.fill((0,0,0))
    storyy=image.load("story/story2.png").convert()
    storyy=transform.scale(storyy,(1280,720))
    screen.blit(storyy,(0,0))
    button_continue=Rect(980,662,362,150)
    if button_continue.collidepoint(mx,my) and mp:
        transition="story3"
        mixer.music.load(m1[3])
        #mixer.music.play(-1)

        
def story3():
    global transition
    screen.fill((0,0,0))
    storyy=image.load("story/story3.png").convert()
    storyy=transform.scale(storyy,(1280,720))
    screen.blit(storyy,(0,0))
    button_continue=Rect(945,650,362,130)
    if button_continue.collidepoint(mx,my) and mp:
        transition="decide"
        mixer.music.load(m1[4])
        mixer.music.play(-1)

 #---------------------------------------------------------------------Tutorial---------------------------------------------------------------------------  
def intro():
    global transition
    global playerRect1
    global playerRect2
    screen.blit(background,(0,0))
    screen.blit(introkeyss,(255,40))
    portal(1050,80)
    movePlayer1(HOTOIL)
    Jump1(HOTOIL)
    check(HOTOIL, plats)
    movePlayer2(SOY)
    Jump2(SOY)
    check2(SOY, plats)
    drawSceneMain()
    
        
    tutorial_instruct("Use the arrow keys to control Chilli King and A W D to control Soy Queen. Up only to dance, (P) to pause game",TUR)
    pb=Rect(1100,80,200,220)#area of the portal to level 1
    if pb.colliderect(b) and pb.colliderect(c):
        transition="story"
        HOTOIL[0]=210
        HOTOIL[1]=450
        mixer.music.load(m1[6])
        #mixer.music.play()

def decide():
    global transition
    screen.fill((0,0,0))
    deciding=image.load("story/decide.png").convert()
    deciding=transform.scale(deciding,(1280,720))
    screen.blit(deciding,(0,0))
    button_continue=Rect(470,205,380,100)
    button_stop=Rect(470,370,380,100)
    if button_continue.collidepoint(mx,my) and mp:
        transition="level2"
        mixer.music.load(m1[6])
        mixer.music.play(-1)
    elif button_stop.collidepoint(mx,my) and mp:
        transition="pog"
        
def pog():
    global transition
    screen.fill((0,0,0))
    pogchamp=image.load("story/pogchamp.png").convert()
    pogchamp=transform.scale(pogchamp,(1280,720))
    screen.blit(pogchamp,(0,0))
    button_stop=Rect(0,0,1280,720)
    if button_stop.collidepoint(mx,my) and mp:
        quit()
back=image.load("background/n.png").convert()
Cback=image.load("Masking/colorN.bmp").convert()
Bback=image.load("Masking/colorJupiter.bmp")
life=[image.load("gif/h0.png"),image.load("gif/h1.png"),image.load("gif/h2.png"),image.load("gif/h3.png")]

b=draw.rect(screen, WHITE, HOTOIL[:4], 2)

def L1():
    global wallS
    global wallA
    global transition
    global offset

    wallS=(245,255,0,255)#getting the collision colour for spikes
    wallA=(255,27,0,255)
    colourCollision1(HOTOIL)
    drawScene1(screen,HOTOIL)
    drawsceneForLevel1()
    movePlayerLEVEL1(HOTOIL)
    jump1(HOTOIL)
    check(HOTOIL,stepspace)
    if Cback.get_at((HOTOIL[0],HOTOIL[1]))==wallA \
       or Cback.get_at((HOTOIL[0]+140,HOTOIL[1]))==wallA\
       or Cback.get_at((HOTOIL[0]+140,HOTOIL[1]+100))==wallA\
       or Cback.get_at((HOTOIL[0],HOTOIL[1]+100))==wallA\
       or Cback.get_at((HOTOIL[0],HOTOIL[1]+137))==wallA\
       or Cback.get_at((HOTOIL[0]+70,HOTOIL[1]+137))==wallA\
       or Cback.get_at((HOTOIL[0]+160,HOTOIL[1]+137))==wallA:
        transition="level2"
        lives=3
        HOTOIL[0]=210
        HOTOIL[1]=450
        mixer.music.load(m1[6])
        mixer.music.play()
    display.flip()
back2=image.load("background/n.png").convert()
Cback2=image.load("Masking/colorJupiter.bmp").convert()


def L2():
    global wallS2
    global transition
    global offset
    wallS2=(254,255,0,255)
    wallA2=(255,27,0,255)
    colourCollision2(HOTOIL)
    drawScene2(screen,HOTOIL)
    drawsceneForLevel2()
    movePlayerLEVEL2(HOTOIL)
    jump1(HOTOIL)
    check(HOTOIL,steping2)
    if Cback.get_at((HOTOIL[0],HOTOIL[1]))==wallA2 \
       or Bback.get_at((HOTOIL[0]+140,HOTOIL[1]))==wallA2\
       or Bback.get_at((HOTOIL[0]+140,HOTOIL[1]+100))==wallA2\
       or Bback.get_at((HOTOIL[0],HOTOIL[1]+100))==wallA2\
       or Bback.get_at((HOTOIL[0],HOTOIL[1]+137))==wallA2\
       or Bback.get_at((HOTOIL[0]+70,HOTOIL[1]+137))==wallA2\
       or Bback.get_at((HOTOIL[0]+160,HOTOIL[1]+137))==wallA2:
        transition="level3"
        lives=3
        HOTOIL[0]=210
        HOTOIL[1]=450
        mixer.music.load(m1[6])
        mixer.music.play()

def L3():
    global wallS3
    global wallA3
    global transition
    global offset
    life()
    wallS3=(254,255,0,255)
    wallA3=(255,27,0,255)
    colourCollision3(HOTOIL)
    drawScene3(screen,HOTOIL)
    drawsceneForLevel3()
    move(HOTOIL)
    jump1(HOTOIL)
    check(HOTOIL,stepspace)
    if Cback.get_at((HOTOIL[0],HOTOIL[1]))==wallA \
       or Cback.get_at((HOTOIL[0]+140,HOTOIL[1]))==wallA\
       or Cback.get_at((HOTOIL[0]+140,HOTOIL[1]+100))==wallA\
       or Cback.get_at((HOTOIL[0],HOTOIL[1]+100))==wallA\
       or Cback.get_at((HOTOIL[0],HOTOIL[1]+137))==wallA\
       or Cback.get_at((HOTOIL[0]+70,HOTOIL[1]+137))==wallA\
       or Cback.get_at((HOTOIL[0]+160,HOTOIL[1]+137))==wallA:
        transition="level3"
        HOTOIL[0]=210
        HOTOIL[1]=450
        mixer.music.load(m1[6])
        mixer.music.play()
  
def creditss():
    print("THE END")
    
#####################################################     coulour collision    ################################################

def colourCollision1(p):
    global offset
    global HOTOIL
    global SOY
    global lives
    print(Cback.get_at((p[0],p[1])),wallS)
    if Cback.get_at((p[0],p[1]))==wallS \
       or Cback.get_at((p[0]+140,p[1]))==wallS\
       or Cback.get_at((p[0]+140,p[1]+100))==wallS\
       or Cback.get_at((p[0],p[1]+100))==wallS\
       or Cback.get_at((p[0],p[1]+137))==wallS\
       or Cback.get_at((p[0]+70,p[1]+137))==wallS\
       or Cback.get_at((p[0]+120,p[1]+137))==wallS:
        print("collision")
        lives-=1
        p[0]=210
        p[1]=450
def colourCollision2(p):
    global offset
    global HOTOIL
    global lives
    print(Cback2.get_at((p[0],p[1])),wallS2)
    if Cback.get_at((p[0],p[1]))==wallS2 \
       or Bback.get_at((p[0]+140,p[1]))==wallS2\
       or Bback.get_at((p[0]+140,p[1]+100))==wallS2\
       or Bback.get_at((p[0],p[1]+100))==wallS2\
       or Bback.get_at((p[0],p[1]+137))==wallS2\
       or Bback.get_at((p[0]+70,p[1]+137))==wallS2\
       or Bback.get_at((p[0]+120,p[1]+137))==wallS2:
        print("collision")
        lives-=1
        p[0]=210
        p[1]=450

def colourCollision3(p):
    global offset
    global HOTOIL
    global lives
    print(Cback.get_at((p[0],p[1])),wallS3)
    if Cback.get_at((p[0],p[1]))==wallS2 \
       or Cback.get_at((p[0]+140,p[1]))==wallS3\
       or Cback.get_at((p[0]+140,p[1]+100))==wallS3\
       or Cback.get_at((p[0],p[1]+100))==wallS3\
       or Cback.get_at((p[0],p[1]+137))==wallS3\
       or Cback.get_at((p[0]+70,p[1]+137))==wallS3\
       or Cback.get_at((p[0]+120,p[1]+137))==wallS3:
        print("collision")
        lives-=1
        p[0]=210
        p[1]=450



plats=[Rect(0, 700, width, 50),
            Rect(125, 650, width-125, 50),
            Rect(250, 600, width-250, 50),
            Rect(375, 550, width-375, 50),
            Rect(500, 500, width-500, 50),
            Rect(625, 450, width-625, 50),
            Rect(750, 400, width-750, 50),
            Rect(875, 350, width-875, 50),
            Rect(1000, 300, width-1000, 50),
            Rect(-1280, 0, width, height),
            Rect(1280, 0, width, height)]

step=4
def Jump1(p):
    'moving the player'
    keys = key.get_pressed()
    if keys[K_UP] and p[Y] + p[H] == v[BOT] and v[Y] == 0:    
        v[Y] = jumpSpeed
       # player must be "sitting steady" on
    #a platform/ground in order to jump
    #to move p
    p[X] += v[X] #moving left/right
    v[Y] += gravity #acceleration


def movePlayer1(player):
    keys = key.get_pressed()
    if keys[K_LEFT] and hitside1(player[X]-step,player[Y],plats)==-1:                                                            
        player[X] -= step
        player[ROW]=1
        player[X]-=2
       
    elif keys[K_RIGHT] and hitside1(player[X]+step,player[Y],plats)==-1:                                                              
        player[X] += step
        player[ROW]=0
        player[X]+=2
       
    elif keys[K_UP]:
        player[ROW]=2
        player[Y]-=2

    else:
        player[COL]=0 #"idle" (standing) position
        player[COL]=player[COL]-0.2 #below this line of code we are adding 0.2
               
    player[COL]=player[COL]+0.2 #advancing to the "next" frame

    if player[COL]>=6:#len(p[ROW]):
        player[COL]=1

def movePlayerLEVEL1(player):
    keys = key.get_pressed()
    if keys[K_LEFT] and hitside1(player[X]-step,player[Y],stepspace)==-1:                                                            
        player[X] -= step
        player[ROW]=1
        player[X]-=2
       
    elif keys[K_RIGHT] and hitside1(player[X]+step,player[Y],stepspace)==-1:                                                              
        player[X] += step
        player[ROW]=0
        player[X]+=2
       
    elif keys[K_UP]:
        player[ROW]=2
        player[Y]-=2

    else:
        player[COL]=0 #"idle" (standing) position
        player[COL]=player[COL]-0.2 #below this line of code we are adding 0.2
               
    player[COL]=player[COL]+0.2 #advancing to the "next" frame

    if player[COL]>=6:#len(p[ROW]):
        player[COL]=1
def movePlayerLEVEL2(player):
    keys = key.get_pressed()
    if keys[K_LEFT] and hitside1(player[X]-step,player[Y],stepspace)==-1:                                                            
        player[X] -= step
        player[ROW]=1
        player[X]-=2
       
    elif keys[K_RIGHT] and hitside1(player[X]+step,player[Y],stepspace)==-1:                                                              
        player[X] += step
        player[ROW]=0
        player[X]+=2
       
    elif keys[K_UP]:
        player[ROW]=2
        player[Y]-=2

    else:
        player[COL]=0 #"idle" (standing) position
        player[COL]=player[COL]-0.2 #below this line of code we are adding 0.2
               
    player[COL]=player[COL]+0.2 #advancing to the "next" frame

    if player[COL]>=6:#len(p[ROW]):
        player[COL]=1        
def check(p, plats):
    for plat in plats:
        'check if the player "lands" on a platform'
        if p[X]+p[W]>plat[X] and p[X]<plat[X]+plat[W] and p[Y]+p[H]<=plat[Y] and p[Y]+p[H]+v[Y]>plat[Y]:

            v[BOT] = plat[Y]
            p[Y] = v[BOT] - p[H]
            v[Y] =0
           
    p[Y] += v[Y]#falling down      
   
    if p[Y]+p[H] >= GROUND:# if the player attempts to fall below the ground
        v[BOT] = GROUND
        p[Y] = GROUND - p[H]
        v[Y] = 0

       
def Jump2(p2):
    'moving the player'
    keys = key.get_pressed()

    if keys[K_w] and p2[Y2] + p2[H2] == v2[BOT2] and v2[Y2] == 0:    
        v2[Y2] = jumpSpeed           # player must be "sitting steady" on
                                   #a platform/ground in order to jump
    # move p2
    p2[X2] += v2[X2] #moving left/right
    v2[Y2] += gravity #acceleration


def movePlayer2(player2):
    keys = key.get_pressed()
    if keys[K_a] and hitside2(player2[X2]-step,player2[Y2],plats)==-1:                                                            
        player2[X2] -= step
        player2[ROW]=1
        player2[X]-=2
    elif keys[K_d] and hitside2(player2[X2]+step,player2[Y2],plats)==-1:                                                              
        player2[X2] += step
        player2[ROW]=0
        player2[X]+=2
    elif keys[K_w]:
        player2[ROW]=2
        player2[Y]-=2
       
    else:
        player2[COL]=0 #"idle" (standing) position
        player2[COL]=player2[COL]-0.2 #below this line of code we are adding 0.2

    player2[COL]=player2[COL]+0.2 #advancing to the "next" frame

    if player2[COL]>=6:#len(p[ROW]):
        player2[COL]=1


def check2(p2, plats):
    for plat in plats:
        'check if the player "lands" on a platform'
        if p2[X2]+p2[W2]>plat[X2] and p2[X2]<plat[X2]+plat[W2] and p2[Y2]+p2[H2]<=plat[Y2] and p2[Y2]+p2[H2]+v2[Y2]>plat[Y2]:
            v2[BOT2] = plat[Y2]
            p2[Y2] = v2[BOT2] - p2[H2]
            v2[Y2] =0
       
    p2[Y2] += v2[Y2]#falling down
   
    if p2[Y2]+p2[H2] >= GROUND:# if the player attempts to fall below the ground
        v2[BOT2] = GROUND
        p2[Y2] = GROUND - p2[H2]
        v2[Y2] = 0


def portal(a,b):
    global lol #so we can change open files, this is a public file that cannot be used outside of function. Global let's u do the opposite.
    if lol>=5:
        lol=0
    screen.blit(gif[lol],(a,b))
    lol+=1
    #display.update()
    
def addPics(name,start,end):
          mypics=[]
          for i in range(start,end+1):
                    mypics.append(image.load("sprites/player 1/%s%03d.png"%(name,i)))
          return mypics

p=[]
p.append(addPics("hotoil",0,9))#right
p.append(addPics("hotoil",10,19))#left
p.append(addPics("hotoil",20,26))#right jump


def addPics2(name,start,end):
          mypics=[]
          for i in range(start,end+1):
                    mypics.append(image.load("sprites/player 2/%s%03d.png"%(name,i)))
          return mypics
        
p2=[]
p2.append(addPics2("soy",0,6))#right
p2.append(addPics2("soy",7,13))#left
p2.append(addPics2("soy",14,20))#right jump


def hitside1(x,y,plats):
    playerRect=Rect(x,y,98,104)  #player's rect
    return playerRect.collidelist(plats)


def hitside2(x,y,plats):
    playerRect=Rect(x,y,120,150)  #player's rect
    return playerRect.collidelist(plats)

#-----------------------------------------------------------------------LEVEL 1-------------------------------------------------------
neptune=image.load("background/n.png").convert()

rocket = image.load("background/rocket.png")
rocket = transform.scale(rocket, (400, 700))
stepspace = (Rect(200, 680, 380, 40),# first plat
             Rect(600, 600, 160, 50),
             Rect(840, 530, 350, 40),
             Rect(1280, 535, 320, 200),
             Rect(1730,440, 140, 40),
             Rect(1780, 655, 160, 40),
             Rect(2050, 690, 300, 30),
             Rect(2425, 625, 150, 50),
             Rect(2480, 575, 50, 150),
             Rect(2610,  440, 50, 150),
             Rect(2700, 360, 150, 50),
             Rect(2750, 310, 50, 150),
             Rect(2550, 500, 150, 50))

steping2 = (Rect(0, 560, 630, 260), # first plat
            Rect(780, 560, 170, 230),
            Rect(1170, 560, 170, 230),
            Rect(1440, 630, 200, 40),
            Rect(1635, 545, 55, 40),
            Rect(1830, 670, 200, 50),
            Rect(2100, 510, 410, 40),
            Rect(2080, 700, 1100, 21),
            Rect(3050, 620, 65, 40),
            Rect(3260, 615, 65, 45),
            Rect(3325, 565, 65, 40),
            Rect(3395, 520, 60, 45),
            Rect(3400, 675, 180, 40),
            Rect(3550, 480, 60, 45),
            Rect(3615, 430, 60, 45),
            Rect(3690, 675, 180, 40),
            Rect(3760, 380, 60, 45),
            Rect(3935, 375, 60, 45),
            Rect(4125, 315, 50, 40),
            Rect(4165, 675, 314, 55),
            Rect(4430, 630, 155, 50),
            Rect(4485, 590, 145, 40),
            Rect(4580, 540, 335, 45),
            Rect(4630, 500, 300, 50),
            Rect(4725, 450, 100, 50),
            Rect(4980, 675, 310, 50),
            Rect(5450, 680, 370, 41),
            Rect(5565, 490, 200, 10),
            Rect(6010, 675, 390, 55),
            Rect(6385, 630, 195, 40),
            Rect(6590, 550, 145, 35),
            Rect(6855, 545, 100, 20),
            Rect(7080, 540, 100, 20),
            Rect(7290, 540, 100, 20),
            Rect(7525, 500, 100, 20),
            Rect(7745, 425, 100, 20),
            Rect(7990, 455, 400, 150))
#new variables
a=[0,0,bottom,200]
stageX = 3

offset=0

def drawScene1(screen,p):
    global offset
    global HOTOIL
    global SOY
    offset=v[SCREENX]-p[X]
    screen.blit(neptune,(offset,0))
    screen.blit(rocket, (offset+3000,20))
   
c=draw.rect(screen, RED, SOY[:4], 2)
b=draw.rect(screen, WHITE, HOTOIL[:4], 2)    
def drawsceneForLevel1():
    global b
    global c
    row=HOTOIL[ROW]
    col=int(HOTOIL[COL])
    pic=p[row][col]
    screen.blit(pic,(200,HOTOIL[Y]))
    for s in stepspace:
         s=s.move(offset,0)
         draw.rect(screen, (255,0,0), s)
         
    draw.rect(screen, (255,255,100), (200,HOTOIL[1],HOTOIL[2],HOTOIL[3]), 2)
def move(p):
    
    keys = key.get_pressed()

    if keys[K_LEFT] and p[X]>200:
        v[X] = -15#5
    elif keys[K_RIGHT] and p[X]<3300:
        v[X] = 15#5
    else:
        v[X] = 0

def jump1(p):
    'moving the player'
    keys = key.get_pressed()
    if keys[K_UP] and p[Y] + p[H] == v[BOT] and v[Y] == 0:    
        v[Y] = jumpSpeed
    p[X] += v[X] #moving left/right
    v[Y] += gravity #acceleration

#-----------------------------------------------------------------------LEVEL 2-------------------------------------------------------
jupiter=image.load("background/jupiter.png").convert()
stepspace2 = (Rect(0, 695, 580, 60))# first plat
def drawScene2(screen,p):
    global offset
    global HOTOIL
    global SOY
    offset=v[SCREENX]-p[X]
    screen.blit(jupiter,(offset,0))
    screen.blit(rocket, (offset+3000,20))
   
c=draw.rect(screen, RED, SOY[:4], 2)
b=draw.rect(screen, WHITE, HOTOIL[:4], 2)  
def drawsceneForLevel2():
    global b
    global c
    row=HOTOIL[ROW]
    col=int(HOTOIL[COL])
    pic=p[row][col]
    screen.blit(pic,(200,HOTOIL[Y]))
    for s in steping2:
         s=s.move(offset,0)
         draw.rect(screen, (255,0,0), s)
         
    draw.rect(screen, (255,255,100), (200,HOTOIL[1],HOTOIL[2],HOTOIL[3]), 2)
#-----------------------------------------------------------------------LEVEL 3-------------------------------------------------------
mars=image.load("background/mars.png").convert()
stepspace3 = (Rect(0, 695, 580, 60))# first plat
def drawScene3(screen,p):
    global offset
    offset=v[SCREENX]-p[X]
    screen.blit(mars,(offset,0))
    screen.blit(rocket, (offset+3000,20))    
b=draw.rect(screen, WHITE, HOTOIL[:4], 2)    
def drawsceneForLevel3():
    global b
    global c    
    row=HOTOIL[ROW]
    col=int(HOTOIL[COL])
    pic=p[row][col]
    screen.blit(pic,(200,HOTOIL[Y]))
    for s in stepspace:
         s=s.move(offset,0)
         draw.rect(screen, (255,0,0), s)
         
    draw.rect(screen, (255,255,100), (200,HOTOIL[1],HOTOIL[2],HOTOIL[3]), 2)



#-----------------------------------------------------------------------------------------------------------------------------------------
running = True
myClock=time.Clock()
while running:
    mp=False
    for evnt in event.get():              
        if evnt.type == QUIT:
            running = False
        elif evnt.type==MOUSEBUTTONDOWN:
            if evnt.button==1:
                mp=True
    screen.fill((0,0,0))
    keys=key.get_pressed()
    mx,my=mouse.get_pos()
    #print(mx, my)
  

        
#-------------------------------------------------------------------Transitions-------------------------------------------------------
    if transition=="Menu":
        menu()
    if transition=="intro":
        intro()
        gravity=6
    elif transition=="level1":
        gravity=4
        L1()
    elif transition=="level2":
        L2()
        gravity=3
    elif transition=="level3":
        gravity=4
    elif transition=="credits":
        creditss()
    elif transition=="story":
        story()
    elif transition=="story2":
        story2()
    elif transition=="story3":
        story3()    
    elif transition=="decide":
        decide()
    elif transition=="pog":
        pog()
    if lives<=0:
         screen.blit(life[0],(427,10))
         pog()
         transition="pog"
    elif lives==1 and transition !="Menu" and transition !="story"and transition !="story2"and transition !="story3" and transition !="decide"and transition !="intro":
        screen.blit(life[1],(427,10))
    elif lives==2 and transition !="Menu" and transition !="story"and transition !="story2"and transition !="story3" and transition !="decide"and transition !="intro" :
        screen.blit(life[2],(427,10))
    elif lives==3 and transition !="Menu" and transition !="story"and transition !="story2"and transition !="story3" and transition !="decide"and transition !="intro":
        screen.blit(life[3],(427,10))
    display.update()
    
    myClock.tick(60)

quit()
