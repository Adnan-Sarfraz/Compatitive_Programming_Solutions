class car:
    def __init__(self, BrandName, ModelYear, speed):
        self.BrandName=BrandName
        self.ModelYear=ModelYear
        self.speed=speed
    
    def brandname(self):
        print(f"The name is--> {self.BrandName} ")
    
    def modelyear(self):
        print(f"The model year is --> {self.ModelYear} ")

    def Speed(self):
        print(f"The speed is --> {self.speed}")

car1=car("toyota", "2019", 290)      
car2=car("Honda", "1999", 225) 
car3=car("Suzuki", "2010", 220)   
car4=car("KIA", "2007", 205) 
print("-----------------------------------\n")
car1.brandname()
car1.modelyear()
car1.Speed()

print("-----------------------------------\n")
car2.brandname()
car2.modelyear()
car2.Speed()

print("-----------------------------------\n")
car3.brandname()
car3.modelyear()
car3.Speed()

print("-----------------------------------\n")
car4.brandname()
car4.modelyear()
car4.Speed()