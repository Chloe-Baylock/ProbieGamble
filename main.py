import pygame

# pygame setup
pygame.init()

# screen = pygame.display.set_mode((1280, 720))
screen = pygame.display.set_mode((1080, 920))
clock = pygame.time.Clock()
running = True

size = 32

class Probie():
  def __init__(self, x, y, vel_x, vel_y, grounded):
    self.x = x
    self.y = y
    self.vel_x = vel_x
    self.vel_y = vel_y
    self.grounded = grounded
  
  def get_x(self):
    return self.x

  def set_x(self, x):
    self.x = x
  
  def get_y(self):
    return self.y

  def set_y(self, y):
    self.y = y
  
  def get_vel_x(self):
    return self.vel_x

  def set_vel_x(self, vel_x):
    self.vel_x = vel_x

  def get_vel_y(self):
    return self.vel_y

  def set_vel_y(self, vel_y):
    self.vel_y = vel_y

  def is_grounded(self):
    return self.grounded

  def set_grounded(self, val):
    self.grounded = val

p = Probie(size, 10 * size, 0, 0, True)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    p.set_x(p.get_x() - size/4)
  if keys[pygame.K_RIGHT]:
    p.set_x(p.get_x() + size/4)
  if keys[pygame.K_UP]:
    if p.is_grounded():
      p.set_vel_y(-4 * size/4)
      p.set_grounded(False)
        
  
  if not p.is_grounded():
    p.set_vel_y(p.get_vel_y() + size/4)

  p.set_x(p.get_x() + p.get_vel_x())
  p.set_y(p.get_y() + p.get_vel_y())

  screen.fill("black")  
  # fill the screen with a color to wipe away anything from last frame

  # RENDER YOUR GAME HERE

  
  pygame.draw.rect(screen, "pink", (p.get_x(),p.get_y(),size,size))




  # flip() the display to put your work on screen
  pygame.display.flip()


  dt = clock.tick(60) / 1000

pygame.quit()