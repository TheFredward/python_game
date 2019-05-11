import pygame
from random import randint
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
# initiallize font from pygame
pygame.font.init()
font = pygame.font.SysFont('microsoftphagspa',50)
"""The next edits will be focused on adding various enemies at a time using an array, expect to have about 5 max, after that the next step will be to have them move in all directions."""
class Game():
    # similar to FPS
    TICK_RATE = 60
    npc_list = []

    # initiallizer for the game class
    def __init__(self,imagePath,title,width,height):
        self.title = title
        self.width = width
        self.height = height
        # library pygame takes in a tuple of the screen's width and height and will create a window based on this size
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)
        # save the image to backgournd image and then transform and save to self.image to use for display later on
        background_img = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(background_img,(width,height))
    # function to run the game
    def run_game(self, mlvlSpeed):
         # variable for a loop to determine wether to end the game
        is_game_over = False
        direction = 0
        did_win = False
        # create a random postion for the enemies
        enemy_posX = randint(200,500)
        # initiallize PlayerChar npc_char and treasure
        plyrChar = PlayerChar('Images/player.png',375,700,50,50)
        npc_char= NPC('Images/enemy.png',40,enemy_posX,50,50)
        self.npc_list.append(npc_char)
        npc_char.SPEED *= mlvlSpeed
        treasure = GameObject('Images/treasure.png', 375,50,50,50)
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
            self.game_screen.fill(WHITE_COLOR)
            self.game_screen.blit(self.image,(0,0))
            # update position of character and then draw
            treasure.draw(self.game_screen)
            plyrChar.move(direction,self.height)
            plyrChar.draw(self.game_screen)
            if len(self.npc_list) > 0:
                i = 0
                while i < len(self.npc_list):
                    self.npc_list[i].move(self.width)
                    self.npc_list[i].draw(self.game_screen)
                    # spawn new enemy after level xx has been reached
                    if mlvlSpeed > 2:
                        self.npc_list[i].move(self.width)
                        self.npc_list[i].draw(self.game_screen)
                    i += 1
            # after the movement is done we need to detect if collision has occured
            for enemies in self.npc_list:
                if plyrChar.collDetection(enemies):
                    is_game_over = True
                    did_win = False
                    # create a text box to display
                    text = font.render('Game Over',True, BLACK__COLOR)
                    self.game_screen.blit(text,(300,350))
                    pygame.display.update()
                    clock.tick(2)
                    break
                elif plyrChar.collDetection(treasure):
                    is_game_over = True
                    did_win = True
                    # display for if the user wins
                    text = font.render('You win',True, BLACK__COLOR)
                    self.game_screen.blit(text,(300,350))
                    pygame.display.update()
                    clock.tick(2)
                    break
            # renders and draws on display
            # game_screen.blit(plyr_img,(375,375))
            pygame.display.update()
            clock.tick(self.TICK_RATE)
        if did_win:
            # recursion occurring here, so it will continue running
            self.run_game(mlvlSpeed + 0.35)
        else:
            return
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
    def collDetection(self, mNpc_char):
        if self.y_pos > mNpc_char.y_pos + mNpc_char.height:
            return False
        elif self.y_pos + self.height < mNpc_char.y_pos:
            return False
        if self.x_pos > mNpc_char.x_pos + mNpc_char.width:
            return False
        elif self.x_pos + self.width < mNpc_char.x_pos:
            return False
        return True
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
new_game = Game('Images/background.png',SCREEN_TITLE,SCREEN_WIDTH,SCREEN_HEIGHT)
new_game.run_game(1)

pygame.quit()
quit()
