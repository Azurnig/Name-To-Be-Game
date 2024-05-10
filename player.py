import pygame
from pygame import font


class Player():
  def __init__(self, x, y):
      self.x = x
      self.y = y
      self.width = 50
      self.height = 50
      self.speed = 5

  def draw(self, screen):
      pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))

  def move(self):
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT]:
          self.x -= self.speed
      if keys[pygame.K_RIGHT]:
          self.x += self.speed
      if keys[pygame.K_UP]:
          self.y -= self.speed
      if keys[pygame.K_DOWN]:
          self.y += self.speed

