import pygame
from state import State
from character_selection import CharacterSelection
from label import Label


#FIXME try resizing screen with labels. Prolly wont resize correctly
#FIXME take out labels
class Title(State):
    def __init__(self, game):

        State.__init__(self, game)
        self.game = game
        self.prev_state = None
        self.background_colour = (20, 9, 252)
        self.screen_width, self.screen_height= self.game.screen.get_size()
        self.hovering_start = False
        self.hovering_quit = False
        self.start_button = Label(self.game.screen, 0.354, 0.431 , 0.2918, 0.139, button=True, text="START", image="Assets/start2.png", hover_image="Assets/start.png")
        self.quit_button = Label(self.game.screen, 0.354, 0.431 + 0.15, 0.2918, 0.139, button=True, text="START", image="Assets/start2.png", hover_image="Assets/start.png")
        self.hover_location = -1
        self.labels = [self.start_button, self.quit_button]
        self.screen_width, self.screen_height = self.game.screen.get_size()
        self.start_rect = pygame.rect.Rect(self.screen_width/2, (2*self.screen_height)/3, 300, 100)
        self.quit_rect = pygame.rect.Rect(self.screen_width/2, (2*self.screen_height)/3, 300, 100)
        #self.CharacterSelect = CharacterSelection(game)
        #self.create_labels()


    def update(self, actions):
       # print(self.game.screen.get_size())
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.screen_width, self.screen_height = self.game.screen.get_size()
        
        #self.render_labels()
        self.check_hover_location(mouse_x, mouse_y)
        
        if(mouse_x <= self.start_button.rect.x + self.start_button.rect.w and self.start_button.rect.x <= mouse_x) and (mouse_y <= self.start_button.rect.y + self.start_button.rect.h and self.start_button.rect.y <= mouse_y):
            self.hovering_start = True
        else:
            self.hovering_start = False

        if(mouse_x <= self.quit_button.rect.x + self.quit_button.rect.w and self.quit_button.rect.x <= mouse_x) and (mouse_y <= self.quit_button.rect.y + self.quit_button.rect.h and self.quit_button.rect.y <= mouse_y):
              self.hovering_quit = True
        else:
            self.hovering_quit = False
            
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.hover_location != -1:
                    if self.hover_location == 0:
                        char_state = CharacterSelection(self.game)
                        char_state.enter_state()
                    if self.hover_location == 1:
                        self.game.running = False
               # if(mouse_x <= self.quit_button.rect.x + self.quit_button.rect.w and self.quit_button.rect.x <= mouse_x) and (mouse_y <= self.quit_button.rect.y + self.quit_button.rect.h and self.quit_button.rect.y <= mouse_y):
               # if(mouse_x <= self.start_button.rect.x + self.start_button.rect.w and self.start_button.rect.x <= mouse_x) and (mouse_y <= self.start_button.rect.y + self.start_button.rect.h and self.start_button.rect.y <= mouse_y):
                    #new_state = CharacterSelection(self.game)
    
    def render(self):
        self.game.screen.fill((211,211,211))
        self.screen_width, self.screen_height = self.game.screen.get_size()
        pygame.display.set_caption("PROF title!!!!!!")
        self.render_labels()
        
    def create_labels(self):
        for index in range(1,2):
            #current_image = self.character_images[index]
            #image_rect = current_image.get_rect()
            temp_label = Label(self.game.screen, 0.354, 0.431 + index * 0.15, 0.2918, 0.139, button=True, text="START", image="Assets/start2.png", hover_image="Assets/start.png")
            self.labels.append(temp_label)

    def render_labels(self):
        for index, label in enumerate(self.labels):
            if self.hover_location == index:
              #  it disappear
               # self.screen.blit(pyg
               # ame.transform.scale(img, (image_rect.w, image_rect.h)), image_rect)
               label.hover_label() 
                
            else:
               # image_surface = pygame.image.load(self.image).convert_alpha()
                #self.screen.blit(pygame.transform.scale(image_surface, (self.w, self.h)), self.rect)
                label.render_label() 


    def check_hover_location(self, xlo, ylo):
        for index, label in enumerate(self.labels):
            if(xlo <= label.rect.x + label.rect.w and label.rect.x <= xlo) and (ylo <= label.rect.y + label.rect.h and label.rect.y <= ylo):
                self.hover_location = index
                return
        self.hover_location = -1

        
    #   play >> characterselection >> map select >> level.enterstate(p1, p2)

    


        
