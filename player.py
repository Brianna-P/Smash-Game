import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, player, name, pos, width, height, image):
        super().__init__()
        self.player = player
        self.name = name
        #self.image = pygame.Surface((width, height))
        #self.image.fill('blue')
        self.img = pygame.image.load(image).convert_alpha()
        #self.rect = self.image.get_rect(topleft = pos)
        self.x, self.y, self.w, self.h = pos[0], pos[1], width, height
        #self.screen_width, self.screen_height = self.game.screen.get_size()
        #self.rect = pygame.rect.Rect(self.screen_width * self.x, self.screen_height * self.y, self.screen_width * self.w, self.screen_height * self.h)

        self.movable = True
        self.gravity = 0.2
        self.jump_speed = -5
        self.vector = pygame.Vector2(0,0)
        self.speed = 2
        self.jumpCount = 0
        self.onGround = True
        self.canDoubleJump = True
        self.jumpsLeft = 2
        self.lastJump = 0
        self.canJump = True
        self.health = 100
        self.font = pygame.font.SysFont('Arial', 25)
    
    def draw(self, surface, screen_width, screen_height):
        #pygame.draw.rect(surface, (0,0,0), self.rect)
        text_surface = self.font.render(self.name, True, (255,0,0))
        label_rect = pygame.rect.Rect(screen_width * self.x, screen_height * self.y - 50, screen_width *0.10, screen_height * 0.10)
        surface.blit(text_surface, label_rect)

        color = (255, 0 ,0)
        if self.health > 20:
            color = (0, 255, 255)
        elif self.health > 50:
            color = (0, 128, 0)

        self.rect = pygame.rect.Rect(screen_width * self.x, screen_height * self.y, screen_width * self.w, screen_height * self.h)
        surface.blit(pygame.transform.scale(self.img, (self.rect.w, self.rect.h)), self.rect)
            
        if self.player == 1:
            corner_image_rect = pygame.rect.Rect(0, 0, screen_width * 0.1 , screen_height * 0.1)
            pygame.draw.rect(surface, (0,0,0), corner_image_rect)
            health_rect = pygame.rect.Rect(screen_width * self.x, screen_height * self.y - 30, screen_width *0.10, screen_height * 0.10)
            #pygame.draw.rect(surface, color, health_rect)

            surface.blit(pygame.transform.scale(self.img, (0.10 * screen_width, 0.10 * screen_height)), corner_image_rect)
        elif self.player == 2:
            corner_image_rect = pygame.rect.Rect(screen_width * .9, 0, screen_width * 0.1, screen_height * 0.1)
            pygame.draw.rect(surface, (0,0,0), corner_image_rect)
            health_rect = pygame.rect.Rect(screen_width * self.x, screen_height * self.y - 30, screen_width *0.10, screen_height * 0.10)
            #pygame.draw.rect(surface, color, health_rect)
            surface.blit(pygame.transform.scale(self.img, (0.10 * screen_width, 0.10 * screen_height)), corner_image_rect)
        

    def get_input(self):
        if self.movable:
            if self.player == 1:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    self.vector.x = -1
                elif keys[pygame.K_d]:
                    self.vector.x = 1
                if keys[pygame.K_w]:
                    self.jump()
            if self.player == 2:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.vector.x = -1
                elif keys[pygame.K_RIGHT]:
                    self.vector.x = 1
                if keys[pygame.K_UP]:
                    self.jump()


#FIXME Fix that 
    def horizontal_movement_collision(self, tiles):

        #self.rect.x += self.vector.x * self.speed
        for sprite in tiles.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.rect.colliderect(self):
                    if self.vector.x < 0:
                         self.rect.left = sprite.rect.right
                    elif self.vector.x > 0:
                        self.rect.right = sprite.rect.left

    def vertical_movement_collision(self, tiles):

        #self.apply_gravity()
        #self.rect.y += self.vector.y * self.speed
        self.apply_gravity()

        for sprite in tiles.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.vector.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.vector.y = 0      
                #elif self.vector.y < 0:
                    self.onGround = True

                    

    
    def jump(self):
        #resets jumps
        if(self.onGround):
            self.canJump = True
            self.jumpsLeft = 2
        if(self.canJump and self.jumpsLeft > 0):
            self.onGround = False
            if(self.lastJump + 400 < pygame.time.get_ticks()):
                self.vector.y = self.jump_speed
                self.jumpsLeft -=1
                self.lastJump = pygame.time.get_ticks()
            

        
            
    def apply_gravity(self):
        self.vector.y += self.gravity
        self.rect.y += self.vector.y
    def move(self):
        self.rect.x += self.vector.x * self.speed
        self.vector.x = 0
        self.rect.y += self.vector.y * self.speed

    def update(self, sprites):
        self.get_input()
        #self.apply_gravity()
        self.vertical_movement_collision(sprites)
        self.horizontal_movement_collision(sprites)
        self.move()