import pygame
import time
import random
from os import path #build file locations

pygame.init()

# Set screen variables
display_width = 800
display_height = 600
hsFile = "highscore.txt"

#Set Color Variables
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
block_color = (53, 115, 255)

# Set variables for sounds
crash_sound = pygame.mixer.Sound("crash.mp3")

# Set variables for collision
car_width = 55

life = 5 #set initial value of lives

# Set captions and display surface
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Super Racer')
clock = pygame.time.Clock()
gameIcon = pygame.image.load('carIcon.png')

#Load images and set image sizes
backgroundImage = pygame.image.load("background.png")
backgroundImage = pygame.transform.scale(backgroundImage, (800, 600))
gameDisplay.blit(backgroundImage, (0, 0))





pygame.display.set_icon(gameIcon)

pause = False






def score(count):
    font = pygame.font.SysFont("comicsansms", 35)  #set font type and size
    text = font.render("SCORE: " + str(count), True, red) # what to print, anti alias, color
    gameDisplay.blit(text, (0, 0)) #location of where to print to screen


def get_high_score():
    # Default high score
    high_score = 0

    # Try to read the high score from a file
    try:
        high_score_file = open("highscore.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        #print("The high score is", high_score)
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")

    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")

    return high_score


def save_high_score(new_high_score):

    current_score = 0
    hi_score = 0
    print current_score
    print hi_score
    print new_high_score

    if current_score >= high_score:

        try:
            # Write the file to disk
            high_score_file = open("highscore.txt", "w")
            high_score_file.write(str(new_high_score))
            high_score_file.close()
            print ("high score written")
        except IOError:
            # Hm, can't write it.
            print("Unable to save the high score.")


def lives_left(remain):
    font = pygame.font.SysFont("comicsansms", 35)  #set font type and size
    text = font.render("Lives: " + str(remain), True, red) # what to print, anti alias, color
    gameDisplay.blit(text, (0, 50)) #location of where to print to screen

def load_image(name_img):
    car = pygame.image.load(name_img)
    car = pygame.transform.scale(car, (60, 100)) # resize graphic
    return car.convert_alpha() # remove whitespace from graphic

carImg = load_image('racecar.png')
enemies_list = ['diablo.png', 'aventador.png', 'nsx.png', 'bike.png', 'Mach6.png', 'speeder.png', 'Stingray.png', 'slr.png' ] # add all other cars
randomCars = [load_image(img) for img in enemies_list]

def things(enemy, thingx, thingy, thingw, thingh, color):
    gameDisplay.blit(enemy, [thingx, thingy, thingw, thingh])

def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def crash():
    global life

    life -= 1
    #print (life)
    if life >= 0:
        #time.sleep(.5)
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(crash_sound)
        pygame.mixer.music.play()

        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("You Crashed", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        game_loop()

    elif life <= 0:
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(crash_sound)
        pygame.mixer.music.load("assets/sounds/crashed_music.wav")
        pygame.mixer.music.play()

        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("Game Over", largeText)
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

    pygame.mixer.music.pause()

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

    pygame.mixer.music.load("assets/sounds/intro.wav")
    pygame.mixer.music.play(-1)

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("Super Racer", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        largeText = pygame.font.SysFont("comicsansms", 30)
        TextSurf, TextRect = text_objects("Hi Score:  " + str(get_high_score()), largeText)
        TextRect.center = ((200,25))
        gameDisplay.blit(TextSurf, TextRect)

        button("LEGGO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause, high_score
    enemy = random.choice(randomCars)

    high_score = get_high_score()

    pygame.mixer.music.load('bgmusic.mp3')
    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0 # how to move player on x-axis

    thing_startx = random.randrange(0, display_width - 50) #random enemy x axis start
    thing_starty = -600 #start enemy off screen
    enemy_speed = 4 #initial speed of enemy
    thing_width = 55 #size for collision
    thing_height = 95 #size for collision
    enemy = random.choice(randomCars)

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
                    x_change = -5 #move player left on x axis
                if event.key == pygame.K_RIGHT:
                    x_change = 5 #move player right on x axis
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0 # when let up on key stop moving

        x += x_change # set variable equal to what is saved in x_change

        gameDisplay.blit(backgroundImage, (0, 0)) #show background image

        things(enemy, thing_startx, thing_starty, thing_width, thing_height, block_color) #place enemy


        thing_starty += enemy_speed # Move enemies closer to top of screen
        car(x, y)
        score(dodged * 1250) #sets the actual score
        current_score = dodged * 1250
        save_high_score(current_score)

        lives_left(life)


        if x > display_width - car_width or x < 0:# crash if hit the edge of screen
            crash()

        # adds score, increase difficulty
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            enemy = random.choice(randomCars)
            #enemy_speed += .25

            if dodged % 5 == 0:
                enemy_speed += (dodged * .5)



        if y < thing_starty + thing_height:


            # crash if hit enemy
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                time.sleep(.5)
                crash()



        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()