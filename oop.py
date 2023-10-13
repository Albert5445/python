class Vector:
    min_coord = 0
    max_coord = 100

    @classmethod
    def validate(cls, arg):
        return cls.min_coord <= arg <= cls.max_coord

    @staticmethod
    def norm2(x, y):
        return x*x + y*y
