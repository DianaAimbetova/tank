from GameObject import objects, imageBangs, window, GameObject


class Smoke(GameObject):
    def __init__(self, x, y):
        objects.append(self)
        self.x = x
        self.y = y
        self.type = 'smoke'
        self.frame = 0

    def update(self):
        self.frame += 0.2
        if self.frame >= 3:
            objects.remove(self)

    def draw(self):
        image = imageBangs[int(self.frame)]
        rect = image.get_rect(center=(self.x, self.y))
        window.blit(image, rect)