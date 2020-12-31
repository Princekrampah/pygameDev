# import pygame and initialize it
import pygame
# initialization enables us to work with the same code on Windows, Mac and Linux
pygame.init()

# create pygame screen
screen = pygame.display.set_mode((500, 500))

# Create game loop

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill screen with white background
    screen.fill((255, 255, 255))

    # Draw circle
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # flip the screen
    # this pushes all the content we created to the display
    pygame.display.flip()

pygame.quit()

