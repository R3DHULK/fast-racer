import pygame
import time
import random
pygame.init()

display_width = 800
display_height = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

gameDisplay = pygame.display.set_mode((display_width,display_height)) # Set size of display
pygame.display.set_caption("Fast Racer") # set window title
gameClock = pygame.time.Clock() #Sets frame per sec

backgroundImage = pygame.image.load("background.png")
backgroundImage = pygame.transform.scale(backgroundImage, (800, 600))
gameDisplay.blit(backgroundImage, (0, 0))

carImage = pygame.image.load("racecar.png")
carImage = pygame.transform.scale(carImage, (60, 75)) # resize graphic
carImage = carImage.convert_alpha() # remove whitespace from graphic

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


#################  Functions  #####################

def car(x,y):
    gameDisplay.blit(carImage,(x,y)) #blit writes images to screen
    enemy = random.choice(randomCars)


def crash():
    message_display("You Crashed!")

def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("You dodged:  " + str(count), True, BLUE)
    gameDisplay.blit(text, (10,0))



def things(thingX, thingY, thingWidth, thingHeight, color):
    #pygame.draw.rect(gameDisplay, color, [thingX, thingY, thingWidth, thingHeight])
    gameDisplay.blit(enemy,[thingX, thingY, thingWidth, thingHeight] )

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text, largeText) #text surface and rectange
    TextRect.center = ((display_width /2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2) #pause for 2 seconds
    game_loop()# start game loop back

def game_loop():

    x = (display_width * .45)
    y = (display_height * 0.8)

    thing_startX = random.randrange(0,display_width)
    thing_startY = -600 #start off screen
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    car_width = 60
    x_change = 0
    dodged = 0


    ########### Set Game loop   #########


    gameExit = False #set parameter if crash

    while not gameExit:
        ####### Event handling loop  ##############

        for event in pygame.event.get(): #gets list of all events per frame
            if event.type == pygame.QUIT:  #if hit the close key
                pygame.QUIT()
                quit()

            if event.type == pygame.KEYDOWN: #Check if any key pressed
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP: #released keys
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0 #Stop changing x axis



        x += x_change
        #print enemy
        #gameDisplay.fill(WHITE)
        gameDisplay.blit(backgroundImage, (0, 0))

        things(thing_startX, thing_startY, thing_width, thing_height, BLACK )
        thing_startY += thing_speed


        car(x,y)
        score(dodged)

        if x > display_width - car_width  or x < 0: #Set game over if hit borders
            crash()

        if thing_startY > display_height:
            thing_startY = 0 - thing_height
            thing_startX = random.randrange(0, display_width)
            dodged += 1
            thing_speed += .25




            if x > thing_startX and x < thing_startX + thing_width or x + car_width > thing_startX and x + car_width < thing_startX + thing_width:
                #print('x crossover')
                crash()

            #gameExit = True
            #print (event) # See all events tracking

        pygame.display.update()  #updates the entire screen

        gameClock.tick(60) #set actual frames per sec



game_loop()

pygame.QUIT()
quit()
