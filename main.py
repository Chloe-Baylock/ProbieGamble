import pygame
import math

# notes

# level editor
# upward collisions next

# annoying that probie cannot be on the very edge of some blocks without falling off.
# dont fully understand the horizontal collision
# downward collision can probably glitch through blocks at high speed.

# pygame setup
pygame.init()

# screen = pygame.display.set_mode((1280, 720))
width = 1080
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

size = 32
is_editing = False

font = pygame.font.SysFont("Arial", 29)
text_surf = font.render("Editor", True, "black")



# ground_arr = [(0, 9), (1,10), (2,9), (2,10), (3,9), (5,11), (6,9), (6,10)]
ground_arr = [(6, 10), (9, 12), (13, 12), (15, 12), (18, 7), (10, 3), (12, 8), (22, 12), (23, 14), (16, 18), (6, 17), (15, 13), (21, 16), (9, 11), (11, 15), (10, 15), (1, 20), (2, 20), 
(3, 20), (0, 20), (0, 19), (0, 16), (0, 15), (0, 17), (0, 18), (0, 14), (0, 13), (0, 12), (0, 11), (0, 10), (0, 8), (0, 9), (0, 7), (0, 5), (0, 6), (1, 5), (2, 6), (2, 5), 
(3, 6), (3, 5), (4, 5), (5, 5), (6, 5), (2, 2), (6, 2), (17, 7), (15, 7), (16, 7), (20, 6), (20, 5), (22, 5), (21, 5), (23, 5), (23, 7), (23, 8), (23, 9), (23, 6), (23, 10), (23, 12), (23, 11), (21, 17), (20, 18), (12, 21), (15, 21), (18, 21), (21, 21), (23, 21), (17, 21), (20, 21), (24, 21), (25, 21), (26, 21), (24, 10), (10, 11), (3, 15), (1, 10), (2, 10), (3, 10), (7, 10), (7, 17), (8, 17), (28, 14), (30, 14), (29, 14), (32, 13), (32, 11), (32, 12), (31, 13), (30, 19), (31, 19), (32, 19), (24, 14), (28, 4), 
(29, 4), (30, 4), (24, 2), (23, 2), (22, 1), (21, 0), (14, 2), (15, 2), (16, 2), (28, 1), (30, 1), (27, 3), (31, 3)]

def check_grounded(user):
  return ( ( math.floor(user.get_x() / size), math.floor( (user.get_y() + size) / size ) ) in ground_arr or
           ( math.floor( (user.get_x() + size ) / size), math.floor( (user.get_y() + size) / size ) ) in ground_arr
         )

def hor_collision(user, new_dest_x):
  return ( math.floor(new_dest_x / size), math.floor( user.get_y() / size ) ) in ground_arr

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

  mouse_pos = pygame.mouse.get_pos()
  mouse_x = mouse_pos[0]
  mouse_y = mouse_pos[1]
  if mouse_x >= width - size * 2 and mouse_y < size:
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
  else:
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
  # checking if mouse is over edit button

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_p:
        print(ground_arr)
      if event.key == pygame.K_r:
        p = initialize_probie()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if mouse_x >= width - size * 2 and mouse_y < size:
        is_editing = not is_editing
      elif is_editing and ( math.floor(mouse_x / size), math.floor(mouse_y / size) ) in ground_arr:
        ground_arr.remove( (math.floor(mouse_x / size), math.floor(mouse_y / size)) )
      elif is_editing:
        ground_arr.append( (math.floor(mouse_x / size), math.floor(mouse_y / size)))

  keys = pygame.key.get_pressed()
  if keys[pygame.K_q]:
    running = False
  if keys[pygame.K_LEFT]:
    if not hor_collision(p, p.get_x() - size/4):
      p.set_x(p.get_x() - size/4)
  if keys[pygame.K_RIGHT]:
    if not hor_collision(p, p.get_x() + size):
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
  
  if is_editing:
    pygame.draw.rect(screen, "red", (width - size * 2, 0 , 2 * size, size))
  else:  
    pygame.draw.rect(screen, "cyan", (width - size * 2, 0 , 2 * size, size))

  screen.blit(text_surf, (width - size * 2, 0))



  # flip() the display to put your work on screen
  pygame.display.flip()


  dt = clock.tick(60) / 1000

pygame.quit()