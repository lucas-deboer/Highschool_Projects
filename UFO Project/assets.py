      '''
Lucas DeBoer
Images and Sounds
May 10, 2022
'''

# import statements
import pygame
import os

# This file contains all the images and sounds that are used in the game
# set up the necessary folders
game_folder = os.path.dirname(__file__)  # renaming the file where the main is
img_folder = os.path.join(game_folder, "Images")  # takes game folder and adds img folder
sound_folder = os.path.join(game_folder, "Sounds")  # takes game folder and adds img folder

# Images
backgroundImg1 = pygame.image.load(os.path.join(img_folder, "background.png"))  # nature
backgroundImg1 = pygame.transform.scale(backgroundImg1, (1080, 720))

backgroundImg2 = pygame.image.load(os.path.join(img_folder, "back.jpg"))  # space
backgroundImg2 = pygame.transform.scale(backgroundImg2, (1080, 720))

backgroundImg3 = pygame.image.load(os.path.join(img_folder, "backgrd.jpg"))  # city
backgroundImg3 = pygame.transform.scale(backgroundImg3, (1080, 720))

crosshairImg = pygame.image.load(os.path.join(img_folder, "crosshair.png"))
ufoImg = pygame.image.load(os.path.join(img_folder, "ufo.png"))

bulletSheetImg = pygame.image.load(os.path.join(img_folder, "bulletSheet.png"))
bulletSheetImg = pygame.transform.scale(bulletSheetImg, (67.5, 40.5))

# spunds


# list of bad words
badWords = ['ASS', 'FUC', 'FUK', 'FUQ', 'FUX', 'FCK', 'COC', 'COK', 'COQ', 'KOX', 'KOC', 'KOK', 'KOQ', 'CAC', 'CAK',
            'CAQ', 'KAC', 'KAK', 'KAQ', 'DIC', 'DIK', 'DIQ', 'DIX', 'DCK', 'PNS', 'PSY', 'FAG', 'FGT', 'NGR', 'NIG',
            'CNT', 'KNT', 'SHT', 'DSH', 'TWT', 'BCH', 'CUM', 'CLT', 'KUM', 'KLT', 'SUC', 'SUK', 'SUQ', 'SCK', 'LIC',
            'LIK', 'LIQ', 'LCK', 'JIZ', 'JZZ', 'GAY', 'GEY', 'GEI', 'GAI', 'VAG', 'VGN', 'SJV', 'FAP', 'PRN', 'LOL',
            'JEW', 'JOO', 'GVR', 'PUS', 'PIS', 'PSS', 'SNM', 'TIT', 'FKU', 'FCU', 'FQU', 'HOR', 'SLT', 'JAP', 'WOP',
            'KIK', 'KYK', 'KYC', 'KYQ', 'DYK', 'DYQ', 'DYC', 'KKK', 'JYZ', 'PRK', 'PRC', 'PRQ', 'MIC', 'MIK', 'MIQ',
            'MYC', 'MYK', 'MYQ', 'GUC', 'GUK', 'GUQ', 'GIZ', 'GZZ', 'SEX', 'SXX', 'SXI', 'SXE', 'SXY', 'XXX', 'WAC',
            'WAK', 'WAQ', 'WCK', 'POT', 'THC', 'VAJ', 'VJN', 'NUT', 'STD', 'LSD', 'POO', 'AZN', 'PCP', 'DMN', 'ORL',
            'ANL', 'ANS', 'MUF', 'MFF', 'PHK', 'PHC', 'PHQ', 'XTC', 'TOK', 'TOC', 'TOQ', 'MLF', 'RAC', 'RAK', 'RAQ',
            'RCK', 'SAC', 'SAK', 'SAQ', 'PMS', 'NAD', 'NDZ', 'NDS', 'WTF', 'SOL', 'SOB', 'FOB', 'SFU']

pygame.mixer.init()

gameOverSFX = pygame.mixer.Sound(os.path.join(sound_folder, "gameOver.mp3"))
shotSFX = pygame.mixer.Sound(os.path.join(sound_folder, "gun.mp3")) # shot
nextRoundSFX = pygame.mixer.Sound(os.path.join(sound_folder, "nextRound.mp3"))
bangSFX = pygame.mixer.Sound(os.path.join(sound_folder, "Bang2.mp3"))
clickSFX = pygame.mixer.Sound(os.path.join(sound_folder, "Click1.mp3"))
pewSFX = pygame.mixer.Sound(os.path.join(sound_folder, "Pew1.mp3"))
menuSFX = pygame.mixer.Sound(os.path.join(sound_folder, "menu.mp3"))
sadTromboneSFX = pygame.mixer.Sound(os.path.join(sound_folder, "sadTrombone.wav"))
explosionSFX = pygame.mixer.Sound(os.path.join(sound_folder, "boom4.wav"))
