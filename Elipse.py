class Elipse:
    def __init__(self, x, y, a, b, alpha):
        self._x = x
        self._y = y
        self._a = a
        self._b = b
        self._alpha = alpha

    #set functions
    def set_x(self, x):
        self._x = x
    def set_y(self, y):
        self._y = y
    def set_alpha(self, alpha):
        self._alpha = alpha
    #get functions
    def get_x(self):
        return self._x 
    def get_y(self):
        return self._y 
    def get_a(self):
        return self._a
    def get_b(self):
        return self._b
    def get_alpha(self):
        return self._alpha 