#   This game is built from scratch based on the idea of sentdex youtube videos with some extra functions.
#   You are free to edit and re-distribute the code wherever you like , Just don't forget to mention me somewhere :)
#   Built By : M41k Dev3lops
#   Thanks To : Sentdex

from functions.settings import *
from functions.colors import *
from functions.funcs import *
import time
import random

pause = False


#   This doesn't require explanation
def quit_game():
    pygame.quit()
    quit()


#   Crash Function
def crash(score):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.load("assets/sounds/crashed_music.wav")
    pygame.mixer.music.play()

    high_score = get_high_score()
    file_handler = open('sts.m41k', 'w')
    score = int(score)
    str_score = str(score)
    if high_score is not None:
        if score > int(high_score):
            file_handler.write(str_xor(str_score, "YeahDudeWhatever#231231^*^&(**&)("))
    elif score > 0:
        file_handler.write(str(str_xor(str_score, "YeahDudeWhatever#231231^*^&(**&)(")))

    file_handler.close()

    display_msg("You Crashed :-(", 25, white, (window_width / 2), (window_height / 2))
    time.sleep(1)
    while True:
        display_msg("Do you want to play again ? Y/N", 20, white, (window_width / 2), (window_height / 2) + 50)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    game_loop()
                elif event.key == pygame.K_n:
                    quit_game()
            elif event.type == pygame.QUIT:
                quit_game()


def intro():
    # The intro
    # It would be boring of me to say don't edit it, So U r free to edit the intro. Just don't forget to mention me somewhere :)
    pygame.mixer.music.load("assets/sounds/intro.wav")
    pygame.mixer.music.play(-1)

    display_msg("M41k Dev3lops", 40, bright_red, (window_width / 2), (window_height * 0.1))
    time.sleep(1)
    display_msg("Presents :", 25, bright_red, (window_width / 2), (window_height * 0.2))
    time.sleep(1)
    display_msg("RacerZ :-)", 35, bright_red, (window_width / 2), (window_height * 0.3))
    time.sleep(1)
    high_score = get_high_score()

    if high_score is not None:
        display_msg("High Score : " + str(high_score), 20, white, (window_width / 2), (window_height * 0.4))
    else:
        display_msg("No High Score Yet !", 20, white, (window_width / 2), (window_height * 0.4))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    game_loop()

        button("GO !", 100, (window_height * 0.7), 150, 100, green, bright_green, 20, game_loop)
        button("Quit", 600, (window_height * 0.7), 150, 100, red, bright_red, 20, quit_game)

        pygame.display.update()
        clock.tick(15)


def unpause():
    global pause
    pause = False


def Pause():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        # surface.fill(black)
        display_msg("Paused", 25, red, window_width / 2, window_height / 2)

        button("Continue", 150, (window_height * 0.7), 150, 100, green, bright_green, 20, unpause)
        button("New Game", 350, (window_height * 0.7), 150, 100, grey, diff_grey, 20, game_loop)
        button("Quit", 550, (window_height * 0.7), 150, 100, red, bright_red, 20, quit_game)
        pygame.display.update()
        clock.tick(15)


def game_loop():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("assets/sounds/main.wav")
    pygame.mixer.music.play(-1)
    global pause

    #   Starting Vars
    car_width = 73
    car_x = (window_width / 2) - (car_width / 2)
    car_y = window_height * 0.87
    car_speed = 10
    car_x_change = 0
    block_w = 120
    block_x_list = [random.randrange(0, window_width - block_w)]
    block_h = 100
    block_y = -600
    block_speed = 7
    block_count = 1
    score = 0
    high_score = get_high_score()

    while True:

        # Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    car_x_change += - car_speed
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    car_x_change += car_speed
                if event.key == pygame.K_p:
                    pause = True
                    Pause()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car_x_change = 0

        # Touched The Boundaries
        if (car_x + car_width) > window_width or car_x < 0:
            crash(score)

        # Touched Block
        if car_y < block_y + block_h:
            for block_x in block_x_list:
                if block_x < car_x < block_x + block_w or block_x < car_x + car_width < block_x + block_w:
                    crash(score)

        # Repeat Blocks
        if block_y > window_height:
            block_x_list = []
            block_y = -100
            for x in range(block_count):
                block_x_new = random.randrange(0, window_width - block_w)
                block_x_list.append(block_x_new)

            block(block_x_list, block_y, block_w, block_h, green)
            score += 1
            if score % 5 == 0:
                block_speed += 2
                car_speed += 2

            if score % 10 == 0:
                if block_count < 4:
                    block_count += 1

        # Extra Variables
        surface.fill(black)
        car_x += car_x_change
        block_y += block_speed

        #   Graphics
        surface.blit(car_obj, (car_x, car_y))
        block(block_x_list, block_y, block_w, block_h, green)
        display_msg("Score : " + str(score), 15, white, 40, 20)
        if high_score is not None:
            display_msg("High Score : " + str(high_score), 15, bright_green, 60, 40)
            high_score = int(high_score)
            if score >= high_score:
                display_msg("New High Score !", 10, bright_red, 70, 60)
                high_score = score

        # Update Display
        pygame.display.update()
        clock.tick(30)


intro()
quit_game()