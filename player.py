import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, player, game, name, pos, width, height, image):
        super().__init__()
        self.player = player
        self.name = name
        #self.image = pygame.Surface((width, height))
        #self.image.fill('blue')

        #self.rect = self.image.get_rect(topleft = pos)
        self.x, self.y, self.w, self.h = pos[0], pos[1], width, height
        #self.screen_width, self.screen_height = self.game.screen.get_size()
        #self.rect = pygame.rect.Rect(self.screen_width * self.x, self.screen_height * self.y, self.screen_width * self.w, self.screen_height * self.h)

        self.currently_attacking = False
        self.currentlly_blocking = False
        self.collided = False
        self.movable = True
        self.right_facing = False
        self.gravity = 0.02
        self.y_speed = 0
        self.y_vel = 0
        self.can_double = True
        self.vector = pygame.Vector2(0,0)
        self.speed = 0.001
        self.on_ground = True
        self.health = 18
        self.font = pygame.font.SysFont('Arial', 25)
        self.screen_w, self.screen_h = game.screen.get_size()
        img = pygame.image.load(image).convert_alpha()
        self.img = pygame.transform.scale(img, (50, 50))
        self.rect=  pygame.rect.Rect(self.screen_w * self.x, self.screen_h * self.y, self.screen_w * self.w, self.screen_h * self.h)
        self.mask = pygame.mask.from_surface(self.img)
        self.mask_img = self.mask.to_surface()
    
    def draw(self, surface, screen_width, screen_height):
        self.screen_w, self.screen_h = surface.get_size()        
        #pygame.draw.rect(surface, (0,0,0), self.rect)
        text_surface = self.font.render(self.name, True, (255,0,0))
        label_rect = pygame.rect.Rect(screen_width * self.x, screen_height * self.y - 50, screen_width *0.10, screen_height * 0.10)
        surface.blit(text_surface, label_rect)

        color = (255, 0 ,0)
        if self.health > 20:
            color = (0, 255, 255)
        if self.health > 50:
            color = (0, 255, 0)

        self.rect = pygame.rect.Rect(screen_width * self.x, screen_height * self.y, screen_width * self.w, screen_height * self.h)
        surface.blit(pygame.transform.scale(self.img, (self.rect.w, self.rect.h)), self.rect)
        surface.blit(pygame.transform.scale(self.mask_img, (self.rect.w, self.rect.h)), self.rect)

        if self.player == 1:
            corner_image_rect = pygame.rect.Rect(0, 0, screen_width * 0.1 , screen_height * 0.1)
            pygame.draw.rect(surface, (0,0,0), corner_image_rect)
            back_rect = pygame.rect.Rect(screen_width * 0.1, 0, screen_width *0.5 - screen_width * 0.1, screen_height * 0.02)
            health_rect = pygame.rect.Rect(screen_width * 0.1, 0, (screen_width *0.5 - screen_width * 0.1)* (self.health/100), screen_height * 0.02)
            pygame.draw.rect(surface, (0,0,0), back_rect)
            pygame.draw.rect(surface, color, health_rect)

            pygame.draw.circle(surface, (255,0,0), (0, 0), self.screen_w *.13)
            pygame.draw.circle(surface, (0,0,0), (0, 0), self.screen_w *.11)
            surface.blit(pygame.transform.scale(self.img, (0.10 * screen_width, 0.10 * screen_height)), corner_image_rect)
        elif self.player == 2:
            corner_image_rect = pygame.rect.Rect(screen_width * .9, 0, screen_width * 0.1, screen_height * 0.1)
            pygame.draw.rect(surface, (0,0,0), corner_image_rect)
            back_rect = pygame.rect.Rect(screen_width * 0.5, 0, screen_width *0.5 - screen_width * 0.1, screen_height * 0.02)
            health_rect = pygame.rect.Rect(screen_width * 0.5, 0, (screen_width - screen_width * 0.1)*(self.health/100), screen_height * 0.02)
            pygame.draw.rect(surface, (0,0,0), back_rect)
            pygame.draw.rect(surface, color, health_rect)
            pygame.draw.circle(surface, (255,0,0), (self.screen_w, 0), self.screen_w *.13)
            pygame.draw.circle(surface, (0,0,0), (self.screen_w, 0), self.screen_w *.11)
            surface.blit(pygame.transform.scale(self.img, (0.10 * screen_width, 0.10 * screen_height)), corner_image_rect)
        

    def get_input(self):
        if self.movable:
            if self.player == 1:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    if self.vector.x >= -4:
                        self.vector.x -= 1
                elif keys[pygame.K_d]:
                    if self.vector.x <= 4:
                        self.vector.x += 1
                if keys[pygame.K_w]:
                    self.jump()
            if self.player == 2:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    if self.vector.x >= -4:
                        self.vector.x -= 1
                elif keys[pygame.K_RIGHT]:
                    if self.vector.x <= 4:
                        self.vector.x += 1
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
        if(self.on_ground):
            self.on_ground = False
            self.can_double = True
            self.vector.y -= 3
            #self.y_speed = 0.3
        elif not self.on_ground and self.can_double:
                self.vector.y -= 3
                self.can_double = False
            
        
            
    def apply_gravity(self):
        self.vector.y += self.gravity
        self.y += self.vector.y
        if self.collided:
            self.vector.y = 0
            self.collided = False

    def move(self):
        self.x += (self.vector.x * self.speed)
        self.vector.x = 0
        self.y += (self.vector.y * self.speed)

    def update(self):
        #self.rect = self.x
        self.get_input()
        if self.vector.y <0:
            self.vector.y += 0.15
        else:
            self.vector.y = 0
     
        self.move()

#Platform collisions

    def check_collisions():
        pass
#Movement fixes (DOWN) & (SPEED)
#Attak Moves
