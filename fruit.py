from block import Block
from random import choice
from image_manager import ImageManager


class Fruit(Block):
    def __init__(self, x, y, width, height):
        images = ['superfruit.png', 'Cherry-1.png', 'peach.png', 'strawberry.png']
        fruit_image, _ = ImageManager(img=choice(images), resize=(width // 2, height // 2)).get_image()
        super(Fruit, self).__init__(x, y, width, height, fruit_image)
