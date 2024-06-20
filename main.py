import pygame
import math

# pygame setup
pygame.init()

# screen = pygame.display.set_mode((1280, 720))
screen = pygame.display.set_mode((1080, 920))
clock = pygame.time.Clock()
running = True

size = 32

ground_arr = [(0, 9), (1,10), (2,10), (6,10)]

def check_grounded(user):
  return ( ( math.floor(user.get_x() / size), math.floor( (user.get_y() + size) / size ) ) in ground_arr or
           ( math.floor( (user.get_x() + size ) / size), math.floor( (user.get_y() + size) / size ) ) in ground_arr
         )

class Probie():
  def __init__(self, x, y, vel_x, vel_y, grounded, jumping):
    self.x = x
    self.y = y
    self.vel_x = vel_x
    self.vel_y = vel_y
    self.grounded = grounded
    self.jumping = jumping
  
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

  def is_jumping(self):
    return self.jumping

  def set_jumping(self, val):
    self.jumping = val

def initialize_probie():
  return Probie(size, 9 * size, 0, 0, True, False)

p = initialize_probie()


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_p:
        print(p.y)
      if event.key == pygame.K_r:
        p = initialize_probie()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    p.set_x(p.get_x() - size/4)
  if keys[pygame.K_RIGHT]:
    p.set_x(p.get_x() + size/4)
  if keys[pygame.K_UP]:
    if p.is_grounded():
      p.set_vel_y(-4 * size/4)
      p.set_grounded(False)
      p.set_jumping(True)

  if p.is_jumping() and p.get_vel_y() >= 0:      
    p.set_jumping(False)


  if not p.is_jumping():
    p.set_grounded(check_grounded(p))


  if p.is_grounded():
    p.set_vel_y(0)
    p.set_y((p.get_y()) - (p.get_y() % size))
  else:
  # if not p.is_grounded():
    p.set_vel_y(p.get_vel_y() + size/16)

  p.set_x(p.get_x() + p.get_vel_x())
  p.set_y(p.get_y() + p.get_vel_y())




  screen.fill("black")  
  # fill the screen with a color to wipe away anything from last frame

  # RENDER YOUR GAME HERE

  
  pygame.draw.rect(screen, "pink", (p.get_x(),p.get_y(),size,size))
  for ele in ground_arr:
    pygame.draw.rect(screen, "darkgreen", (ele[0] * size, ele[1] * size,size,size))




  # flip() the display to put your work on screen
  pygame.display.flip()


  dt = clock.tick(60) / 1000

pygame.quit()