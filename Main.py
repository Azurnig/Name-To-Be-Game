import pygame


# set up pygame modules

pygame.init()

pygame.font.init()

my_font = pygame.font.SysFont('Arial', 16)

pygame.display.set_caption("NameToBe")


# set up variables for the display

size = (700, 500)

screen = pygame.display.set_mode(size)


name = "Welcome to NameToBe"


# render the text for later

display_name = my_font.render(name, True, (255, 255, 255))


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
