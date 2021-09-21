import random

class Shapes:
    shapes = [
        [],
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1,5,6,10],[6,7,9,10]],
        [[2,5,6,9],[4,5,9,10]],
        [[1, 2, 5, 6]],
    ]

    colors = [
        (),
        (77, 200, 233),
        (3, 65, 174),
        (255, 151, 28),
        (128,0,128),
        (114, 203, 59),
        (255, 50, 19),
        (255, 213, 0),
    ]

    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.type = random.randint(1,len(self.shapes) - 1)
        self.color = self.type
        self.rotation = 0

    def image(self):
        return self.shapes[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.shapes[self.type])
