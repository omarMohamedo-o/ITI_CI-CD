import pygame
import sys
import random 

pygame.init()

width=500
height=500
screen=pygame.display.set_mode((width,height))
Name= pygame.display.set_caption("snake game'J.I'")  # PROBLEM 1: Unnecessary assignment
# PROBLEM 1: Assigning pygame.display.set_caption() to 'Name' is pointless because set_caption() returns None. This doesn't affect functionality but is confusing and unnecessary.
Time=pygame.time.Clock( )  # PROBLEM 2: Confusing variable name
# PROBLEM 2: Naming the clock 'Time' is unconventional. It should be 'clock' for clarity, as it's a pygame.time.Clock object used for frame rate control. Not used in the loop, so it has no effect yet.
cell=20
snake_colour="#C15F6E"  # PROBLEM 3: Incorrect color format
# PROBLEM 3: Hex string "#C15F6E" is used directly in pygame.draw.rect later, which expects an RGB tuple (e.g., (193, 95, 110)). This causes a TypeError when drawing the snake.
Food_colour="#6B4DFF"   # PROBLEM 4: Incorrect color format
# PROBLEM 4: Same as above; hex string "#6B4DFF" will cause a TypeError in pygame.draw.rect for the food.
BG_COLOR = "#111111"    # PROBLEM 5: Incorrect color format
# PROBLEM 5: Hex string "#111111" will cause a TypeError in screen.fill() if used. Contributes to no background rendering.
 
running=True

class Snake:
    def __init__(self):
        self.body=[(cell,cell)]
        self.dx,self.dy=cell,0
        self.colour=snake_colour

    def grow(self):  # PROBLEM 6: Misnamed method
    # PROBLEM 6: Named 'grow' but actually moves the snake (adds new head, removes tail). Should be 'move', as 'grow' implies increasing length (e.g., when eating food). Doesn't directly cause black screen but is a logical error.
        x, y = self.body[0]
        new_head = (x + self.dx, y + self.dy)
        self.body.insert(0, new_head)
        self.body.pop()

    def set_direction(self, dx, dy):
        if (dx, dy) != (-self.dx, -self.dy):
            self.dx, self.dy = dx, dy

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(screen, snake_colour, (x, y, cell, cell))  # PROBLEM 7: Incorrect color usage
            # PROBLEM 7: Uses 'snake_colour' (hex string) instead of 'self.colour' or an RGB tuple, causing a TypeError when drawing. Prevents snake rendering.

class Food:
    def __init__(self):
        self.pos= self.random_food( ) 

    def random_food():  # PROBLEM 8: Missing 'self' parameter
    # PROBLEM 8: 'random_food' lacks 'self' parameter, making it a static method. Calling self.random_food() in __init__ causes TypeError: random_food() takes 0 positional arguments but 1 was given. Prevents Food instantiation.
        return(random.randrange(0, width // cell) * cell,
              random.randrange(0, height // cell) * cell)

    def draw(self):
        pygame.draw.rect(screen,Food_colour(self.pos,cell,cell))  # PROBLEM 9: Syntax error and incorrect color
        # PROBLEM 9: Incorrect syntax: 'Food_colour' is treated as a function, and arguments are malformed. Should be pygame.draw.rect(screen, Food_colour, (x, y, cell, cell)). Also, 'Food_colour' is a hex string, causing a TypeError. Prevents food rendering.

class game:  # PROBLEM 10: Invalid class syntax with while loop
# PROBLEM 10: Defining a while loop directly in the class body is syntactically incorrect. Python expects methods or attributes, not executable code. Causes a SyntaxError or prevents the loop from running, leading to a black screen.
    while running:

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                    sys.exit( )
                elif event.type==pygame.KEYDOWN:  # PROBLEM 11: Incorrect key event handling
                # PROBLEM 11: Checks KEYDOWN but then checks K_LEFT and K_RIGHT as event types, which is wrong. pygame.K_LEFT, etc., are key constants checked via event.key. Also, KEYDOWN and KEYUP logic is incomplete (only sets dy for vertical movement).
                    dx,dy=0,cell
                elif event.type==pygame.KEYUP:
                    dx,dy=0,-cell
                elif event.type==pygame.K_LEFT:
                    dx,dy=-cell,0
                elif event.type==pygame.K_RIGHT:
                    dx,dy=cell,0
        # PROBLEM 12: Missing game logic and rendering
        # PROBLEM 12: The loop (if it ran) only handles events but doesn't update the snake, check collisions, clear the screen, draw objects, or call pygame.display.flip(). This ensures nothing is rendered, causing a black screen.

pygame.quit( )  # PROBLEM 13: Premature program exit
sys.exit( )    # PROBLEM 13: Premature program exit
# PROBLEM 13: pygame.quit() and sys.exit() are called immediately after the class definition, exiting the program before the game loop can run. This ensures only a black screen (or no window) appears.