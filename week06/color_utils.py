class Color:
    """ Handles RGB colors on a 0 ... 1 scale.

    """
    def __init__(self, r,g,b):
        self.r = max(min(1,r),0)
        self.g = max(min(1,g),0)
        self.b = max(min(1,b),0)
    
    def __(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)
    
    def __str__(self):
        return f"Color(r:{self.r}, g:{self.g}, b:{self.b})"

    def __sub__(self, other):
        return Color(self.r - other.r, self.g - other.g, self.b - other.b)
        

# red = Color(1,0,0)
# green = Color(0,1,0)
# blue = Color(0,0,1)

# print(red)

if __name__ == "__main__":
    import doctest
    doctest.testmod()