import pygame

class Label():

    def __init__(self, screen, x, y, w, h, button = False, text = "", image = "", hover_image = ""):
        self.screen = screen 
        self.button = button 
        self.text = text
        self.image = image
        self.x=x
        self.w = w
        self.h = h
        self.hover_image = hover_image
        self.rect = pygame.rect.Rect(x, y, w, h)
    
    
    def render_label(self):
        try:
            image_surface = pygame.image.load(self.image).convert_alpha()
            self.screen.blit(pygame.transform.scale(image_surface, (self.w, self.h)), self.rect)
        
        except:
            print("no label")

    def get_label_rect(self):
        return self.rect
    
    def hover_label(self):
#FIXME Let me know when u test this to see if worky
#perhaps we can handle popup on state side? Popup queue and just delete when timer done? alas i must go
        hover_rect = self.rect
        hover_surface = pygame.image.load(self.hover_image).convert_alpha()
        self.screen.blit(pygame.transform.scale(hover_surface, (self.w, self.h)), hover_rect)
        
        

        

