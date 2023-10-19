#from level import level_one
from state import State
from label import Label
from level import Level
import pygame
print("yo cuzzbob")

#FIXME Are we gonna chnge this to just level
class LevelSelection(State):
    def __init__(self, game):
        State.__init__(self, game)
        #Initial setup
        self.game = game
        self.screen = game.screen
        self.screen_width, self.screen_height = self.screen.get_size()
        self.prev_state = None
        self.levels_display = {"Level1" : "imgpath", "Level2" : "imgpath", "Level3" : "imgpath", "Level4" : "imgpath"}
        self.num_levels = len(self.levels_display)
        self.currentlySelected = ["", ""]
        self.level_rects = []
        self.botleft_rect = pygame.rect.Rect(0, self.screen_height/2, self.screen_width/2, self.screen_height/2)
        self.botright_rect = pygame.rect.Rect(self.screen_width/2, self.screen_height/2, self.screen_width/2, self.screen_height/2)
        self.hover_location = -1
        self.popOut =1
        self.labels = []
        self.font = pygame.font.SysFont('Arial', 25)
        self.level_state = None
        self.count = 1
        self.currentMap = Label(self.game.screen, 0, 0, 1, .5, button=True, text= self.currentlySelected) #, image="Assets/start2.png", hover_image="Assets/start.png"

        #self.create_levels()
        #self.create_labels()
        self.create_level_labels()

    #Set locations to be selected or hovered with mouse pos
    def update(self, actions):
        x, y = pygame.mouse.get_pos()
        self.check_hover_location(x, y)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.level_state.enter_state()
                if event.key == pygame.K_ESCAPE:
                    self.game.running = False

                


      #  if()
        #if actions["level_selection"]:
            #self.game.level_one.enter_state()
    def render(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        #self.render_levels()
        self.render_level_labels()
        #self.render_labels()
        #pygame.display.update()

    def create_labels(self):
        for index in range(1,3):
            label_rect = pygame.rect.Rect(self.screen_width * ((index-1)/2) +10, self.screen_height - self.screen_height/8, self.screen_width/4, self.screen_height/2)
            self.labels.append(label_rect)

    def create_level_labels(self):
        for index, level in enumerate(self.levels_display):
            txt = "Map {}".format(index+1)
            map = Label(self.game.screen, 0, .5+ index/(len(self.levels_display) * 2), 1, 1/(len(self.levels_display) * 2), button=True, text= txt) #, image="Assets/start2.png", hover_image="Assets/start.png"
            self.labels.append(map)
            self.level_rects.append(map.rect)



    def create_levels(self):
        for index, level in enumerate(self.levels_display):
            image_rect = pygame.rect.Rect(self.screen_width * (index/self.num_levels), 0, self.screen_width/self.num_levels, self.screen_height/2)
            self.level_rects.append(image_rect)
    
    def render_labels(self):
        for index in range(len(self.labels)):
            text_surface = self.font.render('Player' + str(index+1), True, (255,0,0))
            label_rect = pygame.rect.Rect(self.screen_width * ((index)/2) +10, self.screen_height - self.screen_height/8, self.screen_width/4, self.screen_height/2)
            self.labels[index] = label_rect
            self.screen.blit(text_surface, (self.labels[index].x, self.labels[index].y))


    def render_level_labels(self):
        for index, label in enumerate(self.labels):
            if self.hover_location == index:
                label.hover_label()  
            else:
                label.render_label() 

        if self.hover_location != -1:
            self.currentMap.text = self.labels[self.hover_location].text
            self.currentMap.render_label()

    def render_levels(self):
        for index, rect in enumerate(self.level_rects):
            enhance = 1
            if index == self.hover_location:
                enhance = 1.2
            image_rect = pygame.rect.Rect(self.screen_width * (index/self.num_levels), 0, enhance * self.screen_width/self.num_levels, enhance *self.screen_height/2)
            self.level_rects[index] = image_rect
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
                    self.screen.blit(self.levels_display[char], image_rect)

                if(index == 1):
                    image_rect = self.botright_rect
                    image_rect.x = image_rect.w = (4*self.screen_width)/6, self.screen_width/6
                    self.screen.blit(self.levels_display[char], image_rect)

    def check_hover_location(self, xlo, ylo):
        for index, rect in enumerate(self.level_rects):
            print(xlo, ylo)
            if(xlo <= rect.x + rect.w and rect.x <= xlo) and (ylo <= rect.y + rect.h and rect.y <= ylo):
                self.hover_location = index
                return


    def enter_state(self):
        print("level state")
        pygame.display.set_caption('Choose Your Level')

        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)

    def exit_state(self):
        self.game.state_stack.pop()