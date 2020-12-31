import pygame
import random

# import .locals fo enhace getting access to Keyinputs coordinates

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# create player class

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("images/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_music.play()

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_music.play()

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # keep player on screen

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("images/missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )

        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)

        if self.rect.right < 0:
            self.kill()

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("images/cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed = 8

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        
        if self.rect.right < 0:
            self.kill()

# set mixer
pygame.mixer.init()

# Pygame must be initialized after you have imported the necessary thing you wish to use.
pygame.init()

# set clock
clock = pygame.time.Clock()



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# custome event
ADDENEMY = pygame.USEREVENT + 1
ADDCLOUD = pygame.USEREVENT + 2
# this will run the addenemy event after every 250 milliseconds
pygame.time.set_timer(ADDENEMY, 250)
pygame.time.set_timer(ADDCLOUD, 1000)

# instantiate player

player = Player()

# create spiret groups

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
clouds = pygame.sprite.Group()

all_sprites.add(player)

# load some music

pygame.mixer.music.load('sound/Sky_dodge_theme.ogg')
pygame.mixer.music.play(loops=-1)

# load in other music

move_up_music = pygame.mixer.Sound("sound/Jet_up.ogg")
move_down_music = pygame.mixer.Sound("sound/Jet_down.ogg")
collision_music = pygame.mixer.Sound("sound/Boom.ogg")

# GAME loop:
# Process user inpu
# control game speed
# update state of game object
# update the state of audion

# every cycle of the game is called a frame of the game

# All events will be placed in the event queue and each event has a type,
# we use the pygame.event.get() to get events in the event queue
running = True

while running:

    

    # look for events in the game
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == pygame.KEYDOWN:
            # Check if the key hit was an ESC key
            if event.key == K_ESCAPE:
                running = False

        # Check if the window close button is pressed
        elif event.type == QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)


    # Get pressed keys
    pressed_keys = pygame.key.get_pressed()

    # update player

    player.update(pressed_keys)
    enemies.update()
    clouds.update()

    # fill the screen
    screen.fill((135, 206, 250))

    # create another surface on which we can draw. Surfaces are rectangle on pygame on which we can draw.The screen above is a surface.

    # surf = pygame.Surface((50, 50))

    # # fill the surface
    # surf.fill((0, 0, 0))

    # rect = surf.get_rect()

    # # Now lets place the content on the screen, to do this we will need to use blit() which add the content to the screen and flip() which actually displays the content it copies the content of one surface onto another surface

    # surf_center = (
    #     (SCREEN_WIDTH - surf.get_width())/ 2,
    #     (SCREEN_HEIGHT-surf.get_height())/ 2
    # )

    for entities in all_sprites:
        screen.blit(entities.surf, entities.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        move_up_music.stop()
        move_down_music.stop()
        pygame.mixer.music.stop()
        pygame.time.delay(50)
        collision_music.play()
        pygame.time.delay(500)
        running = False

    # display player
    pygame.display.flip()
    clock.tick(30)


    # Sprite is a 2D representation of an image or object on the screen





pygame.mixer.music.stop()
pygame.mixer.quit()

pygame.quit()

# kenny.org
# gameart2d
# creativecomments
# freesound