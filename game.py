import pygame
from settings import *
from level import Level
from title import Title
class game():
    def __init__(self):

        #Initial screen setup
        pygame.init()
        pygame.mixer.init()
       # pygame.mixer.music.load("Brawl_Theme.mp3")
        self.tile_size = tile_size
        self.background_colour = (100, 100, 252)
        self.screen_width, self.screen_height =  1028, 720 #len(level[0]) *tile_size,  len(level) * tile_size,
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.full_screen_ratio = (0.68, 0.76)
        self.state_stack = []
       # self.events = pygame.event.get()

        #States
        #self.title = Title(self)

        #Graphics
        pygame.display.set_caption('PROF BRAWLLLLLLLL!!!!!!!')
        self.screen.fill(self.background_colour)

        #Music control
        self.playing_music = False

        #Game logic
        self.actions = {"left": False, "right": False, "up" : False, "down" : False, "action1" : False, "action2" : False, "start" : False, "quit": False, "level_selection": False, "level_one": False}
        self.running = True

    def update(self):
        self.state_stack[-1].update(self.actions)

    def render(self):
        self.state_stack[-1].render()
        #self.clock.tick(self.FPS)
        pygame.display.flip()

    def play_music(self):
        if not self.playing_music:
            pygame.mixer.music.play(-1)
            self.playing_music = True

    #Main running loop
    def game_loop(self): 
        while self.running:
            #self.get_events()

            self.update()
            self.render()
            self.screen.fill((99, 100, 252))
          #  self.level.run()
         #   self.play_music()
            self.clock.tick(self.FPS)

g = game()
title = Title(g)
g.state_stack.append(title)
g.game_loop()
pygame.display.quit()


#FIXME
#PLAYER:
#Input player player interactions (attacks, movement)
#Make players move
#Find player sprite images (walking, fighting, jumping, etc)
#Input player sprite animations
#Set player damage and health and shield and abilities
#Keep track of player stats

#MAP SCREEN
#Fix zoom and pan (work on aspect ratio conversions of platforms & characters)
#Add health bar
#implement multiple rounds??

#CHAR SELECTION SCREEN
#Add character banner
#Fix 'floating' labels when character chosen

#MISC
#Create custom GUI elements
#Fix music on different states & sound effects
#Make various map layouts
#Eat poop
#Add end screen
#GET PROF PERMISSION
#clean up screens (ie title)




