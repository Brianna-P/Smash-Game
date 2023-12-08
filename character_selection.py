#from level import level_one
from state import State
from label import Label
from level import Level
from player import Player
from level_selection import LevelSelection
import pygame
class CharacterSelection(State):
    def __init__(self, game):
        State.__init__(self, game)
        #Initial setup
        self.game = game
        self.screen = game.screen
        self.screen_width, self.screen_height = self.screen.get_size()
        self.prev_state = None
        self.characters_display = {"Character1" : "Assets/option1.png", "Character2" : "Assets/option2.png", "Character3" : "Assets/option3.png", "Character4" : "Assets/option4.png"}
        self.character_images = [pygame.image.load(self.characters_display["Character1"]), pygame.image.load(self.characters_display["Character2"])]
        self.num_characters = len(self.characters_display)
        self.currently_selected = ["", ""]
        self.char_rects = []
        self.botleft_rect = pygame.rect.Rect(0, self.screen_height/2, self.screen_width/2, self.screen_height/2)
        self.botright_rect = pygame.rect.Rect(self.screen_width/2, self.screen_height/2, self.screen_width/2, self.screen_height/2)
        self.hover_location = -1
        self.button_hover_location = -1
        self.popOut =1
        self.labels = []
        self.font = pygame.font.SysFont('Arial', 25)
        #self.level_select_state = LevelSelection(self.game)
        #self.level_state = Level(game, "option4.png", "option2.png", 1)
        self.count = 1
        self.player_chosen_queue = []
        self.create_characters()
        self.create_labels()

        #need implement hover location: players chosen, to pass to level in update

    #Set locations to be selected or hovered with mouse pos

    #MOVE BOXES DOWN A BIT for "character selection" banner
    #pop out centered
    def update(self, actions):
        x, y = pygame.mouse.get_pos()
        self.check_hover_location(x, y)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(self.button_hover_location == 0 and self.currently_selected[0] != ""):
                    self.currently_selected[0] = ""
                if(self.button_hover_location == 1 and self.currently_selected[1] != ""):
                    self.currently_selected[1] = ""
                if (self.currently_selected[0] == "" or self.currently_selected[1] == "") and (self.hover_location != -1):
                    if self.currently_selected[0] == "":
                        self.currently_selected[0] = list(self.characters_display.values())[self.hover_location]
                        self.player_chosen_queue.append([list(self.characters_display.keys())[self.hover_location], pygame.time.get_ticks()])
                        self.player1 = list(self.characters_display.keys())[self.hover_location]
                    else:
                        self.currently_selected[1] = list(self.characters_display.values())[self.hover_location]
                        self.player_chosen_queue.append([list(self.characters_display.keys())[self.hover_location], pygame.time.get_ticks()])
                        self.player2 = list(self.characters_display.keys())[self.hover_location]

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if(self.currently_selected[0] != "" and self.currently_selected[1] != ""):
                        p1_selected = Player(1, self.game, str(self.player1), (.4,.5), .1, .05, self.characters_display[self.player1])
                        p2_selected = Player(2, self.game, str(self.player2), (.6,.5), .1, .05, self.characters_display[self.player2])
                        self.level_select_state = LevelSelection(self.game)
                        self.level_select_state.enter_state(p1_selected, p2_selected)
                        #self.level_state.enter_state(self.player1, self.player2, 1)
                if event.key == pygame.K_ESCAPE:
                    self.game.running = False
            if event.type == pygame.QUIT:
                self.game.running = False




      #  if()
        #if actions["level_selection"]:
            #self.game.level_one.enter_state()
    def render(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        self.render_characters()
        self.render_labels()
        self.render_player_chosen()
        #pygame.display.update()

    def create_labels(self):
     #   for index in range(1,3):
     ##       #current_image = self.character_images[index]
      #      #image_rect = current_image.get_rect()
      #      label_rect = pygame.rect.Rect(self.screen_width * ((index-1)/2) +10, self.screen_height - self.screen_height/8, self.screen_width/4, self.screen_height/2)
      #      self.labels.append(label_rect)
        self.player1_undo = Label(self.game.screen, 0.015, 0.915 , 0.07, 0.07, button=True, text="<-", image="Assets/back.png", hover_image="Assets/back2.png")
        self.player2_undo = Label(self.game.screen, 0.515, 0.915, 0.07, 0.07, button=True, text="<-", image="Assets/back.png", hover_image="Assets/back2.png")
        self.back_buttons =  [self.player1_undo,self.player2_undo]
        self.player1_label = Label(self.game.screen, 0.015, 0.87, 0.12, 0.07, button=True, text="Player 1")
        self.player2_label = Label(self.game.screen, 0.515, 0.87, 0.12, 0.07, button=True, text="Player2")
        self.player_labels = [self.player1_label, self.player2_label]


    def create_characters(self):
        for index, character in enumerate(self.characters_display):
            #current_image = self.character_images[index]
            #image_rect = current_image.get_rect()
            image_rect = pygame.rect.Rect(self.screen_width * (index/self.num_characters), 0, self.screen_width/self.num_characters, self.screen_height/2)
            self.char_rects.append(image_rect)
            #image_rect.x, image_rect.y, image_rect.w, image_rect.h = self.num_characters * index, 0, self.screen_width/self.num_characters, self.screen_height
            #self.screen.blit(current_image, image_rect)
    
    def render_labels(self):
        for index, labels in enumerate(self.player_labels):
         #   text_surface = self.font.render('Player' + str(index+1), True, (255,0,0))
         #   label_rect = pygame.rect.Rect(self.screen_width * ((index)/2) +10, self.screen_height - self.screen_height/8, self.screen_width/4, self.screen_height/2)
         #   self.labels[index] = label_rect
         #   self.screen.blit(text_surface, (self.labels[index].x, self.labels[index].y))
            labels.render_label() 

        for index, buttons in enumerate(self.back_buttons):
            if self.button_hover_location == index:
               buttons.hover_label() 
            else:
               buttons.render_label() 
        

    def render_characters(self):
        for index, rect in enumerate(self.char_rects):
            enhance = 1
            if index == self.hover_location:
                enhance = 1.2
          #  txt = "Character" + str(index)
            txt = "Character{}".format(index+1)
            #txt.format(ind = index)
            img = pygame.image.load(self.characters_display[txt]).convert_alpha()
            image_rect = pygame.rect.Rect(self.screen_width * (index/self.num_characters), 0, enhance * self.screen_width/self.num_characters, enhance *self.screen_height/2)
            self.screen.blit(pygame.transform.scale(img, (image_rect.w, image_rect.h)), image_rect)
            self.char_rects[index] = image_rect
            #pygame.draw.rect(self.screen, (0, 0 ,0), image_rect, 1)
        self.botleft_rect = pygame.rect.Rect(0, self.screen_height/2, self.screen_width/2, self.screen_height/2)
        self.botright_rect = pygame.rect.Rect(self.screen_width/2, self.screen_height/2, self.screen_width/2, self.screen_height/2)
                
        pygame.draw.rect(self.screen, (211, 211, 211), self.botright_rect, 1)
        pygame.draw.rect(self.screen, (211, 211, 211), self.botright_rect, 1)
#Implement the ability to choose the image when selected
        for index, char in enumerate(self.currently_selected):
            if(char != ""):
                if(index == 0):
                    img = pygame.image.load(self.currently_selected[0]).convert_alpha()
                    image_rect = self.botleft_rect
                    image_rect.x, image_rect.w = (self.screen_width)/6, self.screen_width/6
                    self.screen.blit(pygame.transform.scale(img, (image_rect.w, image_rect.h)), image_rect)

                if(index == 1):
                    img = pygame.image.load(self.currently_selected[1]).convert_alpha()
                    image_rect = self.botright_rect
                    image_rect.x, image_rect.w = (4*self.screen_width)/6, self.screen_width/6
                    self.screen.blit(pygame.transform.scale(img, (image_rect.w, image_rect.h)), image_rect)

    def check_hover_location(self, xlo, ylo):
        for index, rect in enumerate(self.char_rects):
            if(xlo <= rect.x + rect.w and rect.x <= xlo) and (ylo <= rect.y + rect.h and rect.y <= ylo):
                self.hover_location = index
                return
        self.hover_location = -1
        for index, button in enumerate(self.back_buttons):
            if(xlo <= button.rect.x + button.rect.w and button.rect.x <= xlo) and (ylo <= button.rect.y + button.rect.h and button.rect.y <= ylo):
                self.button_hover_location = index
                return
        self.button_hover_location = -1


    def enter_state(self):
        print("char state")
        pygame.display.set_caption('Choose Your Character')

        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)

    def exit_state(self):
        self.game.state_stack.pop()




    def render_player_chosen(self):
        for x in range(len(self.player_chosen_queue)):
            if (pygame.time.get_ticks() - self.player_chosen_queue[x][1])/1000 < 3:
                #xx yy pypgame tick, index
                text_surface = self.font.render(self.player_chosen_queue[x][0], True, (0,0,0))
                text_rect = text_surface.get_rect()
                text_rect.x = self.screen_width/2 - text_rect.w/2
                text_rect.y = self.screen_height/2 - text_rect.h/2
                pygame.transform.scale(text_surface, (50, 50))
                self.screen.blit(text_surface, text_rect)
            else:
                self.player_chosen_queue.pop(x)
                break