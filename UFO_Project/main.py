"""
Lucas DeBoer
UFO Video Game
May 2, 2022
"""

# import statements
import pygame
import controller
import assets
from Objects import Crosshair, UFO, Button
import Functions
import os

game_folder = os.path.dirname(__file__)  # renaming the file where the main is
sound_folder = os.path.join(game_folder, "Sounds")  # takes game folder and adds img folder

# define the constants
gameSizeHeight = 720
gameSizeWidth = 1080
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
DARK_RED = (139, 0, 0)
GREEN = (57, 255, 20)
PINK = (255, 20, 147)

# set up some variables
run = start = main = end = True
highscore = False
name = ''
goofy = False
colourChoice = RED

background = assets.backgroundImg1
background_rect = background.get_rect()

# set up the timers
flyAway = pygame.USEREVENT + 1

# initialize some things
pygame.init()  # initialize pygame
pygame.joystick.init()  # initialize the joysticks
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

pygame.mixer.music.load(os.path.join(sound_folder, "gameloop.mp3"))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.35)

# set up the screen and background images
screen = pygame.display.set_mode((gameSizeWidth, gameSizeHeight))
pygame.display.set_caption("Alien Invasion")  # CHANGE THIS WHEN A PROPER NAME IS DECIDED UPON

# set up the controllers
p1 = controller.Controller(0)  # Pass in index value of 0, representing controller 1

# Set up the sprite groups
crosshair_sprites = pygame.sprite.Group()
UFO_sprites = pygame.sprite.Group()

# create the player 1 sprite
p1Crosshair = Crosshair(RED, screen.get_width() / 4, screen.get_height() / 4, assets.crosshairImg)
crosshair_sprites.add(p1Crosshair)


# ---------------------------------------------------------------------------------------------------------------------
# simple function that gives the font at the requested size
def fonts(size):
    Font = pygame.font.SysFont('comicsans', size)  # creates a font object
    return Font


# function that spawns in the UFOs
def Spawn(lowerLim, upperLim):
    newUFO = UFO(1000, assets.ufoImg, lowerLim, upperLim)
    UFO_sprites.add(newUFO)
    pygame.time.set_timer(flyAway, 5000)


# ----------------------------------------------------------------------------------------------------------------------
# set up the clock
CLOCK = pygame.time.Clock()

buttonGroup = []

