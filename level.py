2#from game import tile_size
import pygame
from tile import Tile
from state import State
from player import Player
from settings import tile_size, level1platforms
import math


class Level(State):
    def __init__(self, game):
        State.__init__(self, game)
        level = 1
        self.layout = level
        self.surface = self.game.screen
        self.platformRects = level1platforms
        self.tile_size = tile_size
        self.tiles = pygame.sprite.Group()
        self.zoom_factor = 1
        self.dist = 0
        self.level = 0
        self.timer = 0
        self.prev_dist = self.dist
        self.font = pygame.font.SysFont('Arial', 25)

        self.screen_width, self.screen_height = self.game.screen.get_size()
        #self.player1 = Player(1, (4 * self.tile_size + 32, 6* self.tile_size), 32, 64)
        #self.player2 = Player(2, (15 * self.tile_size + 32,6 * self.tile_size), 32, 64)


    def update(self, actions):
        self.screen_width, self.screen_height = self.game.screen.get_size()
        #self.player1.update()
        #self.player2.update() # beep boop dingleberry
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.game.running = False
            if event.type == pygame.QUIT:
                self.game.running = False

    def render(self):
        self.screen_width, self.screen_height = self.game.screen.get_size()
        #self.surface.blit(self.level_image, (0,0))
        self.surface.blit(pygame.transform.scale(self.level_image, (self.screen_width, self.screen_height)), (0,0))
        self.render_level()
        self.render_clock()

        
    def render_level(self):
        for p in self.platformRects:
            temp_rect = pygame.rect.Rect(self.screen_width* p[0], self.screen_height * p[1], self.screen_width * p[2], self.screen_height * p[3])
            pygame.draw.rect(self.surface, (0,0,0), temp_rect)
        
        self.player1.draw(self.surface, self.screen_width, self.screen_height)
        self.player2.draw(self.surface, self.screen_width, self.screen_height)

    def render_clock(self):
        time = (60000 - (pygame.time.get_ticks() - self.timer))/1000
        if(time < 0):

            self.game.state_stack.pop()
            self.game.state_stack.pop()
            self.game.state_stack.pop()

        text_surface = self.font.render(str(time), True, (255,0,0))
        label_rect = pygame.rect.Rect(self.screen_width * 0.5 -.05, 0, self.screen_width *0.10, self.screen_height * 0.10)
        self.surface.blit(text_surface, label_rect)
        #self.timer = pygame.time.get_ticks()

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

    def enter_state(self, p1, p2, level):
        print("level state")
        pygame.display.set_caption('FIGHTT!!!')
        #self.player1 = p1
        #self.player2 = p2
        self.level = level

        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)

        #why do you fraw the player in so many places

    def enter_state1(self, p1, p2, level_image, level_platforms):
        print("Map")
        self.player1, self.player2 = p1, p2
        self.level_image = pygame.image.load("Assets/{}".format(level_image)).convert_alpha()
        self.timer = pygame.time.get_ticks()
        self.level_platforms = level_platforms
        pygame.display.set_caption('FIGHTTT')

        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
        self.game.state_stack.append(self)
