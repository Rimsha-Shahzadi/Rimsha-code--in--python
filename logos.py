import pygame
pygame.init()
width = 700
height = 400
screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("My Logo Window")

running = True
print("start----")

img = pygame.image.load("logo.png")
img = pygame.transform.scale(img, (200, 200))
x = 200
y = 100
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fil((0, 0, 0))
    screen.blit(img,(x, y))
    pygame.display.update()
pygame.quit()
print("end---")