import pygame
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, width, height, xratio, yratio, wratio, hratio):
        super().__init__() 
        self.image = pygame.Surface((width, height))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.xratio = xratio
        self.yratio = yratio
        self.wratio = wratio
        self.hratio = hratio


    def adjust(self, zoom, screen_width, screen_height):

        self.rect.x = 0
        self.rect.y = 0
        self.rect.w = 0
        self.rect.h = 0

        
        #self.image = pygame.transform.scale(self.image, (self.image.get_width() * zoom, self.image.get_height() * zoom))
        #self.rect.w = self.rect.w * zoom
        #self.rect.h = self.rect.h * zoom
        #self.image = pygame.transform.scale(self.image, (self.rect.w, self.rect.h))

    def shift(self, xamount, yamount):
        self.rect.x += xamount
        self.rect.y += yamount

    