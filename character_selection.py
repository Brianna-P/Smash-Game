#from level import level_one
from state import State
from label import Label
import pygame
class CharacterSelection(State):
    def __init__(self, game):
        State.__init__(self, game)
        #Initial setup
        self.game = game
        self.screen = game.screen
        self.screen_width, self.screen_height = self.screen.get_size()
        self.prev_state = None
        self.characters_display = {"Character1" : "imgpath", "Character2" : "imgpath"}
        #self.character_images = [pygame.image.load(self.characters_display["Character1"]), pygame.image.load(self.characters_display["Character2"])]
        self.num_characters = len(self.characters_display)
        self.currentlySelected = ["", ""]
        self.char_rects = []
        self.botleft_rect = pygame.rect.Rect(0, self.screen_height/2, self.screen_width/2, self.screen_height/2)
        self.botright_rect = pygame.rect.Rect(self.screen_width/2, self.screen_height/2, self.screen_width/2, self.screen_height/2)
        self.hover_location = -1
        self.popOut =1
        self.labels = []
        self.font = pygame.font.SysFont('Arial', 25)
        self.create_characters()
        self.create_labels()

    #Set locations to be selected or hovered with mouse pos
    def update(self, actions):
        x, y = pygame.mouse.get_pos()
        self.check_hover_location(x, y)

      #  if()
        #if actions["level_selection"]:
            #self.game.level_one.enter_state()
    def render(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        self.render_characters()
        self.render_labels()
        #pygame.display.update()

    def create_labels(self):
        for index in range(1,2):
            #current_image = self.character_images[index]
            #image_rect = current_image.get_rect()
            label_rect = pygame.rect.Rect(self.screen_width * index, self.screen_height - self.screen_height/8, self.screen_width/4, self.screen_height/2)
            self.labels.append(label_rect)

    def create_characters(self):
        for index, character in enumerate(self.characters_display):
            #current_image = self.character_images[index]
            #image_rect = current_image.get_rect()
            image_rect = pygame.rect.Rect(self.num_characters * index, 0, self.screen_width/self.num_characters, self.screen_height/2)
            self.char_rects.append(image_rect)
            #image_rect.x, image_rect.y, image_rect.w, image_rect.h = self.num_characters * index, 0, self.screen_width/self.num_characters, self.screen_height
            #self.screen.blit(current_image, image_rect)
    
    def render_labels(self):
        for index in range(len(self.labels)):
            self.screen.blit(self.font.render('Player' + str(index), True, (255,0,0)), self.labels[index])


    def render_characters(self):
        for index, rect in enumerate(self.char_rects):
            enhance = 1
            if index == self.hover_location:
                ehance = 1.2
            image_rect = pygame.rect.Rect(self.num_characters * index, 0, enhance * self.screen_width/self.num_characters, enhance *self.screen_height/2)
            pygame.draw.rect(self.screen, (0, 0 ,0), image_rect, 1)
        self.botleft_rect = pygame.rect.Rect(0, self.screen_height/2, self.screen_width/2, self.screen_height/2)
        self.botright_rect = pygame.rect.Rect(self.screen_width/2, self.screen_height/2, self.screen_width/2, self.screen_height/2)
                
        pygame.draw.rect(self.screen, (211, 211, 211), self.botright_rect, 1)
        pygame.draw.rect(self.screen, (211, 211, 211), self.botright_rect, 1)
#Implement the ability to choose the image when selected
        for index, char in enumerate(self.currentlySelected):
            if(char != ""):
                if(index == 0):
                    image_rect = self.botleft_rect
                    image_rect.x, image_rect.w = (2*self.screen_width)/6, self.screen_width/6
                    self.screen.blit(self.characters_display[char], image_rect)

                if(index == 1):
                    image_rect = self.botright_rect
                    image_rect.x = image_rect.w = (4*self.screen_width)/6, self.screen_width/6
                    self.screen.blit(self.characters_display[char], image_rect)

    def check_hover_location(self, x, y):
    
        for index, rect in enumerate(self.char_rects):
            if(rect.x + x < rect.x + rect.w) and (rect.y + y < rect.y + rect.h):
                self.hover_location = index
                return
        self.hover_location = -1


    def enter_state(self):
        print("char state")
        pygame.display.set_caption('Choose Your Character')

        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)

    def exit_state(self):
        self.game.state_stack.pop()