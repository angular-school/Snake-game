import pygame
import random

square_colour = (255, 0, 100)

class Square(pygame.sprite.Sprite):
	def __init__(self, x, y, side, speed_x, speed_y):
		super().__init__()
		self.side = side
		self.image = pygame.Surface([side, side])
		self.image.fill(square_colour)
		self.speed_x = speed_x
		self.speed_y = speed_y

		self.rect=self.image.get_rect()
		self.rect.x=x
		self.rect.y=y

	def update(self):
		self.rect.x = self.rect.x + self.speed_x
		self.rect.y = self.rect.y + self.speed_y
		if self.rect.x > 800:
			self.rect.x = -self.side
		if self.rect.x < -self.side:
			self.rect.x = 800
		if self.rect.y > 600:
			self.rect.y = -self.side
		if self.rect.y < -self.side:
			self.rect.y = 600

my_square = Square(400, 300, 150, 4, 0)
my_square2 = Square(400, 100, 50, -3, 1)

allspriteslist = pygame.sprite.Group()

for i in range(100):
    s = Square(400 - 20/2 + i*30,300 - 20/2, 20, random.randint(-3,3), random.randint(-3,3))
    allspriteslist.add(s)

pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption('Snake Example')
clock = pygame.time.Clock()

background_colour = (225,0,0)
done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
			    done = True
			if event.key == pygame.K_r:
			    square_colour = (random.randint(0, 255), 0, 0)
			if event.key == pygame.K_b:
			    background_colour = (0,0,200)
			if event.key == pygame.K_g:
			    background_colour = (0,200,0)

	my_square.image.fill(square_colour)
	screen.fill(background_colour)
	allspriteslist.draw(screen)
	pygame.display.flip()
	allspriteslist.update()

	clock.tick(24)
pygame.quit()
