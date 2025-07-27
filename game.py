import pygame
import sys
import random

pygame.init()

width = 500
height = 500
cell = 20

# Define colors in RGB format
snake_colour = (193, 95, 110) 
Food_colour = (107, 77, 255)   
BG_COLOR = (17, 17, 17)        

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("snake game'J.I'")
Time = pygame.time.Clock()
running = True

class Snake:
    def __init__(self):
        self.body = [(cell, cell)]
        self.dx, self.dy = cell, 0
        self.colour = snake_colour

    def move(self):
        x, y = self.body[0]
        new_head = (x + self.dx, y + self.dy)
        new_head = ((new_head[0] % width), (new_head[1] % height))
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        x, y = self.body[0]
        new_head = (x + self.dx, y + self.dy)
        new_head = ((new_head[0] % width), (new_head[1] % height))
        self.body.insert(0, new_head)

    def set_direction(self, dx, dy):
        if (dx, dy) != (-self.dx, -self.dy):
            self.dx, self.dy = dx, dy

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(screen, self.colour, (x, y, cell, cell))

class Food:
    def __init__(self):
        self.pos = self.random_food()

    def random_food(self):
        return (random.randrange(0, width // cell) * cell,
                random.randrange(0, height // cell) * cell)

    def draw(self):
        x, y = self.pos
        pygame.draw.rect(screen, Food_colour, (x, y, cell, cell))

class game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()

    def run(self):
        global running
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.snake.set_direction(0, cell)
                    elif event.key == pygame.K_UP:
                        self.snake.set_direction(0, -cell)
                    elif event.key == pygame.K_LEFT:
                        self.snake.set_direction(-cell, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.set_direction(cell, 0)

            self.snake.move()
            if self.snake.body[0] == self.food.pos:
                self.snake.grow()
                self.food.pos = self.food.random_food()
            
            screen.fill(BG_COLOR)
            self.snake.draw()
            self.food.draw()
            pygame.display.flip()
            Time.tick(10)

if __name__ == "__main__":
    game_instance = game()
    game_instance.run()
    pygame.quit()
    sys.exit()