class lastEvent():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_int_x(self):
        if self.x != None:
            return int(self.x)

    def get_int_y(self):
        if self.y != None:
            return int(self.y)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y