import pygame
level = [
'                     ',
'          XX         ',
'                     ',
'     XX        XX    ',
'                     ',
'     1          2    ',
'   XXXXXXXXXXXXXXXX  ',
'                     ',
]
tile_size = 64
level1platforms =  [
                    (pygame.Rect(2*tile_size +32, 7 *tile_size, tile_size * 16, 32), (1/4, 2/3 , 1/2, 1/16)),
                    (pygame.Rect(4*tile_size +32, 4 *tile_size, tile_size * 2, 32),(1/2, 1/3 , 1/3, 1/16)),
                    (pygame.Rect(14*tile_size, 4 *tile_size, tile_size * 2, 32),(1/2, 2/3 , 1/3, 1/16)),
                    (pygame.Rect(9*tile_size +16, 2 *tile_size, tile_size * 2, 32),(3/4, 2/3 , 1/3, 1/16))
                    ]
