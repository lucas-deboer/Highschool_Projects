"""
Lucas DeBoer
Objects
May 2, 2022
"""
# This file contains all the classes that are used in the game.

#Import statements
import pygame
import Functions
import assets
from random import randint, choice

# define some colors
WHITE = (255, 255, 255)
DARK_RED = (255, 100, 100)
LIGHT_BLUE = (100, 100, 255)
BLACK = (0, 0, 0)

# Class for the crosshair
class Crosshair(pygame.sprite.Sprite):
    def __init__(self, newColour, x, y, Image):
        pygame.sprite.Sprite.__init__(self)  # initialize the sprite
        self.image = pygame.transform.scale(Image, (44, 44))
        # self.image.set_colorkey(WHITE)  # graphic has white background, this removes/ignores/"green screens" it out
        # this changes the colour of the crosshair
        var = pygame.PixelArray(self.image)
        var.replace((255, 0, 0), newColour)
        del var
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10  # this is the speed that the crosshair moves at
        self.shooting = False
        self.bullets = 3

    # A useful method to move the box based on a tuple input!
    def move(self, movement: tuple = (0, 0)):
        self.rect.x += movement[0] * self.speed
        self.rect.y += movement[1] * self.speed

    def update(self, width, height, controllers, bool, goofy):
        self.shooting = False  # always have shooting to false
        self.move(controllers.get_axis())
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= width:
            self.rect.right = width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= height:
            self.rect.bottom = height

        if controllers.is_button_just_pressed(0):
            if bool is False:
                if goofy: assets.clickSFX.play()
                else: assets.menuSFX.play()
            elif self.bullets != 0:  # only shot if the time is greater than the dif. shoot
                if goofy: assets.pewSFX.play()
                else: assets.shotSFX.play()
                self.bullets -= 1
                self.shooting = True


# Class for the UFO
class UFO(pygame.sprite.Sprite):
    def __init__(self, x, Image, randLower, randUpper):
        pygame.sprite.Sprite.__init__(self)  # initialize the sprite
        self.image = pygame.transform.scale(Image, (84.375, 61.875))
        self.image.set_colorkey(WHITE)  # remove background
        self.rect = self.image.get_rect()
        self.rect.center = (randint(50, x), -self.rect.height)
        # set up the UFO variables
        self.randUpper = randUpper
        self.randLower = randLower
        self.spawning = True
        # choose a random staring speed
        self.xspeed = choice((randint(randLower, randUpper), -randint(randLower, randUpper)))
        self.yspeed = randint(randLower, randUpper)

    def update(self, width, height, screen, roundOver, roundNumber, bullets):
        # this is the spawn in mechanism makes it appear as is the UFO is 'flying' in
        if self.rect.top < 0 and self.spawning == True:
            self.rect.y += 3
        else:
            self.spawning = False

        # resume normal game mechanics
        if self.spawning is False:
            if roundOver: # leave screen when round is over
                if bullets == 0:
                    self.xspeed = 0
                    self.yspeed = -6

                if (self.rect.bottom < 0 or self.rect.right < 0 or self.rect.left > width):
                    self.kill()

            if roundOver is False: # bounce around screen while game is still running
                if self.rect.left < 0:
                    self.rect.left = 0
                    self.xspeed = randint(self.randLower, self.randUpper)
                    if roundNumber >= 5:
                        self.yspeed = choice(
                            (randint(self.randLower, self.randUpper), -randint(self.randLower, self.randUpper)))

                if self.rect.right > width:
                    self.rect.right = width
                    self.xspeed = -randint(self.randLower, self.randUpper)
                    if roundNumber >= 5:
                        self.yspeed = choice(
                            (randint(self.randLower, self.randUpper), -randint(self.randLower, self.randUpper)))

                if self.rect.top < 0:
                    self.rect.top = 0
                    self.yspeed = randint(self.randLower, self.randUpper)
                    if roundNumber >= 5:
                        self.xspeed = choice(
                            (randint(self.randLower, self.randUpper), -randint(self.randLower, self.randUpper)))

            # always make the UFO bounce off of the ground
            if self.rect.bottom > height:
                self.rect.bottom = height
                self.yspeed = -randint(self.randLower, self.randUpper)
                if roundNumber >= 5:
                    self.xspeed = choice(
                        (randint(self.randLower, self.randUpper), -randint(self.randLower, self.randUpper)))

            # update UFO position
            self.rect.x += self.xspeed
            self.rect.y += self.yspeed


# Class for all the buttons
class Button ():
    def __init__(self, screen, string, font, x, y):
        self.text = font.render(string, True, BLACK)
        self.x = x
        self.y = y
        self.width = self.text.get_width() + 15
        self.height = self.text.get_height() + 10
        self.Rect = pygame.Rect(0, 0, self.width, self.height)
        self.Rect.center = (x, y)
        self.draw(screen)

    def draw(self, screen):
        pygame.draw.rect(screen, LIGHT_BLUE, self.Rect)
        screen.blit(self.text,(self.Rect.centerx - self.text.get_width()/2, self.y - self.height/2))
        Functions.drawBorder(screen, self.Rect, 3, DARK_RED)

    def update (self, cursor,screen):
        # enlarge the button when cursor is above it
        if self.Rect.colliderect(cursor):
            self.Rect = pygame.Rect(0, 0, self.width + 20, self.height + 20)
            self.Rect.center = (self.x, self.y)
        self.draw(screen)