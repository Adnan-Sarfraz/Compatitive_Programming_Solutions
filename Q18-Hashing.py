'''class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):
        print("This is Child class")
        super().show()   

c = Child()
c.show()'''

class person:
    def __init__(self, name ):
        self.name=name

class student(person):
    def __init__(self, name,roll):
        self.name=name 
        self.roll=roll
        super().__init__(name)
    
s=student("adnan", 20)
print(s.name)
print(s.roll)