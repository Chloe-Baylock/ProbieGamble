import pygame

# pygame setup
pygame.init()

# screen = pygame.display.set_mode((1280, 720))
screen = pygame.display.set_mode((1080, 920))
clock = pygame.time.Clock()
running = True

size = 32

class Probie():
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def set_x(self, x):
    self.x = x
  
  def get_x(self):
    return self.x

  def set_y(self, y):
    self.y = y
  
  def get_y(self):
    return self.y

p = Probie(size, size)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        p.set_x(p.get_x() - size)
      if event.key == pygame.K_RIGHT:
        p.set_x(p.get_x() + size)
      if event.key == pygame.K_UP:
        p.set_y(p.get_y() - size)
      if event.key == pygame.K_DOWN:
        p.set_y(p.get_y() + size)
        

  screen.fill("black")  
  # fill the screen with a color to wipe away anything from last frame

  # RENDER YOUR GAME HERE

  
  pygame.draw.rect(screen, "pink", (p.get_x(),p.get_y(),size,size))




  # flip() the display to put your work on screen
  pygame.display.flip()


  dt = clock.tick(60) / 1000

pygame.quit()