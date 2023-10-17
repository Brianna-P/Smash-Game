#from game import tile_size
import pygame
from tile import Tile
from player import Player
from settings import *
import math

#FIXME: turn into state


class Level():
    def __init__(self, screen, level):
        self.layout = level
        self.surface = screen
        self.tile_size = tile_size
        self.tiles = pygame.sprite.Group()
        self.zoom_factor = 1
        self.dist = 0
        self.prev_dist = self.dist
        self.w, self.h = self.surface.get_size()


    def setup_level1(self):

        for p in level1platforms:
            #pygame.draw.rect(self.surface, (0,0,0), x)
            tile = Tile((p.x, p.y), p.w, p.h)
            self.tiles.add(tile)

        self.player1 = Player(1, (4 * self.tile_size + 32, 6* self.tile_size), 32, 64)
        self.player2 = Player(2, (15 * self.tile_size + 32,6 * self.tile_size), 32, 64)
    def setup_level(self):
        for row_index, row in enumerate(self.layout):
            for col_index, cell in enumerate(row):
                x = col_index * self.tile_size
                y = row_index * self.tile_size
                if cell == 'X':
                    #if row_index< len(self.layout)/2:
                    tile = Tile((x,y), self.tile_size, 32)
                    self.tiles.add(tile)
                if cell == '1':
                    self.player1 = Player(1, (x,y), 32, 64)
                if cell == '2':
                    self.player2 = Player(2, (x,y), 32, 64)
                    #player = Player((x,y), self.tile_size)
                    #self.tiles.add(player)
    def renderPlatforms(self):
        self.tiles.draw(self.surface)
        #for x in level1platforms:
            #pygame.draw.rect(self.surface, (0,0,0), x)
        
    def run(self):
        #self.camera()
        self.tiles.draw(self.surface)
        self.player1.update(self.tiles)
        self.player2.update(self.tiles)
        #self.renderPlatforms()
        self.player1.draw(self.surface)
        self.player2.draw(self.surface)
        

    def camera(self):
        self.dist = math.hypot(self.player1.rect.x - self.player2.rect.x, self.player1.rect.y - self.player2.rect.y)
        if self.dist > math.sqrt(math.pow((self.tile_size * 4), 2) + math.pow(self.tile_size * 2, 2)):
            self.zoom()
        else:
            self.pan()
        self.adjust()
        self.zoom_factor = 1

    def adjust(self):
        self.player1.rect.w = self.player1.rect.w * self.zoom_factor
        self.player1.rect.h = self.player1.rect.h * self.zoom_factor
        self.player2.rect.h = self.player2.rect.h * self.zoom_factor
        self.player2.rect.w = self.player2.rect.w * self.zoom_factor
        for tile in self.tiles:
            tile.adjust(self.zoom_factor)


    def zoom(self):
        if self.dist != self.prev_dist:
            if self.dist > self.prev_dist:
                self.zoom_factor += 0.01
            else:
                self.zoom_factor -= 0.01
        self.prev_dist = self.dist
    def pan(self):
        pass

    def shift(self, dist):
        pass
        for tile in self.tiles:
            tile.shift()