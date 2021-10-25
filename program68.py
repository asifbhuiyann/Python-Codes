class shape() :
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2
        print("I am busy.")

    def area(self):
        print("I am busy.")

class triangle(shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of the triangle is : ",area)

class rectangle(shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of the rectangle is :",area)

t1 = triangle(10,20)
t1.area()

t2 = rectangle(10,20)
t2.area()
