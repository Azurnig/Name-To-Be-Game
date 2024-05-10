import pygame
import sys

from button import Button
from player import Player
pygame.init()

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("NameToBe!")

pink = (255, 182, 193)
white = (255, 255, 255)

font = pygame.font.Font('freesansbold.ttf', 32)

def start_game():
  print("Starting the game!")

start_button = Button(200, 150, 200, 50, "Start Game", start_game)
options_button = Button(200, 225, 200, 50, "Options")  

player = Player(250, 200)  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_button.clicked(event.pos)
            options_button.clicked(event.pos)  

   
    screen.fill(pink)

    Button.draw(start_button, screen)
    

    pygame.display.update()

pygame.quit()
sys.exit()








# The loop will carry on until the user exits the game (e.g. clicks the close button).

run = True


# -------- Main Program Loop -----------

while run:

    # --- Main event loop

    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close

            run = False


    screen.fill((20, 15, 15))

    screen.blit(display_name, (150, 150))

    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:

pygame.quit()
