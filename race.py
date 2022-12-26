import pygame
import time
import random

pygame.init()

#############

#############

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
block_color = (53, 115, 255)

#crash_sound = pygame.mixer.Sound("crash.mp3")

car_width = 55

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Car Dodge Game')
clock = pygame.time.Clock()

gameIcon = pygame.image.load('carIcon.png')

backgroundImage = pygame.image.load("background.png")
backgroundImage = pygame.transform.scale(backgroundImage, (800, 600))
gameDisplay.blit(backgroundImage, (0, 0))

carImg = pygame.image.load("racecar.png")
carImg = pygame.transform.scale(carImg, (60, 100)) # resize graphic
carImg = carImg.convert_alpha() # remove whitespace from graphic

car1 = pygame.image.load("diablo.png")
car1 = pygame.transform.scale(car1, (60, 100)) # resize graphic
car1 = car1.convert_alpha() # remove whitespace from graphic

car2 = pygame.image.load("aventador.png")
car2 = pygame.transform.scale(car2, (60, 100)) # resize graphic
car2 = car2.convert_alpha() # remove whitespace from graphic

car3 = pygame.image.load("nsx.png")
car3 = pygame.transform.scale(car3, (60, 100)) # resize graphic
car3 = car3.convert_alpha() # remove whitespace from graphic

car4 = pygame.image.load("speeder.png")
car4 = pygame.transform.scale(car4, (60, 100)) # resize graphic
car4 = car4.convert_alpha() # remove whitespace from graphic

car5 = pygame.image.load("slr.png")
car5 = pygame.transform.scale(car5, (60, 100)) # resize graphic
car5 = car5.convert_alpha() # remove whitespace from graphic

car6 = pygame.image.load("Mach6.png")
car6 = pygame.transform.scale(car6, (60, 100)) # resize graphic
car6 = car6.convert_alpha() # remove whitespace from graphic

car7 = pygame.image.load("Stingray.png")
car7 = pygame.transform.scale(car7, (60, 100)) # resize graphic
car7 = car7.convert_alpha() # remove whitespace from graphic

car8 = pygame.image.load("bike.png")
car8 = pygame.transform.scale(car8, (60, 100)) # resize graphic
car8 = car8.convert_alpha() # remove whitespace from graphic

randomCars = [car1, car2, car3, car4, car5, car6, car7, car8]
enemy = random.choice(randomCars)


#brought to you by code-projects.org
pygame.display.set_icon(gameIcon)

pause = False


# crash = True

def score(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("SCORE: " + str(count), True, red)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color, enemyC):
    #pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    gameDisplay.blit(enemy, [thingx, thingy, thingw, thingh])

def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def crash():
    ####################################

    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    ####################################
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused():
    ############
    pygame.mixer.music.pause()
    #############
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("Car Dodge", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("LET PLAY!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause, enemy
    enemy = random.choice(randomCars)
    ############

    pygame.mixer.music.load('bgmusic.mp3')
    pygame.mixer.music.play(-1)
    ############
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    enemy_speed = 4
    thing_width = 55
    thing_height = 95
    enemyC = random.choice(randomCars)
    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.blit(backgroundImage, (0, 0))

        things(thing_startx, thing_starty, thing_width, thing_height, block_color, enemyC)

        thing_starty += enemy_speed
        car(x, y)
        score(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            #enemy_speed += .25
            if dodged % 5 == 0:
                enemy_speed += (dodged * 1)


        if y < thing_starty + thing_height:
            #print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                #print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
