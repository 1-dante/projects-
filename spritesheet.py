import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, frame, width, height, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        # first 0,0 is pasting it on the screen and the second two is the area of the sprite
        image.blit(self.sheet, (0,0), ((frame*width),0,width,height))
        image.set_colorkey(colour)
        #for scale
        #image= pygame.transform.scale(image, (width*scale,height*height))
        return image
