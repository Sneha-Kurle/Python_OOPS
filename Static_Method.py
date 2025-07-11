#Static method= A method belong to class rather than instace or object method  
#self parametre not required
#used as a common utility function
#To use any common function is class we must use decorator @staticmethod

class Employee:
    def __init__(self, name , role):
        self.name=name
        self.role=role
    
    def info(self):
        return f'{self.name}={self.role}'
    @staticmethod
    def get_role(role):
        roles=['devops','admin','sales','tester']
        return role in get_role
employee=Employee('sneha','admin')
employee2=Employee('aishu','devop')
print(Employee.get_role('devop'))