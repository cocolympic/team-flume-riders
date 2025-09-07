class Example:
    def __init__(self):
        self.x = 10

obj = Example()

delattr(obj, 'x')
