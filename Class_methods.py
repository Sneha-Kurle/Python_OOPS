#class_methods- Operations related to class
#take cls as paremetre
class Student:
    count=0
    def __init__(self, name, gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1
    def get_info(self):
        pass
    @classmethod
    def get_count(cls):
        return f'The count of the object is :{cls.count}'
student1= Student('Sneha',5)
student2=Student('AISHU',6)
student2=Student('Ayii',7)
print(Student.get_count())
        