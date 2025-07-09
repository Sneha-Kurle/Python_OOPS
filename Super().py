# Super()- A function used in child class by calling methods from parent or super class
#Allow you to extend the functionality of inherited methods
class shape():
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled
    def description(self):
        print(f'It is {self.color} and {'filled' if self.filled else 'Not filled'}')

class circle(shape):
    def __init__(self, color, filled, radius):
        self.radius=radius
        super().__init__(color,filled)

    def description(self):
        super().description()
        print(f'The area of the circle is {3.43*self.radius*self.radius:.2f} cm')
        
class sqare(shape):
    def __init__(self, color, filled, width):
        self.width=width
        super().__init__(color,filled)
    def description(self): #method oevrriding
        super().description()
        print(f'The area of the sqare is {self.width*self.width:.2f} cm^2')

class triangle(shape):
     def __init__(self, color, filled, width,height):
        self.height=height
        self.width=width
        super().__init__(color,filled)
     def description(self):
        super().description()
        print(f'The area of the traingle is {self.height*self.width/2:.2f} cm')

Circle=circle('red',True,5)
Sqare=sqare('blue', False, 6)
Triangle=triangle('Orange',True,3,8)
Sqare.description()
Triangle.description()
Circle.description()
print(Sqare.color)
print(Sqare.filled)
print(f'{Sqare.radius} cm')