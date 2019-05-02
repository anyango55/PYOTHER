class Circle:
    def __init__(self,radius):
        self.radius=radius
        
    
    def area(self):
        radius=self.radius
        A=(22/7*radius*radius)
        print(A)

    def circumference(self):
        radius=self.radius
        C=(22/7*radius)
        print(C)

class Square:
    def __init__(self,side):
        self.side=side

    def area(self):
            side=self.side
            A=(side*side)
            print(A)

    def perimeter(self):
            side=self.side
            P=(side+side+side+side)
            print (P)  

class Rectangle:
    def __init__(self,width,length):
            self.width=width
            self.length=length

    def area(self):
            width=self.width
            length=self.length
            A=(width*length)
            print(A)

    def perimeter(self):
            width=self.width
            length=self.length
            P=(2*(length*width))

class Sphere:
    def __init__(self,radius):
            self.radius=radius

    def surface_area(self):
            radius=self.radius
            A=(4(22/7*radius*radius))

    def volume(self):
            radius=self.radius
            V=(4/3(22/7*radius*radius*radius))







