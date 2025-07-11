#method overloading
class calc:
    def add(self,a,b=None):
        self.a=a
        self.b=b
        if b is not None:
            return a+b
        return a
cal=calc()
print(cal.add(3))

#Operator overloading- Single operator can take many form
print(2+5)
print('Hi'+' Sneha')
print([1,2]+[3,4])

#method overriding-
class animal():
    def sound(self):
        print('Animal sound')
    
class dog(animal):
    def sound(self):
        print('Bark..bow bow')
        super().sound()
Dog=dog()
Dog.sound()

#duck typing