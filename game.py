import pygame
# must call and initiallize pygame
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossroads'
# tuple of RGB
WHITE_COLOR = (255,255,255)
RED_COLOR = (255,0,0)
BLUE_COLOR = (0,0,255)
BLACK__COLOR = (0,0,0)
# determine how long the loop will run, FPS
clock = pygame.time.Clock()
TICK_RATE = 60
# global variable for a loop to determine wether to end the game
is_game_over = False
# library pygame takes in a tuple of the screen's width and height and will create a window based on this size
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_screen.fill(WHITE_COLOR)
plyr_img = pygame.image.load('Images/player.png')
plyr_img = pygame.transform.scale(plyr_img,(50,50))
pygame.display.set_caption(SCREEN_TITLE)
# to exit this while not loop we will use event listeners
while not is_game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True
        print(event)
    # renders and draws on display
    # pygame.draw.rect(game_screen,RED_COLOR, [350,350,100,100])
    # pygame.draw.circle(game_screen,BLUE_COLOR, (400,300),50)
    game_screen.blit(plyr_img,(375,375))
    pygame.display.update()
    clock.tick(TICK_RATE)
pygame.quit()
quit()
