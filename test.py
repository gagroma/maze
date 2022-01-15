import pygame as pg
pg.init()

class OurSprites(pg.sprite.Sprite):
    def __init__(self, x, y, image, speed):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(image), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


window = pg.display.set_mode((700, 500))
#win.fill((123, 76, 31))
back = pg.transform.scale(pg.image.load("background.png"),(700, 500))
window.blit(back, (0, 0))

clock = pg.time.Clock()
pg.mixer.music.load("Потап и Настя - Чумачечая Весна.mp3")
pg.mixer.music.play()

cat = OurSprites(200, 200, "mishka.png",10)
game = True
FPS = 60

while game:
    window.blit(back, (0, 0))
    cat.reset()

    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False
            
    pg.display.update()
    clock.tick(60)