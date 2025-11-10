#Encapsulation means hiding data and show only what is essentional to the user
class student:
    def __init__(self, name, marks):
        self.name=name
        self.__marks=marks

    def get_marks(self):
        return self.__marks
    
    def set_marks(self,marks):
        if marks>0:
            self.__marks=marks
        else:
            print("Marks cannot be negative")

s=student("adnan", 60)
print(s.get_marks())
print(s.name)
s.set_marks(70)
print(s.get_marks())

    
