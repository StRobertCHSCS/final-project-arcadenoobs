import arcade

class Obstacles:

    def __init__(self, x, y, r):
        obstancles = O_A.Obstacles(x, y, r)
        self.obstancles_list = []
        self.obstancles_list.append(obstancles)
    
    def draw(self):
        for obstancles in self.obstancles_list:
            obstancles.draw()


if __name__ == '__main__':
    print('Main runs as a main file')
else: 
    import Resource.Obstacles.Movement as O_A