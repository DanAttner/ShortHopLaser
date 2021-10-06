try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    print('import error')
    pass

import pygame
import random


#pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init()


#makes the window
window = pygame.display.set_mode((1000,480))

#captions the window
pygame.display.set_caption('SHL')

Screenwidth = 1000
Screenheight = 480
bg1pos = 270



# imports and defines all pictures in game
walkRight = [pygame.image.load('Game/ChickenMan/ChickenR1.png'), pygame.image.load('Game/ChickenMan/ChickenR1.png'), pygame.image.load('Game/ChickenMan/ChickenR1.png'), pygame.image.load('Game/ChickenMan/ChickenR1.png'), pygame.image.load('Game/ChickenMan/ChickenR1.png'), pygame.image.load('Game/ChickenMan/ChickenR1.png'), pygame.image.load('Game/ChickenMan/ChickenR1.png'), pygame.image.load('Game/ChickenMan/ChickenR1.png'), pygame.image.load('Game/ChickenMan/ChickenR1.png')]
walkLeft = [pygame.image.load('Game/ChickenMan/ChickenL1.png'), pygame.image.load('Game/ChickenMan/ChickenL1.png'), pygame.image.load('Game/ChickenMan/ChickenL1.png'), pygame.image.load('Game/ChickenMan/ChickenL1.png'), pygame.image.load('Game/ChickenMan/ChickenL1.png'), pygame.image.load('Game/ChickenMan/ChickenL1.png'), pygame.image.load('Game/ChickenMan/ChickenL1.png'), pygame.image.load('Game/ChickenMan/ChickenL1.png'), pygame.image.load('Game/ChickenMan/ChickenL1.png')]
standingLaser = [pygame.image.load('Game/ChickenMan/ChickenR2.png'), pygame.image.load('Game/ChickenMan/ChickenR3.png'), pygame.image.load('Game/ChickenMan/ChickenR4.png'), pygame.image.load('Game/ChickenMan/ChickenR5.png'), pygame.image.load('Game/ChickenMan/ChickenR6.png'), pygame.image.load('Game/ChickenMan/ChickenR7.png'), pygame.image.load('Game/ChickenMan/ChickenR8.png'), pygame.image.load('Game/ChickenMan/ChickenR9.png'), pygame.image.load('Game/ChickenMan/ChickenR10.png'), pygame.image.load('Game/ChickenMan/ChickenR11.png')]
standingLaserLeft = [pygame.image.load('Game/ChickenMan/ChickenL2.png'), pygame.image.load('Game/ChickenMan/ChickenL3.png'), pygame.image.load('Game/ChickenMan/ChickenL4.png'), pygame.image.load('Game/ChickenMan/ChickenL5.png'), pygame.image.load('Game/ChickenMan/ChickenL6.png'), pygame.image.load('Game/ChickenMan/ChickenL7.png'), pygame.image.load('Game/ChickenMan/ChickenL8.png'), pygame.image.load('Game/ChickenMan/ChickenL9.png'), pygame.image.load('Game/ChickenMan/ChickenL10.png'), pygame.image.load('Game/ChickenMan/ChickenL11.png')]
redLaser = [pygame.image.load('Game/redlaserSmall.png'),pygame.image.load('Game/redlaserMed.png'), pygame.image.load('Game/redlaser1.png')]
deathexplosion = [pygame.image.load('Game/explosion/explosion.png'), pygame.image.load('Game/explosion/explosion_down_one.png'), pygame.image.load('Game/explosion/explosion_down_two.png'), pygame.image.load('Game/explosion/explosion_down_three.png'), pygame.image.load('Game/explosion/explosion_down_four.png'), pygame.image.load('Game/explosion/explosion_down_five.png')]
iframefalco = [pygame.image.load('Game/iframes/iframeStand/istand1.png'), pygame.image.load('Game/iframes/iframeStand/istand2.png'), pygame.image.load('Game/iframes/iframeStand/istand3.png'), pygame.image.load('Game/iframes/iframeStand/istand4.png')]
iframefalcoLeft = [pygame.image.load('Game/iframes/iframeStand/istand1L.png'), pygame.image.load('Game/iframes/iframeStand/istand2L.png'), pygame.image.load('Game/iframes/iframeStand/istand3L.png'), pygame.image.load('Game/iframes/iframeStand/istand4L.png')]
iframestandingLaser = [pygame.image.load('Game/iframes/iframeShoot/ishoot2.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot3.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot4.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot5.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot6.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot7.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot8.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot9.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot10.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot11.png')]
iframestandingLaserLeft = [pygame.image.load('Game/iframes/iframeShoot/ishoot2L.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot3L.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot4L.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot5L.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot6L.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot7L.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot8L.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot9L.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot10L.png'), pygame.image.load('Game/iframes/iframeShoot/ishoot11L.png')]
bg = pygame.image.load('Game/blankbg.jpg')
bgship1 = pygame.image.load(('Game/pinkfox.png'))
icon = pygame.image.load(('Game/chickenicon.ico'))

pausemenu = pygame.image.load('Game/Menus/pause_stuff/pause.png')
mainmenu = pygame.image.load('Game/Menus/main_menu.jpg')
mainmenustart = [pygame.image.load('Game/Menus/main_menu_start/main_menu_start1.jpg'), pygame.image.load('Game/Menus/main_menu_start/main_menu_start2.png'), pygame.image.load('Game/Menus/main_menu_start/main_menu_start3.png'), pygame.image.load('Game/Menus/main_menu_start/main_menu_start4.png'), pygame.image.load('Game/Menus/main_menu_start/main_menu_start5.png'), pygame.image.load('Game/Menus/main_menu_start/main_menu_start6.png'), pygame.image.load('Game/Menus/main_menu_start/main_menu_start7.png'), pygame.image.load('Game/Menus/main_menu_start/main_menu_start8.png'), pygame.image.load('Game/Menus/main_menu_start/main_menu_start9.png'), pygame.image.load('Game/Menus/main_menu_start/main_menu_start10.png')]
mainmenutraining = [pygame.image.load('Game/Menus/main_menu_training/main_menu_training1.png'), pygame.image.load('Game/Menus/main_menu_training/main_menu_training2.png'), pygame.image.load('Game/Menus/main_menu_training/main_menu_training3.png'), pygame.image.load('Game/Menus/main_menu_training/main_menu_training4.png'), pygame.image.load('Game/Menus/main_menu_training/main_menu_training5.png'), pygame.image.load('Game/Menus/main_menu_training/main_menu_training6.png'), pygame.image.load('Game/Menus/main_menu_training/main_menu_training7.png'), pygame.image.load('Game/Menus/main_menu_training/main_menu_training8.png'), pygame.image.load('Game/Menus/main_menu_training/main_menu_training9.png'), pygame.image.load('Game/Menus/main_menu_training/main_menu_training10.png')]
mainmenucontrols = [pygame.image.load('Game/Menus/main_menu_controls/main_menu_controls1.png'), pygame.image.load('Game/Menus/main_menu_controls/main_menu_controls2.png'), pygame.image.load('Game/Menus/main_menu_controls/main_menu_controls3.png'), pygame.image.load('Game/Menus/main_menu_controls/main_menu_controls4.png'), pygame.image.load('Game/Menus/main_menu_controls/main_menu_controls5.png'), pygame.image.load('Game/Menus/main_menu_controls/main_menu_controls6.png'), pygame.image.load('Game/Menus/main_menu_controls/main_menu_controls7.png'), pygame.image.load('Game/Menus/main_menu_controls/main_menu_controls8.png'), pygame.image.load('Game/Menus/main_menu_controls/main_menu_controls9.png'), pygame.image.load('Game/Menus/main_menu_controls/main_menu_controls10.png')]
mainmenusettings = [pygame.image.load('Game/Menus/main_menu_settings/main_menu_settings1.png'), pygame.image.load('Game/Menus/main_menu_settings/main_menu_settings2.png'), pygame.image.load('Game/Menus/main_menu_settings/main_menu_settings3.png'), pygame.image.load('Game/Menus/main_menu_settings/main_menu_settings4.png'), pygame.image.load('Game/Menus/main_menu_settings/main_menu_settings5.png'), pygame.image.load('Game/Menus/main_menu_settings/main_menu_settings6.png'), pygame.image.load('Game/Menus/main_menu_settings/main_menu_settings7.png'), pygame.image.load('Game/Menus/main_menu_settings/main_menu_settings8.png'), pygame.image.load('Game/Menus/main_menu_settings/main_menu_settings9.png'), pygame.image.load('Game/Menus/main_menu_settings/main_menu_settings10.png')]
mainmenuexit = [pygame.image.load('Game/Menus/main_menu_exit/main_menu_exit1.png'), pygame.image.load('Game/Menus/main_menu_exit/main_menu_exit2.png'), pygame.image.load('Game/Menus/main_menu_exit/main_menu_exit3.png'), pygame.image.load('Game/Menus/main_menu_exit/main_menu_exit4.png'), pygame.image.load('Game/Menus/main_menu_exit/main_menu_exit5.png'), pygame.image.load('Game/Menus/main_menu_exit/main_menu_exit6.png'), pygame.image.load('Game/Menus/main_menu_exit/main_menu_exit7.png'), pygame.image.load('Game/Menus/main_menu_exit/main_menu_exit8.png'), pygame.image.load('Game/Menus/main_menu_exit/main_menu_exit9.png'), pygame.image.load('Game/Menus/main_menu_exit/main_menu_exit10.png')]
controlsmenu = [pygame.image.load('Game/Menus/controls_menu/controls_menu1.png')]
settingsmenu= [pygame.image.load('Game/Menus/Settings_menu/Back_Off_off.png'),  pygame.image.load('Game/Menus/Settings_menu/Back_Off_On.png'), pygame.image.load('Game/Menus/Settings_menu/Back_On_Off.png'), pygame.image.load('Game/Menus/Settings_menu/Back_On_On.png'), pygame.image.load('Game/Menus/Settings_menu/Music_Off_Off.png'), pygame.image.load('Game/Menus/Settings_menu/Music_Off_On.png'), pygame.image.load('Game/Menus/Settings_menu/Music_On_Off.png'), pygame.image.load('Game/Menus/Settings_menu/Music_On_On.png'), pygame.image.load('Game/Menus/Settings_menu/Sound_Off_Off.png'), pygame.image.load('Game/Menus/Settings_menu/Sound_Off_On.png'), pygame.image.load('Game/Menus/Settings_menu/Sound_On_Off.png'), pygame.image.load('Game/Menus/Settings_menu/Sound_On_On.png')]
falcostock = [pygame.image.load('Game/falcostock.png')]

