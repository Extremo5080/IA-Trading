class ChartCropper:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def crop(self, image):
        return image[
            self.y:self.y + self.height,
            self.x:self.x + self.width
        ]
