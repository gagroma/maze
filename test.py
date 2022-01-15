import pygame
pygame.init()

win = pygame.display.set_mode((700, 500))
display.set_caption("фвіфв")
#win.fill((123, 76, 31))
back = pygame.transform.scale(
    pygame.image.load("adonail.png"),
    (700, 500)
)
win.blit(back, (0, 0))
clock = pygame.time.Clock()

while True:
    win.update()
    clock.tick(60)