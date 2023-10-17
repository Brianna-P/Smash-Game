import pygame
from state import State
from character_selection import CharacterSelection
from label import Label

class Title(State):
    def __init__(self, game):

        State.__init__(self, game)
        self.game = game
        self.prev_state = None
        self.background_colour = (20, 9, 252)
        
        self.hovering_start = False
        self.hovering_quit = False
        
        #self.CharacterSelect = CharacterSelection(game)


    def update(self, actions):
        screen_width, screen_height= self.game.screen.get_size() 
        mouse_x, mouse_y = pygame.mouse.get_pos()

        self.start_button = Label(self.game.screen, (screen_width / 2) - 150, (screen_height / 2) -50 + 100, 300, 100, button=True, text="START", image="start.png", hover_image="start2.png")
        self.quit_button = Label(self.game.screen, (screen_width / 2) - 150, (screen_height / 2) -50 - 100, 300, 100, button=True, text="START", image="start2.png", hover_image="start.png")

        for event in pygame.event.get():
            if(abs(mouse_x - screen_width/2) <= 150 and abs(mouse_y- ((screen_height / 2) + 50)) <= 50):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.game.running = False
                else:
                    self.hovering_start = True
            else: 
                self.hovering_start = False
            if(abs(mouse_x - screen_width/2) <= 105 and abs(mouse_y- ((screen_height / 2) - 150)) <= 50):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    new_state = CharacterSelection(self.game)
                    new_state.enter_state()
                else:
                    self.hovering_quit = True
            else: 
                self.hovering_quit = False
    
    def render(self):
        self.game.screen.fill((211,211,211))
        pygame.display.set_caption("PROF title!!!!!!")
        
        if(self.hovering_start):
            self.start_button.hover_label()
        else:
            self.start_button.render_label()

        if(self.hovering_quit):
            self.quit_button.hover_label()
        else:
            self.quit_button.render_label()
    
        
    #   play >> characterselection >> map select >> level.enterstate(p1, p2)

    


        