while run:
    fade = 0
    score = 0
    ufosSent = ufosHit = 0
    roundNumber = 1
    display = 1
    limLow = 1
    limHigh = 5
    l1c = l2c = l3c = 65
    string = ''
    roundOver = False
    temp = True

    while start:
        if display == 1:
            pygame.time.delay(9)
        else:
            pygame.time.delay(4)
        screen.fill(WHITE)

        for event in pygame.event.get():  # User did something.
            if event.type == pygame.QUIT:  # If user clicked close.
                start = main = end = run = False  # Flag that we are done, so we exit this loop.

        if p1.is_button_pressed(0) and fade >= 1:
            # main menu
            if button1.Rect.colliderect(p1Crosshair):
                main = True
                start = False
            if button2.Rect.colliderect(p1Crosshair):
                display = 1
            if button3.Rect.colliderect(p1Crosshair):
                display = 2

        if fade < 1:  # to fade in the background
            fade += 0.01
            titleRect = pygame.Rect(0, 0, gameSizeWidth * fade, 100)
            leftRect = pygame.Rect(0, 0, gameSizeWidth / 2, fade * (gameSizeWidth - 100))
            rightRect = pygame.Rect(0, 0, gameSizeWidth / 2, fade * (gameSizeWidth - 100))

            titleRect.topleft = (0, 0)
            leftRect.topleft = titleRect.bottomleft
            rightRect.topleft = leftRect.topright

        # display the background, then buttons
        pygame.draw.rect(screen, DARK_RED, titleRect)
        pygame.draw.rect(screen, GREEN, leftRect)
        pygame.draw.rect(screen, BLACK, rightRect)

        if fade >= 1:
            Functions.textDisplay(screen, 'Alien Invasion', fonts(40), screen.get_width() / 2, 50)
            button1 = Button(screen, 'Begin Game', fonts(30), screen.get_width() / 4, 255)
            button2 = Button(screen, 'Highscores', fonts(30), screen.get_width() / 4, 410)
            button3 = Button(screen, 'Settings', fonts(30), screen.get_width() / 4, 565)

            if display == 1:
                Functions.textDisplay(screen, 'Highscores', fonts(30), 3 * screen.get_width() / 4, 255)
                Functions.displayHighscores(screen, fonts(25), 5 * screen.get_width() / 8, 300)
                buttonGroup = [button1, button2, button3]
            elif display == 2:
                # Backgrounds
                Functions.textDisplay(screen, 'Background', fonts(30), 3 * screen.get_width() / 4, 200)
                back1 = Button(screen, 'Field', fonts(20), 5 * screen.get_width() / 8, 278)
                back2 = Button(screen, 'Space', fonts(20), 6 * screen.get_width() / 8, 278)
                back3 = Button(screen, 'Mountain', fonts(20), 7 * screen.get_width() / 8, 278)

                # Sounds
                Functions.textDisplay(screen, 'Sounds', fonts(30), 3 * screen.get_width() / 4, 355)
                sound1 = Button(screen, 'Regular', fonts(20), 4 * screen.get_width() / 6, 433)
                sound2 = Button(screen, 'Goofy', fonts(20), 5 * screen.get_width() / 6, 433)

                # Colours
                Functions.textDisplay(screen, 'Colour of Crosshair', fonts(30), 3 * screen.get_width() / 4, 510)
                colour1 = Button(screen, 'Red', fonts(20), 5 * screen.get_width() / 8, 615)
                colour2 = Button(screen, 'Magenta', fonts(20), 6 * screen.get_width() / 8, 615)
                colour3 = Button(screen, 'Blue', fonts(20), 7 * screen.get_width() / 8, 615)
                back1.update(p1Crosshair, screen)
                buttonGroup = [button1, button2, button3, back1, back2, back3, sound1, sound2, colour1, colour2,
                               colour3]

            for buttons in buttonGroup:
                buttons.update(p1Crosshair, screen)

        p1.update()  # to break out of the screen

        if p1.is_button_pressed(0) and display == 2:
            # background
            if back1.Rect.colliderect(p1Crosshair):
                background = assets.backgroundImg1
                background_rect = background.get_rect()
            if back2.Rect.colliderect(p1Crosshair):
                background = assets.backgroundImg2
                background_rect = background.get_rect()
            if back3.Rect.colliderect(p1Crosshair):
                background = assets.backgroundImg3
                background_rect = background.get_rect()
            # Sound
            if sound1.Rect.colliderect(p1Crosshair):
                goofy = False
            if sound2.Rect.colliderect(p1Crosshair):
                goofy = True
            # Colour
            if colour1.Rect.colliderect(p1Crosshair):
                colourChoice = RED
            if colour2.Rect.colliderect(p1Crosshair):
                colourChoice = PINK
            if colour3.Rect.colliderect(p1Crosshair):
                colourChoice = BLUE

        p1Crosshair.update(gameSizeWidth, gameSizeHeight, p1, False, goofy)  # call the update function of the class
        crosshair_sprites.draw(screen)
        pygame.display.update()

    # Main Game Loop ----------------
    p1Crosshair.kill()
    Spawn(1, 5)
    ufosSent += 1
    p1Crosshair = Crosshair(colourChoice, screen.get_width() / 4, screen.get_height() / 4, assets.crosshairImg)
    crosshair_sprites.add(p1Crosshair)

    pygame.mixer.music.fadeout(1000)
    while main:
        pygame.time.delay(10)
        # update and redraw everything
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        for event in pygame.event.get():  # User did something.
            if event.type == pygame.QUIT:  # If user clicked close.
                main = end = run = False  # Flag that we are done, so we exit this loop.
            elif event.type == flyAway:
                roundOver = True

        # 'kill' UFO when it is shot
        if p1Crosshair.shooting and pygame.sprite.groupcollide(crosshair_sprites, UFO_sprites, False, True):
            if goofy:
                assets.bangSFX.play()
            else:
                assets.explosionSFX.play()
            ufosHit += 1
            score += 375

        # finish round if all three shots are misses
        if p1Crosshair.bullets == 0 and len(UFO_sprites) > 0:
            roundOver = True

        # reset all the stats when the UFO is hit
        if len(UFO_sprites) == 0:
            roundOver = False
            p1Crosshair.bullets = 3
            if ufosSent < 10:
                ufosSent += 1
                Spawn(limLow, limHigh)

        # display the score, number of ufos hit, and bullets
        Functions.scoreDisplay(screen, score, fonts(25))
        string = str(ufosHit) + ' of ' + str(ufosSent) + " UFO's hit."
        Functions.textDisplay(screen, string, fonts(30), screen.get_width() / 2, screen.get_height() - 60)
        Functions.drawBullets(screen, p1Crosshair.bullets, fonts(20))

        # display message if the ducks are flying away
        if roundOver:
            string = 'Fly Away!'
            Functions.textDisplay(screen, string, fonts(25), screen.get_width() / 2, screen.get_height() / 2)

        # End of Round Mechanics
        if ufosSent == 10 and len(UFO_sprites) == 0:
            if ufosHit >= 5:
                ufosHit = 0
                roundNumber += 1
                ufosSent = 0
                string = 'Round ' + str(roundNumber)
                Functions.textDisplay(screen, string, fonts(30), screen.get_width() / 2, screen.get_height() / 2)
                pygame.mixer.Sound.stop(assets.shotSFX)
                pygame.mixer.Sound.stop(assets.bangSFX)
                pygame.mixer.Sound.stop(assets.explosionSFX)
                pygame.mixer.Sound.stop(assets.pewSFX)
                assets.nextRoundSFX.play()
                if roundNumber > 10:
                    limLow += 1
                    limHigh += 1
                elif roundNumber >= 7:
                    limLow += 1
                    limHigh = 7
                elif roundNumber >= 3:
                    limLow = 1
                    limHigh = 7
                pygame.display.update()
                pygame.time.delay(3000)
            else:
                string = "GAME OVER"
                Functions.textDisplay(screen, string, fonts(30), screen.get_width() / 2, screen.get_height() / 2)
                Functions.textDisplay(screen, 'Press Right Button.', fonts(20), screen.get_width() / 2,
                                      screen.get_height() * 5 / 8)
                if temp:
                    pygame.mixer.Sound.stop(assets.shotSFX)
                    pygame.mixer.Sound.stop(assets.bangSFX)
                    pygame.mixer.Sound.stop(assets.explosionSFX)
                    pygame.mixer.Sound.stop(assets.pewSFX)
                    if goofy:
                        assets.sadTromboneSFX.play()
                    else:
                        assets.gameOverSFX.play()
                    temp = False

        if string == "GAME OVER" and p1.is_button_pressed(1):
            main = False

        # Update the controllers
        p1.update()

        # update crosshair and ufos
        UFO_sprites.update(gameSizeWidth, gameSizeHeight - 100, screen, roundOver, roundNumber, p1Crosshair.bullets)
        if string != "GAME OVER":
            p1Crosshair.update(gameSizeWidth, gameSizeHeight, p1, True, goofy)  # call the update function of the class

        UFO_sprites.draw(screen)
        crosshair_sprites.draw(screen)
        pygame.display.update()

    for scores in Functions.getHighscores():
        if score > int(scores[slice(4, 9)]):
            highscore = True

    pygame.mixer.music.play(-1, 0, 2000)
    while highscore is True:
        screen.fill(BLACK)
        pygame.time.delay(10)
        Functions.textDisplay(screen, 'Please choose a username', fonts(48), gameSizeWidth / 2, 100)
        l1 = Button(screen, chr(l1c), fonts(40), gameSizeWidth * 13 / 32, 250)
        l2 = Button(screen, chr(l2c), fonts(40), gameSizeWidth / 2, 250)
        l3 = Button(screen, chr(l3c), fonts(40), gameSizeWidth * 19 / 32, 250)
        l4 = Button(screen, 'Save', fonts(40), gameSizeWidth / 2, 350)
        l4.update(p1Crosshair, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                highscore = end = run = False

        p1.update()
        # see if the crosshair is over another button to change the letters
        if l1.Rect.colliderect(p1Crosshair):
            if p1.is_button_just_pressed(0):
                l1c = l1c + 1
                if (l1c == 91):
                    l1c = 65
            if p1.is_button_just_pressed(1):
                l1c = l1c - 1
                if (l1c == 64):
                    l1c = 90

        if l2.Rect.colliderect(p1Crosshair):
            if p1.is_button_just_pressed(0):
                l2c = l2c + 1
                if (l2c == 91):
                    l2c = 65
            if p1.is_button_just_pressed(1):
                l2c = l2c - 1
                if (l2c == 64):
                    l2c = 90

        if l3.Rect.colliderect(p1Crosshair):
            if p1.is_button_just_pressed(0):
                l3c = l3c + 1
                if l3c == 91:
                    l3c = 65
            if p1.is_button_just_pressed(1):
                l3c = l3c - 1
                if (l3c == 64):
                    l3c = 90

        # save name - exit loop and connect letters to name variable
        if l4.Rect.colliderect(p1Crosshair):
            if p1.is_button_just_pressed(0):
                name = chr(l1c) + chr(l2c) + chr(l3c)
                if name not in assets.badWords:
                    if score < 1000:
                        score = '00' + str(score)
                    elif score < 10000:
                        score = '0' + str(score)
                    Functions.isHighscore(name, score)
                    highscore = False

        if name in assets.badWords:
            Functions.textDisplay(screen, 'Username not allowed.', fonts(40), gameSizeWidth / 2, 500)

        p1Crosshair.update(gameSizeWidth, gameSizeHeight, p1, False, goofy)  # call the update function of the class
        crosshair_sprites.draw(screen)
        pygame.display.update()

    # End Screen -------------------
    while end:
        pygame.time.delay(10)
        screen.fill(BLACK)

        for event in pygame.event.get():  # User did something.
            if event.type == pygame.QUIT:  # If user clicked close.
                end = run = False

        Functions.displayHighscores(screen, fonts(40), screen.get_width() / 3, 150)
        Functions.textDisplay(screen, 'Highscores', fonts(50), screen.get_width() / 2, 100)
        replay = Button(screen, 'Play Again', fonts(30), screen.get_width() / 4, 650)
        change = Button(screen, 'Settings', fonts(30), 3 * screen.get_width() / 4, 650)

        if p1.is_button_pressed(0):
            # main menu
            if replay.Rect.colliderect(p1Crosshair):
                main = True
                break
            if change.Rect.colliderect(p1Crosshair):
                start = True
                break

        p1.update()
        replay.update(p1Crosshair, screen)
        change.update(p1Crosshair, screen)

        p1Crosshair.update(gameSizeWidth, gameSizeHeight, p1, False, goofy)  # call the update function of the class
        crosshair_sprites.draw(screen)
        pygame.display.update()

pygame.quit()  # This is the final quitting line
