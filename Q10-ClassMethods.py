class Employee:
    company="Google"
    def __init__(self,name):
        self.name=name
    
    @classmethod
    def change_company(cls, new_company):
        cls.company=new_company

e1=Employee("Adnan")
e2=Employee("Mamoon")

print(e1.company)
print(e2.company)
print("---------------------------------------\n")
Employee.change_company("Microsoft")
print("\n")
print(e1.company)
print(e2.company)