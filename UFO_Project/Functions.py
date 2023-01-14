"""
Lucas DeBoer
Functions
May 2, 2022
"""
# This file contains all the functions that I used in this project

# import statements
import pygame
import assets

# defince some colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_RED = (255, 100, 100)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (100, 100, 255)


# Get images off of a sprite sheet
# Pre: image sheet, frame number, width and height of frame, colour of background, number of objects on sheet
# Post: an ind. image with a blank background is returned.
def getImages(sheet, frame, width, height, colour, objects):
    image = pygame.Surface((width * frame / objects, height)).convert_alpha()
    image.fill(colour)
    image.blit(sheet, (0, 0), (0, 0, width * frame / objects, height))
    image.set_colorkey(colour)
    return image


# Display the number of bullets
# Pre: screen/display, number of bullets left, font
# Post: a display in the bottom corner of screen that shows hows many bullets are left
def drawBullets(screen, numBullets, font):
    text = font.render(' Shots', True, BLACK)
    textRect = pygame.draw.rect(screen, LIGHT_BLUE, pygame.Rect(50, screen.get_height() - 50, assets.bulletSheetImg.get_width(),text.get_height() + 10))
    bulletRect = pygame.draw.rect(screen, LIGHT_BLUE, pygame.Rect(50, textRect.top - text.get_height() - 10,assets.bulletSheetImg.get_width(), assets.bulletSheetImg.get_height() + 10))
    referenceRect = pygame.Rect(0, 0, assets.bulletSheetImg.get_width(), text.get_height() + assets.bulletSheetImg.get_height() + 8)
    referenceRect.topleft = bulletRect.topleft
    drawBorder(screen, referenceRect, 3, DARK_RED)
    screen.blit(getImages(assets.bulletSheetImg, numBullets, assets.bulletSheetImg.get_width(), assets.bulletSheetImg.get_height(), DARK_RED, 3), (bulletRect.left, bulletRect.top))
    screen.blit(text, textRect)  # draw the text to the screen


# Displays text
# Pre: screen, text to be displayed, a font, x and y coordinates (center of display)
# Post: The passed tezt is diplayed at the given coordinates
def textDisplay (screen, string, font, x, y):
    # create the text
    text = font.render(string, True, BLACK)
    # create the actual box
    textRect = pygame.Rect(0, 0, text.get_width() + 15, text.get_height() + 10)
    textRect.center = (x, y)
    # print the box
    pygame.draw.rect(screen, LIGHT_BLUE, textRect)
    screen.blit(text,(textRect.centerx - text.get_width()/2, textRect.y))
    drawBorder(screen, textRect, 3, DARK_RED)
    return textRect


# Draws a border around a rectangle
# Pre: screen, a rectange, thickness of line, and a colour
# Post: a border is drawn around a rectangle
def drawBorder(screen, rect, thickness, colour):
    rectangle = pygame.Rect(0, 0 , rect.width + 2 * thickness, rect.height + 2 * thickness)
    rectangle.center = rect.center
    pygame.draw.rect(screen, colour, rectangle, thickness, 5)


# Displays the score
# Pre: screen, score, and the font
# Post: displays the score in the bottom corner of the screen
def scoreDisplay (screen, score, font):
    string = 'Score: ' # to get the proper formatting of the score display
    if score == 0:
        string += '0000'
    elif score < 1000:
        string += '00'
    elif score < 10000:
        string += '0'
    text = font.render(string + str(score), True, BLACK)
    textRect = pygame.Rect(0, 0, text.get_width()+10, text.get_height())
    textRect.bottomright = (screen.get_width() - 50, screen.get_height() - 50)
    drawBorder(screen, textRect, 3, DARK_RED)
    pygame.draw.rect(screen, LIGHT_BLUE, textRect)
    screen.blit(text, textRect)


# Modifies highscore file
# Pre: a name and score
# Post: the highscores list is modified
def isHighscore (name, score):
    # add the new score to list
    scores = open('highscores.txt', 'a')
    scores.writelines(name + ' ' + str(score) + '\n')
    scores.close()

    # sort the highscores from largest to smallest
    H = getHighscores()
    H.sort(key=lambda x: x[slice(4, 9)], reverse=True)

    # add only the top ten scores back to the document
    scores = open('highscores.txt', 'w')
    for x in range(len(H)):
        if x == 10:
            break
        scores.writelines(H[x] + '\n')
    scores.close()


# Get the highscores
# Pre: none
# Post: return the list of highscores
def getHighscores():
    highscores = open("highscores.txt")
    lines = highscores.readlines()
    highscores.close()

    H = []
    for line in lines:
        # strips out the \n and any other formatting
        H.append("{}{}".format('', line.strip()))
    return H


# Display the highscores
# Pre: screen, font, and x and y coordinates (top left of display)
# Post: Displays the highscores at the given set of coordinates
def displayHighscores(screen, font, x, y):
    H = getHighscores()
    for X in range(len(H)): # separate the names from their scores
        name = H[X][slice(0,3)]
        score = H[X][slice(4,9)]

        # create the text for the name and score
        nameText = font.render(name, True, WHITE)
        scoreText = font.render(score, True, WHITE)

        # create the rectangles
        nameTextRect = pygame.Rect(0, 0, nameText.get_width(), nameText.get_height())
        nameTextRect.topleft = (x,y + 35 * X)
        scoreTextRect = pygame.Rect(0, 0, scoreText.get_width(), scoreText.get_height())
        scoreTextRect.topleft = (x + nameText.get_width() + 150, y + 35 * X)

        # display the name and score on screen
        screen.blit(nameText, nameTextRect)
        screen.blit(scoreText, scoreTextRect)