import pygame as py
from random import randint
class My(py.sprite.Sprite):
    def update(self, *args, **kwargs):
        self.rect = self.rect.move(randint(-5, 5), randint(-5, 5))