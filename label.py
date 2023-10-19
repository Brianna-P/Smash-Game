import pygame

class Label():

    def __init__(self, screen, x, y, w, h, button = False, text = "", image = "", hover_image = ""):
        self.screen = screen 
        self.button = button 
        self.text = text
        self.image = image
        self.x=x
        self.y = y
        self.w = w
        self.h = h
        self.hover_image = hover_image
        self.screen_width, self.screen_height = self.screen.get_size()
        self.rect = pygame.rect.Rect(x, y, w, h)
        self.font = pygame.font.SysFont('Arial', 25)
        self.rect = pygame.rect.Rect(self.x * self.screen_width, self.y * self.screen_height, self.w * self.screen_width, self.h * self.screen_height)



    
    
    def render_label(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        try:
            self.rect = pygame.rect.Rect(self.x * self.screen_width, self.y * self.screen_height, self.w * self.screen_width, self.h * self.screen_height)
            image_surface = pygame.image.load(self.image).convert_alpha()
            self.screen.blit(pygame.transform.scale(image_surface, (self.w * self.screen_width, self.h * self.screen_height)), self.rect)
        
        except:
            self.rect = pygame.rect.Rect(self.x * self.screen_width, self.y * self.screen_height, self.w * self.screen_width, self.h * self.screen_height)
            text_surface = self.font.render(self.text, True, (255,0,0))
            self.screen.blit(text_surface, (self.rect.x, self.rect.y))


    def get_label_rect(self):
        return self.rect
    
    def hover_label(self):
        self.hover_rect = self.rect
        try:
            hover_surface = pygame.image.load(self.hover_image).convert_alpha()
            self.screen.blit(pygame.transform.scale(hover_surface, (self.w * self.screen_width, self.h * self.screen_height)), self.rect)
        except:
            text_hover_surface = self.font.render(self.text, True, (255,0,0))
            self.screen.blit(text_hover_surface, (self.rect.x, self.rect.y))

#FIXME Let me know when u test this to see if worky
#perhaps we can handle popup on state side? Popup queue and just delete when timer done? alas i must go