lasersound = pygame.mixer.Sound('Game/Falco sounds/laser sound 4.wav')
clicksound = pygame.mixer.Sound('Game/Falco sounds/click3.wav')
explosionsound = pygame.mixer.Sound('Game/Falco sounds/explosion2.wav')
deathsound = pygame.mixer.Sound('Game/Falco sounds/death sound2.wav')
dingsound1 = pygame.mixer.Sound('Game/Falco sounds/ding1_1.wav')
dingsound2 = pygame.mixer.Sound('Game/Falco sounds/ding2_1.wav')
losestocksound = pygame.mixer.Sound('Game/Falco sounds/fsmash1.wav')


menumusic = pygame.mixer.music.load('Game/music/Flacos_Menu_Groove.mp3')
stagemusic = pygame.mixer.music.load('Game/music/Flaco_main_game.mp3')
nomusic = pygame.mixer.music.load('Game/Falco sounds/silence.wav')

#pygame.mixer.music.play(-1)   # plays full music

# icon
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

# define player class for all of our juicy variables
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4.5
        self.isJump = False
        self.jumpCount = 0
        self.left = False
        self.right = False
        self.down = False
        self.walkCount = 0
        self.standing = True
        self.jumpSquat = False
        self.laserlag = 0
        self.unlockstandinglaser = False
        self.unlockaeriallaser = False
        self.turnonlandLeft = False
        self.turnonlandRight = False
        self.hitbox = (self.x + 14, self.y+3, 36, 55)
        self.alive = True
        self.angelplat = False
        self.iframes = False
        self.falcostockcount = 4



    def draw(self, window):     #character draw method
        self.hitbox = (self.x + 14, self.y+3, 36, 55)
        #pygame.draw.rect(window, (255,0,0), (self.x + 14, self.y+3, 36, 55) , 2)    #hitbox draw

        if self.falcostockcount > 0:
            window.blit(falcostock[0], (8, 18) )
        if self.falcostockcount > 1:
            window.blit(falcostock[0], (40, 18) )
        if self.falcostockcount > 2:
            window.blit(falcostock[0], (72, 18) )
        if self.falcostockcount > 3:
            window.blit(falcostock[0], (104, 18) )



        if self.unlockstandinglaser and self.right:         #draw standing laser right
            if self.iframes == True:
                if self.laserlag >=0 and self.laserlag <= 3:
                    window.blit(iframestandingLaser[0], (round(self.x), round(self.y)))
                if self.laserlag >=4 and self.laserlag <= 6:
                    window.blit(iframestandingLaser[1], (round(self.x), round(self.y)))
                if self.laserlag >=7 and self.laserlag <= 9:
                    window.blit(iframestandingLaser[2], (round(self.x), round(self.y)))
                if self.laserlag >=10 and self.laserlag <= 11:
                    window.blit(iframestandingLaser[3], (round(self.x), round(self.y)))
                if self.laserlag >=12 and self.laserlag <= 13:
                    window.blit(iframestandingLaser[4], (round(self.x), round(self.y)))
                if self.laserlag >=14 and self.laserlag <= 15:
                    window.blit(iframestandingLaser[5], (round(self.x), round(self.y)))
                if self.laserlag >=16 and self.laserlag <= 17:
                    window.blit(iframestandingLaser[6], (round(self.x), round(self.y)))
                if self.laserlag >=18 and self.laserlag <= 20:
                    window.blit(iframestandingLaser[7], (round(self.x), round(self.y)))
                if self.laserlag >=21 and self.laserlag <= 22:
                    window.blit(iframestandingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag >=23 and self.laserlag <= 26:
                    window.blit(iframestandingLaser[9], (round(self.x), round(self.y)))
                if self.laserlag >=27 and self.laserlag <= 30:
                    window.blit(iframestandingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag >=31 and self.laserlag <= 33:
                    window.blit(iframestandingLaser[7], (round(self.x), round(self.y)))
                if self.laserlag >=34 and self.laserlag <= 36:
                    window.blit(iframestandingLaser[6], (round(self.x), round(self.y)))
                if self.laserlag >=37 and self.laserlag <= 39:
                    window.blit(iframestandingLaser[5], (round(self.x), round(self.y)))
                if self.laserlag >=40 and self.laserlag <= 42:
                    window.blit(iframestandingLaser[4], (round(self.x), round(self.y)))
                if self.laserlag >=43 and self.laserlag <= 46:
                    window.blit(iframestandingLaser[3], (round(self.x), round(self.y)))
                if self.laserlag >=47 and self.laserlag <= 49:
                    window.blit(iframestandingLaser[2], (round(self.x), round(self.y)))
                if self.laserlag >=50 and self.laserlag <= 52:
                    window.blit(iframestandingLaser[1], (round(self.x), round(self.y)))
                if self.laserlag >=53 and self.laserlag <= 56:
                    window.blit(iframestandingLaser[0], (round(self.x), round(self.y)))

            else:

                if self.laserlag >=0 and self.laserlag <= 3:
                    window.blit(standingLaser[0], (round(self.x), round(self.y)))
                if self.laserlag >=4 and self.laserlag <= 6:
                    window.blit(standingLaser[1], (round(self.x), round(self.y)))
                if self.laserlag >=7 and self.laserlag <= 9:
                    window.blit(standingLaser[2], (round(self.x), round(self.y)))
                if self.laserlag >=10 and self.laserlag <= 11:
                    window.blit(standingLaser[3], (round(self.x), round(self.y)))
                if self.laserlag >=12 and self.laserlag <= 13:
                    window.blit(standingLaser[4], (round(self.x), round(self.y)))
                if self.laserlag >=14 and self.laserlag <= 15:
                    window.blit(standingLaser[5], (round(self.x), round(self.y)))
                if self.laserlag >=16 and self.laserlag <= 17:
                    window.blit(standingLaser[6], (round(self.x), round(self.y)))
                if self.laserlag >=18 and self.laserlag <= 20:
                    window.blit(standingLaser[7], (round(self.x), round(self.y)))
                if self.laserlag >=21 and self.laserlag <= 22:
                    window.blit(standingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag >=23 and self.laserlag <= 26:
                    window.blit(standingLaser[9], (round(self.x), round(self.y)))
                if self.laserlag >=27 and self.laserlag <= 30:
                    window.blit(standingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag >=31 and self.laserlag <= 33:
                    window.blit(standingLaser[7], (round(self.x), round(self.y)))
                if self.laserlag >=34 and self.laserlag <= 36:
                    window.blit(standingLaser[6], (round(self.x), round(self.y)))
                if self.laserlag >=37 and self.laserlag <= 39:
                    window.blit(standingLaser[5], (round(self.x), round(self.y)))
                if self.laserlag >=40 and self.laserlag <= 42:
                    window.blit(standingLaser[4], (round(self.x), round(self.y)))
                if self.laserlag >=43 and self.laserlag <= 46:
                    window.blit(standingLaser[3], (round(self.x), round(self.y)))
                if self.laserlag >=47 and self.laserlag <= 49:
                    window.blit(standingLaser[2], (round(self.x), round(self.y)))
                if self.laserlag >=50 and self.laserlag <= 52:
                    window.blit(standingLaser[1], (round(self.x), round(self.y)))
                if self.laserlag >=53 and self.laserlag <= 56:
                    window.blit(standingLaser[0], (round(self.x), round(self.y)))

        elif self.unlockstandinglaser and self.left:              #draw stanidng laser left
            if self.iframes == True:
                if self.laserlag >=0 and self.laserlag <= 3:
                    window.blit(iframestandingLaserLeft[0], (round(self.x), round(self.y)))
                if self.laserlag >=4 and self.laserlag <= 6:
                    window.blit(iframestandingLaserLeft[1], (round(self.x), round(self.y)))
                if self.laserlag >=7 and self.laserlag <= 9:
                    window.blit(iframestandingLaserLeft[2], (round(self.x), round(self.y)))
                if self.laserlag >=10 and self.laserlag <= 11:
                    window.blit(iframestandingLaserLeft[3], (round(self.x), round(self.y)))
                if self.laserlag >=12 and self.laserlag <= 13:
                    window.blit(iframestandingLaserLeft[4], (round(self.x), round(self.y)))
                if self.laserlag >=14 and self.laserlag <= 15:
                    window.blit(iframestandingLaserLeft[5], (round(self.x), round(self.y)))
                if self.laserlag >=16 and self.laserlag <= 17:
                    window.blit(iframestandingLaserLeft[6], (round(self.x), round(self.y)))
                if self.laserlag >=18 and self.laserlag <= 20:
                    window.blit(iframestandingLaserLeft[7], (round(self.x), round(self.y)))
                if self.laserlag >=21 and self.laserlag <= 22:
                    window.blit(iframestandingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag >=23 and self.laserlag <= 26:
                    window.blit(iframestandingLaserLeft[9], (round(self.x), round(self.y)))
                if self.laserlag >=27 and self.laserlag <= 30:
                    window.blit(iframestandingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag >=31 and self.laserlag <= 33:
                    window.blit(iframestandingLaserLeft[7], (round(self.x), round(self.y)))
                if self.laserlag >=34 and self.laserlag <= 36:
                    window.blit(iframestandingLaserLeft[6], (round(self.x), round(self.y)))
                if self.laserlag >=37 and self.laserlag <= 39:
                    window.blit(iframestandingLaserLeft[5], (round(self.x), round(self.y)))
                if self.laserlag >=40 and self.laserlag <= 42:
                    window.blit(iframestandingLaserLeft[4], (round(self.x), round(self.y)))
                if self.laserlag >=43 and self.laserlag <= 46:
                    window.blit(iframestandingLaserLeft[3], (round(self.x), round(self.y)))
                if self.laserlag >=47 and self.laserlag <= 49:
                    window.blit(iframestandingLaserLeft[2], (round(self.x), round(self.y)))
                if self.laserlag >=50 and self.laserlag <= 52:
                    window.blit(iframestandingLaserLeft[1], (round(self.x), round(self.y)))
                if self.laserlag >=53 and self.laserlag <= 56:
                    window.blit(iframestandingLaserLeft[0], (round(self.x), round(self.y)))

            else:



                if self.laserlag >=0 and self.laserlag <= 3:
                    window.blit(standingLaserLeft[0], (round(self.x), round(self.y)))
                if self.laserlag >=4 and self.laserlag <= 6:
                    window.blit(standingLaserLeft[1], (round(self.x), round(self.y)))
                if self.laserlag >=7 and self.laserlag <= 9:
                    window.blit(standingLaserLeft[2], (round(self.x), round(self.y)))
                if self.laserlag >=10 and self.laserlag <= 11:
                    window.blit(standingLaserLeft[3], (round(self.x), round(self.y)))
                if self.laserlag >=12 and self.laserlag <= 13:
                    window.blit(standingLaserLeft[4], (round(self.x), round(self.y)))
                if self.laserlag >=14 and self.laserlag <= 15:
                    window.blit(standingLaserLeft[5], (round(self.x), round(self.y)))
                if self.laserlag >=16 and self.laserlag <= 17:
                    window.blit(standingLaserLeft[6], (round(self.x), round(self.y)))
                if self.laserlag >=18 and self.laserlag <= 20:
                    window.blit(standingLaserLeft[7], (round(self.x), round(self.y)))
                if self.laserlag >=21 and self.laserlag <= 22:
                    window.blit(standingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag >=23 and self.laserlag <= 26:
                    window.blit(standingLaserLeft[9], (round(self.x), round(self.y)))
                if self.laserlag >=27 and self.laserlag <= 30:
                    window.blit(standingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag >=31 and self.laserlag <= 33:
                    window.blit(standingLaserLeft[7], (round(self.x), round(self.y)))
                if self.laserlag >=34 and self.laserlag <= 36:
                    window.blit(standingLaserLeft[6], (round(self.x), round(self.y)))
                if self.laserlag >=37 and self.laserlag <= 39:
                    window.blit(standingLaserLeft[5], (round(self.x), round(self.y)))
                if self.laserlag >=40 and self.laserlag <= 42:
                    window.blit(standingLaserLeft[4], (round(self.x), round(self.y)))
                if self.laserlag >=43 and self.laserlag <= 46:
                    window.blit(standingLaserLeft[3], (round(self.x), round(self.y)))
                if self.laserlag >=47 and self.laserlag <= 49:
                    window.blit(standingLaserLeft[2], (round(self.x), round(self.y)))
                if self.laserlag >=50 and self.laserlag <= 52:
                    window.blit(standingLaserLeft[1], (round(self.x), round(self.y)))
                if self.laserlag >=53 and self.laserlag <= 56:
                    window.blit(standingLaserLeft[0], (round(self.x), round(self.y)))

        elif self.unlockaeriallaser and self.right:           # aerial laser right

            if self.iframes == True:

                if self.laserlag >= 0 and self.laserlag <= 2:
                    window.blit(iframestandingLaser[0], (round(self.x), round(self.y)))
                if self.laserlag >= 3 and self.laserlag <= 4:
                    window.blit(iframestandingLaser[1], (round(self.x), round(self.y)))
                if self.laserlag == 5:
                    window.blit(iframestandingLaser[2], (round(self.x), round(self.y)))
                if self.laserlag == 6:
                    window.blit(iframestandingLaser[3], (round(self.x), round(self.y)))
                if self.laserlag == 7:
                    window.blit(iframestandingLaser[4], (round(self.x), round(self.y)))
                if self.laserlag == 8:
                    window.blit(iframestandingLaser[5], (round(self.x), round(self.y)))
                if self.laserlag == 9:
                    window.blit(iframestandingLaser[6], (round(self.x), round(self.y)))
                if self.laserlag == 10:
                    window.blit(iframestandingLaser[7], (round(self.x), round(self.y)))
                if self.laserlag == 11:
                    window.blit(iframestandingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag >=12 and self.laserlag <= 14:
                    window.blit(iframestandingLaser[9], (round(self.x), round(self.y)))
                if self.laserlag >=15 and self.laserlag <= 17:
                    window.blit(iframestandingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag >=17 and self.laserlag <= 20:
                    window.blit(iframestandingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag >=21 and self.laserlag <= 24:
                    window.blit(iframestandingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag >=25 and self.laserlag <= 27:
                    window.blit(iframestandingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag >=28 and self.laserlag <= 30:
                    window.blit(iframestandingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag >=31 and self.laserlag <= 32:
                    window.blit(iframestandingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag == 33:
                    window.blit(iframestandingLaser[2], (round(self.x), round(self.y)))
                if self.laserlag == 34:
                    window.blit(iframestandingLaser[1], (round(self.x), round(self.y)))
                if self.laserlag == 35:
                    window.blit(iframestandingLaser[0], (round(self.x), round(self.y)))

            else:

                if self.laserlag >= 0 and self.laserlag <= 2:
                    window.blit(standingLaser[0], (round(self.x), round(self.y)))
                if self.laserlag >= 3 and self.laserlag <= 4:
                    window.blit(standingLaser[1], (round(self.x), round(self.y)))
                if self.laserlag == 5:
                    window.blit(standingLaser[2], (round(self.x), round(self.y)))
                if self.laserlag == 6:
                    window.blit(standingLaser[3], (round(self.x), round(self.y)))
                if self.laserlag == 7:
                    window.blit(standingLaser[4], (round(self.x), round(self.y)))
                if self.laserlag == 8:
                    window.blit(standingLaser[5], (round(self.x), round(self.y)))
                if self.laserlag == 9:
                    window.blit(standingLaser[6], (round(self.x), round(self.y)))
                if self.laserlag == 10:
                    window.blit(standingLaser[7], (round(self.x), round(self.y)))
                if self.laserlag == 11:
                    window.blit(standingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag >=12 and self.laserlag <= 14:
                    window.blit(standingLaser[9], (round(self.x), round(self.y)))
                if self.laserlag >=15 and self.laserlag <= 17:
                    window.blit(standingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag >=17 and self.laserlag <= 20:
                    window.blit(standingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag >=21 and self.laserlag <= 24:
                    window.blit(standingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag >=25 and self.laserlag <= 27:
                    window.blit(standingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag >=28 and self.laserlag <= 30:
                    window.blit(standingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag >=31 and self.laserlag <= 32:
                    window.blit(standingLaser[8], (round(self.x), round(self.y)))
                if self.laserlag == 33:
                    window.blit(standingLaser[2], (round(self.x), round(self.y)))
                if self.laserlag == 34:
                    window.blit(standingLaser[1], (round(self.x), round(self.y)))
                if self.laserlag == 35:
                    window.blit(standingLaser[0], (round(self.x), round(self.y)))

        elif self.unlockaeriallaser and self.left:                #aerial laser left
            if self.iframes == True:
                if self.laserlag >= 0 and self.laserlag <= 2:
                    window.blit(iframestandingLaserLeft[0], (round(self.x), round(self.y)))
                if self.laserlag >= 3 and self.laserlag <= 4:
                    window.blit(iframestandingLaserLeft[1], (round(self.x), round(self.y)))
                if self.laserlag == 5:
                    window.blit(iframestandingLaserLeft[2], (round(self.x), round(self.y)))
                if self.laserlag == 6:
                    window.blit(iframestandingLaserLeft[3], (round(self.x), round(self.y)))
                if self.laserlag == 7:
                    window.blit(iframestandingLaserLeft[4], (round(self.x), round(self.y)))
                if self.laserlag == 8:
                    window.blit(iframestandingLaserLeft[5], (round(self.x), round(self.y)))
                if self.laserlag == 9:
                    window.blit(iframestandingLaserLeft[6], (round(self.x), round(self.y)))
                if self.laserlag == 10:
                    window.blit(iframestandingLaserLeft[7], (round(self.x), round(self.y)))
                if self.laserlag == 11:
                    window.blit(iframestandingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag >=12 and self.laserlag <= 14:
                    window.blit(iframestandingLaserLeft[9], (round(self.x), round(self.y)))
                if self.laserlag >=15 and self.laserlag <= 17:
                    window.blit(iframestandingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag >=17 and self.laserlag <= 20:
                    window.blit(iframestandingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag >=21 and self.laserlag <= 24:
                    window.blit(iframestandingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag >=25 and self.laserlag <= 27:
                    window.blit(iframestandingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag >=28 and self.laserlag <= 30:
                    window.blit(iframestandingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag >=31 and self.laserlag <= 32:
                    window.blit(iframestandingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag == 33:
                    window.blit(iframestandingLaserLeft[2], (round(self.x), round(self.y)))
                if self.laserlag == 34:
                    window.blit(iframestandingLaserLeft[1], (round(self.x), round(self.y)))
                if self.laserlag == 35:
                    window.blit(iframestandingLaserLeft[0], (round(self.x), round(self.y)))
            else:

                if self.laserlag >= 0 and self.laserlag <= 2:
                    window.blit(standingLaserLeft[0], (round(self.x), round(self.y)))
                if self.laserlag >= 3 and self.laserlag <= 4:
                    window.blit(standingLaserLeft[1], (round(self.x), round(self.y)))
                if self.laserlag == 5:
                    window.blit(standingLaserLeft[2], (round(self.x), round(self.y)))
                if self.laserlag == 6:
                    window.blit(standingLaserLeft[3], (round(self.x), round(self.y)))
                if self.laserlag == 7:
                    window.blit(standingLaserLeft[4], (round(self.x), round(self.y)))
                if self.laserlag == 8:
                    window.blit(standingLaserLeft[5], (round(self.x), round(self.y)))
                if self.laserlag == 9:
                    window.blit(standingLaserLeft[6], (round(self.x), round(self.y)))
                if self.laserlag == 10:
                    window.blit(standingLaserLeft[7], (round(self.x), round(self.y)))
                if self.laserlag == 11:
                    window.blit(standingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag >=12 and self.laserlag <= 14:
                    window.blit(standingLaserLeft[9], (round(self.x), round(self.y)))
                if self.laserlag >=15 and self.laserlag <= 17:
                    window.blit(standingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag >=17 and self.laserlag <= 20:
                    window.blit(standingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag >=21 and self.laserlag <= 24:
                    window.blit(standingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag >=25 and self.laserlag <= 27:
                    window.blit(standingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag >=28 and self.laserlag <= 30:
                    window.blit(standingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag >=31 and self.laserlag <= 32:
                    window.blit(standingLaserLeft[8], (round(self.x), round(self.y)))
                if self.laserlag == 33:
                    window.blit(standingLaserLeft[2], (round(self.x), round(self.y)))
                if self.laserlag == 34:
                    window.blit(standingLaserLeft[1], (round(self.x), round(self.y)))
                if self.laserlag == 35:
                    window.blit(standingLaserLeft[0], (round(self.x), round(self.y)))




        else:

            #draw standing bassed on last directionm
            if self.left:
                if self.iframes == True:
                    window.blit(iframefalcoLeft[(random.randint(0,3))], (round(self.x), round(self.y)))
                else:
                    window.blit(walkLeft[0], (round(self.x), round(self.y)))

            elif self.right:
                if self.iframes == True:
                    window.blit(iframefalco[(random.randint(0,3))], (round(self.x), round(self.y)))
                else:
                    window.blit(walkRight[0], (round(self.x), round(self.y)))

            else:
                window.blit(walkRight[0], (round(self.x), round(self.y)))



#projectle class plz
class projectile(object):
    def __init__(self,x,y ,facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 10 * facing
        self.shootCount = 0
        self.laserSizeTimer = 0
        self.hitbox = (self.x , self.y, 39, 3)
        self.laseralive = True


    def draw(self, window):

        if self.facing == -1:
            self.hitbox = (self.x, self.y, 39, 3)
            #pygame.draw.rect(window, (0,0,255), (self.x + 20 , self.y, 39, 3) , 2)    #hitbox draw

            window.blit(redLaser[2], ((self.x) , self.y))

        else:
            self.hitbox = (self.x , self.y, 39, 3)
            #pygame.draw.rect(window, (0,255,0), (self.x , self.y, 39, 3) , 2)    #hitbox draw

            window.blit(redLaser[2], (self.x , self.y))



#enemy class plz
class enemy (object):
    walkRight = [pygame.image.load('Game/redfalcoR1.png')]
    walkLeft = [pygame.image.load('Game/redfalcoL1.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 2
        self.hitbox = (self.x + 14, self.y + 3, 36, 55)
        self.alive = True
        self.exploding = 0
        self.shield = True

    def draw(self, window):

        if self.alive == False:
            self.hitbox = (9999, 9999, 1, 1)
            self.exploding = self.exploding + 1

            if self.exploding > 1  and self.exploding <= 6:
                window.blit(deathexplosion[0], (self.x , self.y  ))  # throw in the explosivo
            if self.exploding > 6 and self.exploding <= 12:
                window.blit(deathexplosion[1], (self.x , self.y  ))
            if self.exploding > 12 and self.exploding <= 18:
                window.blit(deathexplosion[2], (self.x , self.y  ))
            if self.exploding > 18 and self.exploding <= 24:
                window.blit(deathexplosion[3], (self.x , self.y  ))
            if self.exploding > 24 and self.exploding <= 30:
                window.blit(deathexplosion[4], (self.x , self.y  ))

            if self.exploding >= 31:
                self.x  = 1
                self.alive = True
                self.exploding = 0




        else:
            #pygame.draw.rect(window, (255,0,0), (self.x + 14, self.y+5 , 36, 52) , 2)    #hitbox draw

            self.move()
            self.hitbox = (self.x + 14, self.y+5, 36, 52)


            if self.vel >= 0:
                window.blit(self.walkRight[0], (self.x, self.y))

            else:
                window.blit(self.walkLeft[0], (self.x, self.y))




    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1


        if self.vel < 0:
            if self.x + self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1


    def hit(self):
        print('laser hit')
        self.alive = False


#unfortunate seperate class for each enemy, thus defeating the purpose of classes, and making dan sad.
class gob2 (object):
    walkRight = [pygame.image.load('Game/bluefalcoR1.png')]
    walkLeft = [pygame.image.load('Game/bluefalcoL1.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = -4
        self.hitbox = (self.x + 14, self.y + 3, 36, 55)
        self.alive = True
        self.exploding = 0
        self.shield = True


    def draw(self, window):

        if self.alive == False:
            self.hitbox = (9999, 9999, 1, 1)
            self.exploding = self.exploding + 1

            if self.exploding > 1  and self.exploding <= 6:
                window.blit(deathexplosion[0], (self.x , self.y  ))  # throw in the explosivo
            if self.exploding > 6 and self.exploding <= 12:
                window.blit(deathexplosion[1], (self.x , self.y  ))
            if self.exploding > 12 and self.exploding <= 18:
                window.blit(deathexplosion[2], (self.x , self.y  ))
            if self.exploding > 18 and self.exploding <= 24:
                window.blit(deathexplosion[3], (self.x , self.y  ))
            if self.exploding > 24 and self.exploding <= 30:
                window.blit(deathexplosion[4], (self.x , self.y  ))

            if self.exploding >= 31:
                self.x  = 950
                self.alive = True
                self.exploding = 0

        else:
            #pygame.draw.rect(window, (255,0,0), (self.x + 14, self.y+5 , 36, 52) , 2)    #hitbox draw

            self.move()
            self.hitbox = (self.x + 14, self.y+5, 36, 52)


            if self.vel > 0:
                window.blit(self.walkRight[0], (self.x, self.y))


            else:
                window.blit(self.walkLeft[0], (self.x, self.y))


    def move(self):

        if self.vel < 0:
            if self.x + self.vel >= self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1

        if self.vel > 0:
            if self.x + self.vel <= self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1




    def hit(self):
        print('laser hit')
        self.alive = False





#unfortunate seperate class for each enemy, thus defeating the purpose of classes, and making dan sad.
class gob3 (object):
    walkRight = [pygame.image.load('Game/goldfalcoR1.png')]
    walkLeft = [pygame.image.load('Game/goldfalcoL1.png')]
    walkRight1 = [pygame.image.load('Game/shieldgoldfalcoR1.png')]
    walkLeft1 = [pygame.image.load('Game/shieldgoldfalcoL1.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = -1
        self.hitbox = (self.x + 14, self.y + 3, 36, 55)
        self.alive = True
        self.exploding = 0
        self.shield = True
        self.position = 9999


    def draw(self, window):

        if self.alive == False:
            self.shield = True
            self.hitbox = (9999, 9999, 1, 1)
            self.exploding = self.exploding + 1

            if self.exploding > 1  and self.exploding <= 6:
                window.blit(deathexplosion[0], (self.x , self.y  ))  # throw in the explosivo
            if self.exploding > 6 and self.exploding <= 12:
                window.blit(deathexplosion[1], (self.x , self.y  ))
            if self.exploding > 12 and self.exploding <= 18:
                window.blit(deathexplosion[2], (self.x , self.y  ))
            if self.exploding > 18 and self.exploding <= 24:
                window.blit(deathexplosion[3], (self.x , self.y  ))
            if self.exploding > 24 and self.exploding <= 30:
                window.blit(deathexplosion[4], (self.x , self.y  ))

            if self.exploding >= 31:

                self.position = (random.randint(0,1))
                if self.position == 0:
                    self.x = 950
                    self.end = 1
                else:
                    self.x = 1
                    self.end  = 950

                self.alive = True
                self.exploding = 0

        else:
            #pygame.draw.rect(window, (255,0,0), (self.x + 14, self.y+5 , 36, 52) , 2)    #hitbox draw



            self.move()
            self.hitbox = (self.x + 14, self.y+5, 36, 52)


            if self.vel > 0:
                if self.shield:
                    window.blit(self.walkRight1[0], (self.x, self.y))
                else:
                    window.blit(self.walkRight[0], (self.x, self.y))


            else:
                if self.shield:
                    window.blit(self.walkLeft1[0], (self.x, self.y))
                else:
                    window.blit(self.walkLeft[0], (self.x, self.y))


    def move(self):

        if self.vel < 0:
            if self.x + self.vel >= self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1

        if self.vel > 0:
            if self.x + self.vel <= self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1


    def hit(self):
        print('laser hit')
        if self.shield == False:
            self.alive = False
        else:
            self.shield = False




#unfortunate seperate class for each enemy, thus defeating the purpose of classes, and making dan sad.
class gob4 (object):
    walkRight = [pygame.image.load('Game/greenfalcoR1.png')]
    walkLeft = [pygame.image.load('Game/greenfalcoL1.png')]
    walkRight1 = [pygame.image.load('Game/sheildgreenfalcoR1.png')]
    walkLeft1 = [pygame.image.load('Game/sheildgreenfalcoL1.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 4.5
        self.hitbox = (self.x + 14, self.y + 3, 36, 55)
        self.alive = True
        self.exploding = 0
        self.sheild = False


    def draw(self, window):

        if self.alive == False:
            self.hitbox = (9999, 9999, 1, 1)
            self.exploding = self.exploding + 1

            if self.exploding > 1  and self.exploding <= 6:
                window.blit(deathexplosion[0], (self.x , self.y  ))  # throw in the explosivo
            if self.exploding > 6 and self.exploding <= 12:
                window.blit(deathexplosion[1], (self.x , self.y  ))
            if self.exploding > 12 and self.exploding <= 18:
                window.blit(deathexplosion[2], (self.x , self.y  ))
            if self.exploding > 18 and self.exploding <= 24:
                window.blit(deathexplosion[3], (self.x , self.y  ))
            if self.exploding > 24 and self.exploding <= 30:
                window.blit(deathexplosion[4], (self.x , self.y  ))

            if self.exploding >= 51:
                self.x  = (random.randint(1,950))
                self.y = 0
                self.alive = True
                self.exploding = 0
                if numkill >= 200:
                    self.sheild = True

        else:
            #pygame.draw.rect(window, (255,0,0), (self.x + 14, self.y+5 , 36, 52) , 2)    #hitbox draw
            self.move()
            self.hitbox = (self.x + 14, self.y+5, 36, 52)

            if self.sheild:
                if self.vel > 0:
                    window.blit(self.walkRight1[0], (self.x, self.y))

                else:
                    window.blit(self.walkLeft1[0], (self.x, self.y))



            if self.vel >= 0:
                window.blit(self.walkRight[0], (self.x, self.y))

            else:
                window.blit(self.walkLeft[0], (self.x, self.y))


    def move(self):
        if self.y < 410:
            self.y = self.y + 4
        else:
            if falco.x > self.x:
                if self.vel > 0:
                    self.x = self.x + self.vel
                else:
                    self.vel = self.vel * -1
                    self.x = self.x + self.vel

            if falco.x < self.x:
                if self.vel < 0:
                    self.x = self.x + self.vel
                else:
                    self.vel = self.vel * -1
                    self.x = self.x + self.vel





    def hit(self):
        print('laser hit')

        if self.sheild:
            self.sheild = False
        else:
            self.alive = False



musicmute = False
def sounds(x):                #sound fucntion
    global lasersound
    global clicksound
    global explosionsound
    global deathsound
    global dingsound1
    global dingsound2
    global losestocksound



    if x == 'lasersound':
        lasersound.play()

    if x == 'clicksound':
        clicksound.play()

    if x == 'explosionsound':
        explosionsound.play()

    if x == 'deathsound':
        deathsound.play()

    if x == 'dingsound1':
        dingsound1.play()

    if x == 'losestocksound':
        losestocksound.play()


    if x == 'pause':
        pass

    if x == 'unpause':
        pass

    if x == 'mute':
        lasersound = pygame.mixer.Sound('Game/Falco sounds/silence.wav')
        clicksound = pygame.mixer.Sound('Game/Falco sounds/silence.wav')
        explosionsound = pygame.mixer.Sound('Game/Falco sounds/silence.wav')
        deathsound = pygame.mixer.Sound('Game/Falco sounds/silence.wav')
        dingsound1 = pygame.mixer.Sound('Game/Falco sounds/silence.wav')
        dingsound2 = pygame.mixer.Sound('Game/Falco sounds/silence.wav')
        losestocksound = pygame.mixer.Sound('Game/Falco sounds/silence.wav')

    if x == 'unmute':
        lasersound = pygame.mixer.Sound('Game/Falco sounds/laser sound 4.wav')
        clicksound = pygame.mixer.Sound('Game/Falco sounds/click3.wav')
        explosionsound = pygame.mixer.Sound('Game/Falco sounds/explosion2.wav')
        deathsound = pygame.mixer.Sound('Game/Falco sounds/death sound2.wav')
        dingsound1 = pygame.mixer.Sound('Game/Falco sounds/ding1_1.wav')
        dingsound2 = pygame.mixer.Sound('Game/Falco sounds/ding2_1.wav')
        losestocksound = pygame.mixer.Sound('Game/Falco sounds/dsmash.wav')




def music(x):                         #music function
    global menumusic
    global stagemusic
    global musicmute

    if x == 'menu':
        print('menu music')
        menumusic = pygame.mixer.music.load('Game/music/Franks Groove Menu_shorter.mp3')
        pygame.mixer.music.play(-1)   # plays full music

    if x == 'stage':
        print('stage music')
        stagemusic = pygame.mixer.music.load('Game/music/ff_shorter.mp3')
        pygame.mixer.music.play(-1)   # plays full music


    if x == 'pause':
        pygame.mixer.music.pause()

    if x == 'unpause':
        pygame.mixer.music.unpause()

    if x == 'mute':
        pygame.mixer.music.set_volume(0.0)

    if x == 'unmute':
        pygame.mixer.music.set_volume(1.0)





trigger_no_spawn = False
sound_on = True
music_on = True
#main menu func
def main_menu(main_run):
    music('menu')
    global trigger_no_spawn
    global musicmute

    main_on_start = True
    main_on_training = False
    main_on_controls = False
    main_on_settings = False
    main_on_exit = False
    menu_first = True
    togglelag = 0

    on_back = True  #for settings menu
    on_sound = False
    on_music = False
    global sound_on
    global music_on

    menu_controls = False
    menu_settings = False

    while main_run:
        window.fill((0,0,0))
        ballsacks = pygame.key.get_pressed()

        if main_on_start == True:              #main on start
            if menu_first == True:
                togglelag = 21

            if togglelag >= 0 and togglelag <=1 :
                window.blit(mainmenustart[0], (0,0))
            if togglelag >= 2 and togglelag <= 3:
                window.blit(mainmenustart[1], (0,0))
            if togglelag >= 4 and togglelag <= 5:
                window.blit(mainmenustart[2], (0,0))
            if togglelag >= 6 and togglelag <= 7:
                window.blit(mainmenustart[3], (0,0))
            if togglelag >= 8 and togglelag <= 9:
                window.blit(mainmenustart[5], (0,0))

            if togglelag >= 10:

                if togglelag >= 10 and togglelag <= 11:
                    window.blit(mainmenustart[5], (0,0))
                if togglelag >= 12 and togglelag <= 13:
                    window.blit(mainmenustart[6], (0,0))
                if togglelag >= 14 and togglelag <= 15:
                    window.blit(mainmenustart[7], (0,0))
                if togglelag >= 16 and togglelag <= 17:
                    window.blit(mainmenustart[8], (0,0))
                if togglelag >= 18 and togglelag <= 19:
                    window.blit(mainmenustart[9], (0,0))
                if togglelag >= 20:
                    window.blit(mainmenustart[0], (0,0))

                if ballsacks[pygame.K_RETURN]:
                    music('stage')
                    goblin.vel = 2
                    goblin2.vel = -4
                    trigger_no_spawn = False
                    main_run = False

                if  ballsacks[pygame.K_s] or ballsacks[pygame.K_DOWN]:
                    togglelag = 0
                    sounds('dingsound1')
                    main_on_training = True
                    main_on_start = False

                if  ballsacks[pygame.K_w] or ballsacks[pygame.K_UP]:
                    togglelag = 0
                    sounds('dingsound1')
                    main_on_exit = True
                    main_on_start = False



            togglelag = togglelag + 1



        if main_on_training == True:            #main on training
            menu_first = False

            if togglelag >= 0 and togglelag <=1 :
                window.blit(mainmenutraining[0], (0,0))
            if togglelag >= 2 and togglelag <= 3:
                window.blit(mainmenutraining[1], (0,0))
            if togglelag >= 4 and togglelag <= 5:
                window.blit(mainmenutraining[2], (0,0))
            if togglelag >= 6 and togglelag <= 7:
                window.blit(mainmenutraining[3], (0,0))
            if togglelag >= 8 and togglelag <= 9:
                window.blit(mainmenutraining[5], (0,0))

            if togglelag >= 10:

                if togglelag >= 10 and togglelag <= 11:
                    window.blit(mainmenutraining[5], (0,0))
                if togglelag >= 12 and togglelag <= 13:
                    window.blit(mainmenutraining[6], (0,0))
                if togglelag >= 14 and togglelag <= 15:
                    window.blit(mainmenutraining[7], (0,0))
                if togglelag >= 16 and togglelag <= 17:
                    window.blit(mainmenutraining[8], (0,0))
                if togglelag >= 18 and togglelag <= 19:
                    window.blit(mainmenutraining[9], (0,0))
                if togglelag >= 20:
                    window.blit(mainmenutraining[0], (0,0))

                if ballsacks[pygame.K_RETURN]:
                    music('stage')
                    goblin.vel = 0
                    goblin2.vel = 0
                    trigger_no_spawn = True
                    main_run = False


                if  ballsacks[pygame.K_s] or ballsacks[pygame.K_DOWN]:
                    togglelag = 0
                    sounds('dingsound1')
                    main_on_controls = True
                    main_on_training = False

                if ballsacks[pygame.K_w] or ballsacks[pygame.K_UP]:
                    togglelag = 0
                    sounds('dingsound1')
                    main_on_start = True
                    main_on_training = False

            togglelag = togglelag + 1

        if main_on_controls == True:     #main on controls
            menu_first = False

            if togglelag >= 0 and togglelag <=1 :
                window.blit(mainmenucontrols[0], (0,0))
            if togglelag >= 2 and togglelag <= 3:
                window.blit(mainmenucontrols[1], (0,0))
            if togglelag >= 4 and togglelag <= 5:
                window.blit(mainmenucontrols[2], (0,0))
            if togglelag >= 6 and togglelag <= 7:
                window.blit(mainmenucontrols[3], (0,0))
            if togglelag >= 8 and togglelag <= 9:
                window.blit(mainmenucontrols[5], (0,0))

            if togglelag >= 10:

                if togglelag >= 10 and togglelag <= 11:
                    window.blit(mainmenucontrols[5], (0,0))
                if togglelag >= 12 and togglelag <= 13:
                    window.blit(mainmenucontrols[6], (0,0))
                if togglelag >= 14 and togglelag <= 15:
                    window.blit(mainmenucontrols[7], (0,0))
                if togglelag >= 16 and togglelag <= 17:
                    window.blit(mainmenucontrols[8], (0,0))
                if togglelag >= 18 and togglelag <= 19:
                    window.blit(mainmenucontrols[9], (0,0))
                if togglelag >= 20:
                    window.blit(mainmenucontrols[0], (0,0))

                if ballsacks[pygame.K_RETURN]:
                    togglelag = 0
                    sounds('dingsound1')
                    menu_controls = True
                    main_on_controls = False


                if  ballsacks[pygame.K_s] or ballsacks[pygame.K_DOWN]:
                    togglelag = 0
                    sounds('dingsound1')
                    main_on_settings = True
                    main_on_controls = False

                if ballsacks[pygame.K_w] or ballsacks[pygame.K_UP]:
                    togglelag = 0
                    sounds('dingsound1')
                    main_on_training = True
                    main_on_controls = False

            togglelag = togglelag + 1


        if main_on_settings == True:        # main on settings
            menu_first = False

            if togglelag >= 0 and togglelag <=1 :
                window.blit(mainmenusettings[0], (0,0))
            if togglelag >= 2 and togglelag <= 3:
                window.blit(mainmenusettings[1], (0,0))
            if togglelag >= 4 and togglelag <= 5:
                window.blit(mainmenusettings[2], (0,0))
            if togglelag >= 6 and togglelag <= 7:
                window.blit(mainmenusettings[3], (0,0))
            if togglelag >= 8 and togglelag <= 9:
                window.blit(mainmenusettings[5], (0,0))

            if togglelag >= 10:

                if togglelag >= 10 and togglelag <= 11:
                    window.blit(mainmenusettings[5], (0,0))
                if togglelag >= 12 and togglelag <= 13:
                    window.blit(mainmenusettings[6], (0,0))
                if togglelag >= 14 and togglelag <= 15:
                    window.blit(mainmenusettings[7], (0,0))
                if togglelag >= 16 and togglelag <= 17:
                    window.blit(mainmenusettings[8], (0,0))
                if togglelag >= 18 and togglelag <= 19:
                    window.blit(mainmenusettings[9], (0,0))
                if togglelag >= 20:
                    window.blit(mainmenusettings[0], (0,0))

                if ballsacks[pygame.K_RETURN]:
                    togglelag = 0
                    sounds('dingsound1')
                    menu_settings = True
                    main_on_settings = False


                if  ballsacks[pygame.K_s] or ballsacks[pygame.K_DOWN]:
                    togglelag = 0
                    sounds('dingsound1')
                    main_on_exit = True
                    main_on_settings = False

                if ballsacks[pygame.K_w] or ballsacks[pygame.K_UP]:
                    togglelag = 0
                    sounds('dingsound1')
                    main_on_controls = True
                    main_on_settings = False

            togglelag = togglelag + 1



        if main_on_exit == True:             #main on exit
            menu_first = False

            if togglelag >= 0 and togglelag <=1 :
                window.blit(mainmenuexit[0], (0,0))
            if togglelag >= 2 and togglelag <= 3:
                window.blit(mainmenuexit[1], (0,0))
            if togglelag >= 4 and togglelag <= 5:
                window.blit(mainmenuexit[2], (0,0))
            if togglelag >= 6 and togglelag <= 7:
                window.blit(mainmenuexit[3], (0,0))
            if togglelag >= 8 and togglelag <= 9:
                window.blit(mainmenuexit[5], (0,0))

            if togglelag >= 10:

                if togglelag >= 10 and togglelag <= 11:
                    window.blit(mainmenuexit[5], (0,0))
                if togglelag >= 12 and togglelag <= 13:
                    window.blit(mainmenuexit[6], (0,0))
                if togglelag >= 14 and togglelag <= 15:
                    window.blit(mainmenuexit[7], (0,0))
                if togglelag >= 16 and togglelag <= 17:
                    window.blit(mainmenuexit[8], (0,0))
                if togglelag >= 18 and togglelag <= 19:
                    window.blit(mainmenuexit[9], (0,0))
                if togglelag >= 20:
                    window.blit(mainmenuexit[0], (0,0))

                if ballsacks[pygame.K_RETURN]:
                    sys.exit()


                if  ballsacks[pygame.K_s] or ballsacks[pygame.K_DOWN]:
                    togglelag = 0
                    sounds('dingsound1')
                    main_on_start = True
                    main_on_exit = False

                if ballsacks[pygame.K_w] or ballsacks[pygame.K_UP]:
                    togglelag = 0
                    sounds('dingsound1')
                    main_on_settings = True
                    main_on_exit = False

            togglelag = togglelag + 1


        if menu_controls:                    #controls menu
            window.blit(controlsmenu[0], (0,0))

            if togglelag > 8:
                if ballsacks[pygame.K_RETURN]:
                    togglelag = 0
                    sounds('dingsound1')
                    main_on_controls = True
                    menu_controls = False


            togglelag = togglelag + 1


        if menu_settings:                    #settings menu
            window.blit(settingsmenu[3], (0,0))

            if togglelag > 8:
                if on_back:
                    if ballsacks[pygame.K_RETURN]:
                        sounds('dingsound1')
                        togglelag = 0
                        main_on_settings = True
                        menu_settings = False

                    if ballsacks[pygame.K_w] or ballsacks[pygame.K_UP]:
                        sounds('dingsound1')
                        togglelag = 0
                        on_back = False
                        on_music = True

                if on_music and togglelag > 8:
                    if ballsacks[pygame.K_RETURN]:
                        sounds('dingsound1')
                        if music_on:
                            music_on = False
                            musicmute = True
                            music('mute')
                        else:
                            music_on = True
                            musicmute = False
                            music('unmute')
                        togglelag = 0
                    if ballsacks[pygame.K_w] or ballsacks[pygame.K_UP]:
                        sounds('dingsound1')
                        on_music = False
                        on_sound = True
                        togglelag = 0
                    if ballsacks[pygame.K_s] or ballsacks[pygame.K_DOWN]:
                        sounds('dingsound1')
                        on_music = False
                        on_back = True
                        togglelag = 0

                if on_sound and togglelag > 8:
                    if ballsacks[pygame.K_RETURN]:
                        if sound_on:
                            sound_on = False
                            sounds('mute')
                        else:
                            sound_on = True
                            sounds('unmute')
                            sounds('dingsound1')
                        togglelag = 0
                    if ballsacks[pygame.K_s] or ballsacks[pygame.K_DOWN]:
                        sounds('dingsound1')
                        on_sound = False
                        on_music = True
                        togglelag = 0

            if on_back and sound_on and music_on:
                window.blit(settingsmenu[3], (0,0))

            if on_back and sound_on and not music_on:
                window.blit(settingsmenu[2], (0,0))

            if on_back and not sound_on and  music_on:
                window.blit(settingsmenu[1], (0,0))

            if on_back and not sound_on and not music_on:
                window.blit(settingsmenu[0], (0,0))

            if on_music and sound_on and music_on:
                window.blit(settingsmenu[7], (0,0))

            if on_music and sound_on and not music_on:
                window.blit(settingsmenu[6], (0,0))

            if on_music and not sound_on and  music_on:
                window.blit(settingsmenu[5], (0,0))

            if on_music and not sound_on and not music_on:
                window.blit(settingsmenu[4], (0,0))

            if on_sound and sound_on and music_on:
                window.blit(settingsmenu[11], (0,0))

            if on_sound and sound_on and not music_on:
                window.blit(settingsmenu[10], (0,0))

            if on_sound and not sound_on and  music_on:
                window.blit(settingsmenu[9], (0,0))

            if on_sound and not sound_on and not music_on:
                window.blit(settingsmenu[8], (0,0))






            togglelag = togglelag + 1





        mentime = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()
        clock.tick(60)


#paused func
def paused():
    window.blit (pausemenu, (75,25))
    pygame.display.update()


#display kill count
def show_kill_count():

    tempnum = str(numkill)

    font = pygame.font.SysFont('freesansbold.tff', 48)
    text = font.render(' ' + tempnum, True, (00,00,00))
    textRect = text.get_rect()
    textRect.center = (945 , 65)

    window.blit(text, textRect)


#Draw function
def redrawGameWindow():
    window.blit(bg, (0,0))  #draw background
    window.blit(bgship1, (bg1pos,50))
    falco.draw(window)
    goblin.draw(window)
    goblin2.draw(window)
    goblin3.draw(window)
    goblin4.draw(window)
    for laser in lasers:
        laser.draw(window)

    show_kill_count()


    pygame.display.update()



#character object creation
falco = player(450, 410, 64, 64)
goblin = enemy(-12, 410, 64, 64, 950)
goblin2 = gob2(950, 410, 64, 64, 1)
goblin3 = gob3(950, 410, 64, 64, 1)
goblin4 = gob4( 0, 0 , 64, 64, 0)

#main loop
letsbeslow = False
laserturnleft = False
laserturnright = False
pureleft = False
pureright = False
unlockmomentumleft = False
unlockmomentumright = False
lasers = []
invincibility = 0
numkill = 0
ispause = False
please_proceed = False
deathwait = False
temptime = 0
lockeventpause = True


main_menu(True)
game_run = True
while game_run:

    clock.tick(60) #60 frames (or goes of the main loop) per second

    if bg1pos <= -500:
        bg1pos = 1200


    bg1pos = bg1pos - 1





    if trigger_no_spawn:
        numkill = 15
        falco.falcostockcount = 1



    #used to be laser stuff here



    if falco.isJump & pureleft:      #retain running momentum when jumping
        unlockmomentumleft = True
    elif falco.isJump & pureright:
        unlockmomentumright = True

    if unlockmomentumright and falco.x < (Screenwidth - falco.width):
        if falco.isJump:
            falco.x = falco.x + falco.vel

    if unlockmomentumleft and falco.x > 0:
        if falco.isJump:
            falco.x = falco.x - falco.vel

    pureright = False
    pureleft = False


    ########################################    enemy hitbox detection, lose a stock!!!!!
    if falco.hitbox[1]  < goblin.hitbox[1] + goblin.hitbox[3] and falco.hitbox[1] + falco.hitbox[3] > goblin.hitbox[1]:
        if (falco.hitbox[0]  > goblin.hitbox[0] and falco.hitbox[0]  < goblin.hitbox[0] + goblin.hitbox[2]) or (falco.hitbox[0] + falco.hitbox[2] > goblin.hitbox[0]) and falco.hitbox[0] + falco.hitbox[2] < goblin.hitbox[0] + goblin.hitbox[2]:
            if falco.alive == True:
                falco.alive = False
                falco.down = False
                falco.angelplat = True
                print("you lose a stock")
                falco.falcostockcount = falco.falcostockcount - 1
                if falco.falcostockcount <= 0:
                    falco.falcostockcount = 0
                    falco.alive = True
                else:
                    sounds('losestocksound')
                invincibility = 0
                falco.y = -100
                falco.x = 475


    if falco.hitbox[1]  < goblin2.hitbox[1] + goblin2.hitbox[3] and falco.hitbox[1] + falco.hitbox[3] > goblin2.hitbox[1]:
        if (falco.hitbox[0]  > goblin2.hitbox[0] and falco.hitbox[0]  < goblin2.hitbox[0] + goblin2.hitbox[2]) or (falco.hitbox[0] + falco.hitbox[2] > goblin2.hitbox[0]) and falco.hitbox[0] + falco.hitbox[2] < goblin2.hitbox[0] + goblin2.hitbox[2]:
            if falco.alive == True:
                falco.alive = False
                falco.angelplat = True
                print("you lose a stock")
                falco.falcostockcount = falco.falcostockcount - 1
                if falco.falcostockcount <= 0:
                    falco.falcostockcount = 0
                    falco.alive = True
                else:
                    sounds('losestocksound')
                invincibility = 0
                falco.y = -100
                falco.x = 475


    if falco.hitbox[1]  < goblin3.hitbox[1] + goblin3.hitbox[3] and falco.hitbox[1] + falco.hitbox[3] > goblin3.hitbox[1]:
        if (falco.hitbox[0]  > goblin3.hitbox[0] and falco.hitbox[0]  < goblin3.hitbox[0] + goblin3.hitbox[2]) or (falco.hitbox[0] + falco.hitbox[2] > goblin3.hitbox[0]) and falco.hitbox[0] + falco.hitbox[2] < goblin3.hitbox[0] + goblin3.hitbox[2]:
            if falco.alive == True:
                falco.alive = False
                falco.angelplat = True
                print("you lose a stock")
                falco.falcostockcount = falco.falcostockcount - 1
                if falco.falcostockcount <= 0:
                    falco.falcostockcount = 0
                    falco.alive = True
                else:
                    sounds('losestocksound')
                invincibility = 0
                falco.y = -100
                falco.x = 475


    if falco.hitbox[1]  < goblin4.hitbox[1] + goblin4.hitbox[3] and falco.hitbox[1] + falco.hitbox[3] > goblin4.hitbox[1]:
        if (falco.hitbox[0]  > goblin4.hitbox[0] and falco.hitbox[0]  < goblin4.hitbox[0] + goblin4.hitbox[2]) or (falco.hitbox[0] + falco.hitbox[2] > goblin4.hitbox[0]) and falco.hitbox[0] + falco.hitbox[2] < goblin4.hitbox[0] + goblin4.hitbox[2]:
            if falco.alive == True:
                falco.alive = False
                falco.angelplat = True
                print("you lose a stock")
                falco.falcostockcount = falco.falcostockcount - 1
                if falco.falcostockcount <= 0:
                    falco.falcostockcount = 0
                    falco.alive = True
                else:
                    sounds('losestocksound')
                invincibility = 0
                falco.y = -100
                falco.x = 475
                goblin4.hit()
                sounds('explosionsound')
            else:
                goblin4.hit()
                sounds('explosionsound')




    for event in pygame.event.get():  #makes the x-out button work
        if event.type == pygame.QUIT:
            game_run = False


    keys = pygame.key.get_pressed() #creates list of keys for button pressed

    if keys[pygame.K_s]:     #down press for Fast Falling
        falco.down = True



    if keys[pygame.K_a] and falco.x > 0:  #what to do when left is pressed
        if not falco.isJump and falco.laserlag == 0:
            falco.x = falco.x - falco.vel
            falco.left = True
            falco.right = False
            falco.standing = False
            pureleft = True
        if falco.isJump:
            if unlockmomentumleft:
                pass
            else:
                if letsbeslow:                                #allows aerial drift
                    falco.x = falco.x - ((falco.vel / 4))     #tilt
                else:
                    falco.x = falco.x - (falco.vel / 2)       #full tilt
            laserturnleft = True
            laserturnright = False


    elif keys[pygame.K_d] and falco.x < (Screenwidth - falco.width):  #what to do when right is pressed
        if not falco.isJump and falco.laserlag == 0:
            falco.x = falco.x + falco.vel
            falco.right = True
            falco.left = False
            falco.standing = False
            pureright = True
        if falco.isJump:
            if unlockmomentumright:
                pass
            else:
                if letsbeslow:                                 #allows aerial drift
                    falco.x = falco.x + ((falco.vel / 4) )     #tilt
                else:
                    falco.x = falco.x + (falco.vel / 2)        #full tilt
            laserturnright = True
            laserturnleft = False

    else:     #what to do when nothing is pressed
        falco.standing = True
        falco.walkCount = 0

    if keys[pygame.K_SPACE] and falco.laserlag == 0:       #shoots laser when space is pressed
        if laserturnleft:
            facing = -1
            falco.left = True
            falco.right = False
            falco.turnonlandLeft = True
        elif laserturnright:
            facing = 1
            falco.right = True
            falco.left = False
            falco.turnonlandRight = True
        elif falco.left:
            facing = -1
        else:
            facing = 1

        if not falco.isJump and not falco.angelplat:
            falco.unlockstandinglaser = True
        else:
            falco.unlockaeriallaser = True

    if not falco.isJump:
        laserturnright = False
        laserturnleft = False





    if keys[pygame.K_LSHIFT] :             #what to do when walk is pressed
        if not falco.isJump:
            falco.vel = 2
        if falco.isJump:
            letsbeslow = True
    else:
        falco.vel = 4.5
        letsbeslow = False


    #######################################LASER STUFF BELOW


    if falco.unlockstandinglaser:                 #  trigger standing laser
        falco.laserlag += 1
        if falco.laserlag == 17:
            sounds('clicksound')
        if falco.laserlag == 23:
            sounds('lasersound')
            if falco.right == True:
                lasers.append(projectile(round((falco.x + falco.width //2) + 5), round((falco.y + falco.height //2) + 5 ), facing ))
            if falco.left == True:
                lasers.append(projectile(round((falco.x - falco.width  //2) + 5), round((falco.y + falco.height //2) + 5 ), facing ))

        if falco.laserlag == 57:
            falco.unlockstandinglaser = False
            falco.laserlag = 0


    if falco.unlockaeriallaser:        #trigger aerial laser
        falco.laserlag += 1
        if falco.laserlag == 7:
            sounds('clicksound')
        if falco.laserlag == 13:
            sounds('lasersound')
            if falco.right == True:
                lasers.append(projectile(round((falco.x + falco.width //2) + 5), round((falco.y + falco.height //2) + 5 ), facing ))
            if falco.left == True:
                lasers.append(projectile(round((falco.x - falco.width //2) + 5), round((falco.y + falco.height //2) + 5 ), facing ))

        if falco.laserlag == 35:
            falco.unlockaeriallaser = False
            falco.laserlag = 0



    for laser in lasers:                #hitbox detection for laser
        if laser.hitbox[1]  < goblin.hitbox[1] + goblin.hitbox[3] and laser.hitbox[1] + laser.hitbox[3] > goblin.hitbox[1]:
            if (laser.hitbox[0]  > goblin.hitbox[0] and laser.hitbox[0]  < goblin.hitbox[0] + goblin.hitbox[2]) or (laser.hitbox[0] + laser.hitbox[2] > goblin.hitbox[0]) and laser.hitbox[0] + laser.hitbox[2] < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                sounds('explosionsound')
                numkill = numkill + 1
                lasers.pop(lasers.index(laser))
                laser.laseralive = False

    for laser in lasers:                #hitbox detection for laser
        if laser.hitbox[1]  < goblin2.hitbox[1] + goblin2.hitbox[3] and laser.hitbox[1] + laser.hitbox[3] > goblin2.hitbox[1]:
            if (laser.hitbox[0]  > goblin2.hitbox[0] and laser.hitbox[0]  < goblin2.hitbox[0] + goblin2.hitbox[2]) or (laser.hitbox[0] + laser.hitbox[2] > goblin2.hitbox[0]) and laser.hitbox[0] + laser.hitbox[2] < goblin2.hitbox[0] + goblin2.hitbox[2]:
                goblin2.hit()
                sounds('explosionsound')
                numkill = numkill + 1
                lasers.pop(lasers.index(laser))
                laser.laseralive = False

    for laser in lasers:                #hitbox detection for laser
        if laser.hitbox[1]  < goblin3.hitbox[1] + goblin3.hitbox[3] and laser.hitbox[1] + laser.hitbox[3] > goblin3.hitbox[1]:
            if (laser.hitbox[0]  > goblin3.hitbox[0] and laser.hitbox[0]  < goblin3.hitbox[0] + goblin3.hitbox[2]) or (laser.hitbox[0] + laser.hitbox[2] > goblin3.hitbox[0]) and laser.hitbox[0] + laser.hitbox[2] < goblin3.hitbox[0] + goblin3.hitbox[2]:
                if goblin3.shield == False:
                    numkill = numkill + 1
                goblin3.hit()
                sounds('explosionsound')
                lasers.pop(lasers.index(laser))
                laser.laseralive = False

    for laser in lasers:                #hitbox detection for laser
        if laser.hitbox[1]  < goblin4.hitbox[1] + goblin4.hitbox[3] and laser.hitbox[1] + laser.hitbox[3] > goblin4.hitbox[1]:
            if (laser.hitbox[0]  > goblin4.hitbox[0] and laser.hitbox[0]  < goblin4.hitbox[0] + goblin4.hitbox[2]) or (laser.hitbox[0] + laser.hitbox[2] > goblin4.hitbox[0]) and laser.hitbox[0] + laser.hitbox[2] < goblin4.hitbox[0] + goblin4.hitbox[2]:
                if goblin3.shield == False:
                    numkill = numkill + 1
                goblin4.hit()
                sounds('explosionsound')
                lasers.pop(lasers.index(laser))
                laser.laseralive = False

                #laser out of bounds
        if laser.x < 1000 and laser.x > 0:
            laser.x += laser.vel
        else:
            if laser.laseralive == True:
                lasers.pop(lasers.index(laser))

                ############################################### LASER STUFF ABOVE




    if keys[pygame.K_p]:     #################  pause game
        please_proceed = True
        lockeventpause = False


    if please_proceed and not keys[pygame.K_p]:
        if ispause == False:
            if lockeventpause == False:
                if falco.falcostockcount > 0:
                    print('we are pauseing')
                    ispause = True
                    music('pause')
                    sounds('pause')
                    please_proceed = False

            if lockeventpause == True:
                please_proceed = False
                lockeventpause = False




        elif ispause == True:
            ispause = False
            please_proceed = False


    while ispause:

        paused()

        fuckme = pygame.key.get_pressed()

        if fuckme[pygame.K_a] and fuckme[pygame.K_a] and fuckme[pygame.K_d] and fuckme[pygame.K_SPACE]:       # return to main menu from pause
            ispause = False
            falco.falcostockcount = 0



        if fuckme[pygame.K_p]:
            please_proceed = True

        if please_proceed and not fuckme[pygame.K_p]:
            if ispause == False:
                ispause = True
                please_proceed = False
            elif ispause == True:
                print('we are unpauseing')
                ispause = False
                music('unpause')
                sounds('unpause')
                please_proceed = False


        for event in pygame.event.get():  #makes the x-out button work
            if event.type == pygame.QUIT:
                ispause = False
                game_run = False


    #death wait loop
    if falco.falcostockcount <= 0:
        deathwait = True
        sounds('deathsound')
        music('pause')

    temptime = pygame.time.get_ticks()

    while deathwait:
        if pygame.time.get_ticks() == (temptime + 3000):
            deathwait = False


        for event in pygame.event.get():  #makes the x-out button work
            if event.type == pygame.QUIT:
                ispause = False
                game_run = False




            #redrawGameWindow()   # calls the big draw function






    if falco.alive == False:             #angle platform
        if falco.angelplat == True:


            if falco.y < 410:                           # falling
                if falco.down:             #if we fast fall
                    if falco.y > 402:
                        falco.y = 410
                    else:
                        falco.y += ((60/7) * 1.29 )         # + (100/14 * .129)) is real falco FF rate
                        print('fast fall initiated' + str (falco.y))
                else:
                    falco.y += (60/6)                    #normal fall rate

                if falco.y >= 410:
                    falco.y = 410
                    if falco.unlockaeriallaser:
                        falco.unlockaeriallaser = False
                        falco.laserlag = 0
                    falco.angelplat = False




        if invincibility == 300:
            falco.alive = True
            invincibility = 0
        else:
            invincibility = invincibility + 1

        if invincibility > 0 and invincibility < 300:
            falco.iframes = True
        else:
            falco.iframes = False




    if not (falco.isJump):   #if we are not jumping


        if keys[pygame.K_m] and falco.angelplat == False and falco.laserlag == 0:   #what to do when jump is pressed
            falco.isJump = True
            falco.walkCount = 0


    else:                                     #if we are jumping,  calculating falco short hop
        if falco.jumpCount <= 6:                 # jump squat
            falco.jumpSquat = True
            falco.jumpCount += 1
            falco.turnonlandRight = False
            falco.turnonlandLeft = False
        elif falco.jumpCount > 6 and falco.jumpCount <= 16:      #going up
            falco.y -= 8
            falco.jumpCount += 1
            falco.jumpSquat = False
        elif falco.jumpCount == 17:         #apex height  of 80 from bottom
            falco.jumpCount +=1
            falco.down = False
        elif falco.jumpCount > 17 and falco.jumpCount <= 31:   #on the way down
            if falco.down:             #if we fast fall
                if falco.y > 402:
                    falco.y = 410
                    falco.jumpCount = 32
                else:
                    falco.y += ((60/7) * 1.29 )         # + (100/14 * .129)) is real falco FF rate
                #print('fast fall initiated' + str(falco.jumpCount))
            else:                                     # slow fall after apex


                if falco.jumpCount == 18 or falco.jumpCount == 19:
                    falco.y += 1
                if falco.jumpCount == 20 or falco.jumpCount == 21:
                    falco.y += 2
                if falco.jumpCount == 22 or falco.jumpCount == 23:
                    falco.y += 3
                if falco.jumpCount == 24 or falco.jumpCount == 25:
                    falco.y += 4
                if falco.jumpCount > 25:            #normal fall rate
                    falco.y += (60/6)

            falco.jumpCount += 1


            #if falco.y == 410   we are on the ground

        else:      #what to do upon landing

            falco.isJump = False
            falco.down = False
            falco.jumpCount = 0
            unlockmomentumright = False
            unlockmomentumleft = False
            if falco.unlockaeriallaser:
                falco.laserlag = 0
            falco.unlockaeriallaser = False
            if falco.turnonlandLeft:
                falco.left = True
                falco.right = False
            if falco.turnonlandRight:
                falco.left = False
                falco.right = True



    if not falco.left and not falco.right:
        falco.right = True



    if falco.falcostockcount == 0:  #if falco lost all four stocks, reset all positions
        numkill = 0
        lockeventpause = True
        main_menu(True)
        bg1pos = 270
        falco.falcostockcount = 4
        falco.isJump = False
        falco.down = False
        falco.jumpCount = 0
        falco.x = 450
        falco.y = 410
        goblin.x = 1
        falco.laserlag = 0
        falco.angelplat = False
        for laser in lasers:
            lasers.pop(lasers.index(laser))
            laser.laseralive = False
        falco.unlockaeriallaser = False
        falco.unlockstandinglaser = False



    if numkill < 15:
        goblin2.alive = False
        goblin2.exploding = 9999

    if numkill < 85:
        goblin3.alive = False
        goblin3.exploding = 9999

    if numkill < 30:
        goblin4.alive = False
        goblin4.exploding = 9999



    redrawGameWindow()   # calls the big draw function





pygame.quit()  #kills code when loop ends
