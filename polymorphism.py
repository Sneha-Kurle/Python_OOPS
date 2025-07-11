#polymorphism - Single method can act differently depending on the objects
#ABC`: Base class for creating abstract classes.
#abstractmethod`: Decorator to declare abstract methods, which must be implemented by subclasses.
#decorators adds extra featurs in exsisting method
#An abstract method is a method that is declared, but not implemented in the base class. Its implementation is left to the subclasses. 

from abc import ABC, abstractmethod
class shape(ABC): #abstract class
    @abstractmethod
    def area(self): #just define the abstract method. Implement it in sab class
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius= radius
 
class pizza(circle):
    def __init__(self,radius):
        super().__init__(radius)
        
Shape=circle(5)
Shape1=pizza(2)
print(f"Area of the circle: {Shape.area():.2f} cm^2 ")
print(f"Area of the pizza is : {Shape1.area():.2f} cm^2 ")


