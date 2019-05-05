import pygame
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
class Game():
    # similar to FPS
    TICK_RATE = 60

    # initiallizer for the game class
    def __init__(self, title,width,height):
        self.title = title
        self.width = width
        self.height = height
        # library pygame takes in a tuple of the screen's width and height and will create a window based on this size
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)
    # function to run the game
    def run_game(self):
         # variable for a loop to determine wether to end the game
        is_game_over = False
        direction = 0
        # initiallize PlayerChar
        plyrChar = PlayerChar('Images/player.png',375,700,50,50)
        npc_char = NPC('Images/enemy.png',20,400,50,50)
        # to exit this while not loop we will use event listeners specifically for this it will be w or s for up down
        while not is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                # detect if the key has been pressed down
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                # detect if the key has been released
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)
            self.game_screen.fill(WHITE_COLOR)
            # update position of character and then draw
            plyrChar.move(direction,SCREEN_HEIGHT)
            plyrChar.draw(self.game_screen)
            npc_char.move(self.width)
            npc_char.draw(self.game_screen)
            # renders and draws on display
            # game_screen.blit(plyr_img,(375,375))
            pygame.display.update()
            clock.tick(self.TICK_RATE)
class GameObject():
    def __init__(self, image_path,x_pos,y_pos,width,height):
        plyrObjct_img = pygame.image.load(image_path)
        # scale image up
        self.image = pygame.transform.scale(plyrObjct_img,(width,height))
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
    def draw(self, background):
        background.blit(self.image,(self.x_pos,self.y_pos))
# class for character movement
class PlayerChar(GameObject):
    # speed used to change direction movement
    SPEED = 10
    def __init__(self, image_path,x_pos,y_pos,width,height):
        super().__init__(image_path,x_pos,y_pos,width,height)
    def move(self,direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED
        # creates a lower bounds to prevent the player from going out of bounds
        if self.y_pos >= max_height -40:
            self.y_pos = max_height -40
class NPC(GameObject):
    # speed used to change direction movement
    SPEED = 5
    def __init__(self, image_path,x_pos,y_pos,width,height):
        super().__init__(image_path,x_pos,y_pos,width,height)
    def move(self,max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 60:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED

# must call and initiallize pygame
pygame.init()
# new instance of game
new_game = Game(SCREEN_TITLE,SCREEN_WIDTH,SCREEN_HEIGHT)
new_game.run_game()

pygame.quit()
quit()
