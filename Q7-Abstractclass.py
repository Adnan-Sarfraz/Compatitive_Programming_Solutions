from abc import ABC,abstractmethod

class vehicle(ABC):#abstractclass
    @abstractmethod
    def start(self):
        pass

class Car(vehicle):#concrete class 
    def start(self):
        print("CAR STARTED")

class Bike(vehicle):
    def start(self):
        print("BIKE STARTED") 

car=Car()
bike=Bike()
car.start()
bike.start()  
#v=vehicle()    