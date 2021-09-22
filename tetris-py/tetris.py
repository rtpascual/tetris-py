import shapes

class Tetris:
    level = 1
    x, y = 100, 60
    zoom = 20
    shape = None

    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width
        self.state = "start"
        self.score = 0
        self.field = []

        for i in range(height):
            line = []
            for j in range(width):
                line.append(0)
            
            self.field.append(line)
    
    def new_shape(self):
        self.shape = shapes.Shapes(3,0)
    
    def intersects(self) -> bool:
        intersection = False

        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.shape.image():
                    if (i + self.shape.y > self.height - 1 or
                        j + self.shape.x > self.width - 1 or
                        j + self.shape.x < 0 or
                        self.field[i + self.shape.y][j + self.shape.x] > 0):
                        intersection = True

        return intersection
    
    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.shape.image():
                    self.field[i + self.shape.y][j + self.shape.x] = self.shape.color
        
        self.break_lines()
        self.new_shape()
        if self.intersects():
            self.state = "gameover"
    
    def break_lines(self):
        lines = 0

        for i in range(1, self.height):
            zeros = 0

            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1

            if zeros == 0:
                lines += 1

                for ii in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[ii][j] = self.field[ii - 1][j]
        
        self.score += lines ** 2
    
    def go_space(self):
        while not self.intersects():
            self.shape.y += 1

        self.shape.y -= 1
        self.freeze()

    def go_down(self):
        self.shape.y += 1

        if self.intersects():
            self.shape.y -= 1
            self.freeze()
    
    def go_side(self,dx):
        x = self.shape.x
        self.shape.x += dx

        if self.intersects():
            self.shape.x = x
    
    def rotate(self):
        rotation = self.shape.rotation
        self.shape.rotate()

        if self.intersects():
            self.shape.rotation = rotation