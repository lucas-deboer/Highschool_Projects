import pygame
import os
from random import randint  # need these to generate random Numbers
import images

# some game settings
WIDTH = 800
HEIGHT = 600
FPS = 30

# images
# where the folders are - setup assets
game_folder = os.path.dirname(__file__)  # renaming the file where the main is
img_folder = os.path.join(game_folder, "Images")  # takes game folder and adds img folder

# define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# class for player
class Player(pygame.sprite.Sprite):
    # sprite for player

    def __init__(self, x, y, image_Colour):
        pygame.sprite.Sprite.__init__(self)  # initialize the sprite
        self.image = images.ship
        self.image = pygame.transform.scale(self.image, (52, 44))
        self.image.set_colorkey(
            (246, 246, 246))  # graphic has black background, this removes/ignores/"green screens" it out
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)
        self.x_speed = 0
        self.y_speed = 0
        self.lastShot = pygame.time.get_ticks()
        self.currentTime = 0

    def update(self):
        self.x_speed = 0
        self.y_speed = 0
        # controls and player movement
        # stay within the windows
        keys = pygame.key.get_pressed()
        # player controls
        if keys[pygame.K_LEFT]:
            if self.rect.left <= 0:
                self.x_speed = 0
                self.rect.left = 0
            else:
                self.x_speed = -10
        if keys[pygame.K_RIGHT]:
            if self.rect.right >= WIDTH:
                self.x_speed = 0
                self.rect.right = WIDTH
            else:
                self.x_speed = 10
        if keys[pygame.K_UP]:
            if self.rect.top <= 0:
                self.y_speed = 0
                self.rect.top = 0
            else:
                self.y_speed = -10
        if keys[pygame.K_DOWN]:
            if self.rect.bottom >= HEIGHT:
                self.y_speed = 0
                self.rect.bottom = HEIGHT
            else:
                self.y_speed = 10

        # add spacebar to shoot
        if keys[pygame.K_SPACE]:
            self.currentTime = pygame.time.get_ticks()
            if len(bullets_group) < 3 and self.currentTime - self.lastShot >= 250:  # only fire/have 5 bullets on the screen
                self.lastShot = self.currentTime
                self.shoot()

        #  move player
        self.rect.bottom += self.y_speed
        self.rect.right += self.x_speed

        # add the shoot function

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)  # Big B = bullet class
        all_sprites.add(bullet)
        bullets_group.add(bullet)  # adding to the bullet group


# bullet Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):  # x and y are the center and top of player
        pygame.sprite.Sprite.__init__(self)  # initialize the sprite
        self.image = pygame.image.load(os.path.join(img_folder, "bullet.png")).convert()
        self.image = pygame.transform.scale(self.image, (11.5, 22))
        self.image.set_colorkey(WHITE)  # remove/ignore/"green screen" out the background
        self.rect = self.image.get_rect()
        self.rect.bottom = y  # position the bullet to start
        self.rect.centerx = x  # position the bullet to start
        self.y_speed = -10  # bullet speed

    # update bullet
    def update(self):
        self.rect.y += self.y_speed
        # kill if it moves off of the top of the screen
        if self.rect.bottom < 0:
            self.kill()


# monster class
class Monster(pygame.sprite.Sprite):
    # sprite for the monster

    def __init__(self, x, y, image_Colour):
        pygame.sprite.Sprite.__init__(self)  # initialize the sprite
        if image_Colour == 1:
            self.image = pygame.image.load(os.path.join(img_folder, "redApple.png")).convert()
            self.image = pygame.transform.scale(self.image, (34, 35))
            self.image.set_colorkey(BLACK)  # remove/ignore/"green screen" out the background
            self.type = "apple"
        elif image_Colour == 2:
            self.image = pygame.image.load(os.path.join(img_folder, "watermelon.png")).convert()
            self.image = pygame.transform.scale(self.image, (41, 43))
            self.image.set_colorkey(WHITE)  # remove/ignore/"green screen" out the background
            self.type = "watermelon"
        else:
            self.image = pygame.image.load(os.path.join(img_folder, "banana.jpg")).convert()
            self.image = pygame.transform.scale(self.image, (44, 48))
            self.image.set_colorkey(WHITE)  # remove/ignore/"green screen" out the background
            self.type = "banana"

        self.rect = self.image.get_rect()
        self.rect.center = (0, (randint(0, HEIGHT - 50)))
        self.speed = randint(1, 20)

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.rect.center = (0, (randint(0, HEIGHT - 50)))
            self.speed = randint(1, 20)


# draw the completion bar
def Bar(x):
    if int(x) > 100:
        x = 100
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 202, 25), True)  # (x,y, size x, size y)
    pygame.draw.rect(screen, GREEN, pygame.Rect(1, 1, 2 * int(x), 23))  # (x,y, size x, size y)


def Scoreboard():
    text = Font.render('Score: ' + str(points), True, BLACK)
    textRect = pygame.draw.rect(screen, WHITE, text.get_rect(midtop=(400, 0)))
    screen.blit(text, textRect)  # draw the text to the screen


def stopClock(x):
    if x - (x // 60) * 60 < 10:
        text = Font.render('Timer: ' + str(x // 60) + ":0" + str(int(x) - int(x // 60) * 60), True, BLACK)
    else:
        text = Font.render('Timer: ' + str(x // 60) + ":" + str(int(x) - int(x // 60) * 60), True, BLACK)
    textRect = pygame.draw.rect(screen, WHITE, text.get_rect(topright=(WIDTH, 0)))
    screen.blit(text, textRect)  # draw the text to the screen


# initialize pygame and create window
pygame.init()
# pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

# bullet group
bullets_group = pygame.sprite.Group()

# create Monsters
monster_group = pygame.sprite.Group()

for i in range(0, 5):
    blockColor = randint(1, 3)
    monst = Monster(50, 50, blockColor)
    all_sprites.add(monst)
    monster_group.add(monst)

# create Player
player_group = pygame.sprite.Group()
player1 = Player(35, 35, BLACK)
all_sprites.add(player1)
player_group.add(player1)

# game loop / set up stuff
running = True
points = 0
Font = pygame.font.SysFont('comicsans', 20)  # creates a font object

# setup events
# spawn monster
Spawn = pygame.USEREVENT + 1
pygame.time.set_timer(Spawn, 10000)
# timer
TIMER = pygame.USEREVENT + 2
pygame.time.set_timer(TIMER, 1000)
timer = 0

while running:
    # keep loop running at the right speed
    clock.tick(FPS)

    # process inputs(events)
    for event in pygame.event.get():
        # close the window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == Spawn or len(monster_group) == 0:
            for i in range(0, 5):
                blockColor = randint(1, 3)
                monst = Monster(50, 50, blockColor)
                all_sprites.add(monst)
                monster_group.add(monst)
            if len(monster_group) == 0:
                pygame.time.set_timer(Spawn, 0)
            pygame.time.set_timer(Spawn, 10000)
        elif event.type == TIMER:
            timer += 1

    # update
    all_sprites.update()  # call the update function of the class

    # collision test
    hits = [pygame.sprite.groupcollide(monster_group, bullets_group, False, False)]
    if pygame.sprite.groupcollide(monster_group, bullets_group, True, True):
        points += 1

    # draw /render
    screen.fill(BLUE)  # could use (R,G,B)
    all_sprites.draw(screen)  # draw all the sprites in the group

    # Scoreboard & progress bar
    Scoreboard()
    Bar(points)
    stopClock(timer)
    # * after drawing everything, flip the display
    pygame.display.flip()
pygame.quit()
