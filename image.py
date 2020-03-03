import pygame

pygame.init()

display_width = 500

display_hight = 500

gameDisplay = pygame.display.set_mode((display_width,display_hight))

pygame.display.set_caption('a bit racey')



white = (255,255,255)

clock = pygame.time.Clock()

crashed = False

carImg = pygame.image.load('3.jpg')

def car(x,y):
    gameDisplay.blit(carImg, (x , y))

x = 250

y = 250

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    gameDisplay.fill(white)
    car(x,y)
    pygame.display.update()
pygame.quit()
quit()
