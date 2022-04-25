import pygame
import time
from collections import namedtuple
from random import randint

class Level:

    def __init__(self, display):

        self.snake_head = [1000/2, 800/2]
        self._display = display
        self.block = 20
        self.snake_body = [self.snake_head, [self.snake_head[0] - self.block, self.snake_head[1]], [self.snake_head[0] - 2*self.block, self.snake_head[1]]]
        self.food = None
        self.score = 0
        self.direction = "RIGHT"
        self.spawn_food()


    def spawn_food(self):   
        
        x = randint(0, (1000 - self.block) // self.block) * self.block
        y = randint(0, (800 - self.block) // self.block) * self.block
        self.food = [x, y]
        if self.food in self.snake_body:
            self.spawn_food()


    def render(self):

        for block in self.snake_body:

            pygame.draw.rect(self._display, (0,201,87), pygame.Rect(block[0], block[1], self.block, self.block))

        pygame.draw.rect(self._display, (220,20,60), pygame.Rect(self.food[0], self.food[1], self.block, self.block))

        font = font = pygame.font.SysFont('arial', 25)
        text = font.render(f"Pisteet: {self.score}", True, (240,255,255))
        self._display.blit(text, [0, 0])

        pygame.display.update()


    def check_food(self):

        self.snake_body.insert(0, self.snake_head)
        if self.snake_head == self.food:
                self.score += 1
                self.spawn_food()

        else:
            self.snake_body.pop()


    def check_collisions(self):

        if self.snake_head[0] > 1000 - self.block or self.snake_head[1] > 800 - self.block or self.snake_head[0] < 0 or self.snake_head[1] < 0:
            return True
        
        if self.snake_head in self.snake_body[1:]:
            return True

        return False

    
    def move_snake(self):

        x = self.snake_head[0]
        y = self.snake_head[1]

        if self.direction == "UP":

            y -= self.block

        elif self.direction == "DOWN":

            y += self.block

        elif self.direction == "RIGHT":

            x += self.block

        elif self.direction == "LEFT":

            x -= self.block
        
        self.snake_head = [x, y]


    def game_over(self):

        font = font = pygame.font.SysFont('arial', 90)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        game_over_text_rect = game_over_text.get_rect()

        self._display.fill((0, 0, 0))
        self._display.blit(game_over_text, game_over_text_rect)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()

    

        