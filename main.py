import pygame as py
import random
from spriteeee import My
py.init()
w = py.display.set_mode((600, 600))
img = py.image.load("player.png")
img = py.transform.scale(img, (50, 50))

all_sprites = py.sprite.Group()
for i in range(1000):
    sprite = My(all_sprites)
    sprite.image = img
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = random.randint(1, 650)
    sprite.rect.y = random.randint(1, 650)
    #all_sprites.add(sprite)
while True:
    w.fill((255, 255, 255))
    all_sprites.update(w)
    w.blit(img, (30, 30))
    py.display.update()
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()

