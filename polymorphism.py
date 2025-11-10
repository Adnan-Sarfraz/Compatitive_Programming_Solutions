#polymorphism means many forms
class hen:
    def fly(self):
        print("Hen cant fly properly")

class bird:
    def fly(self):
        print("Bird can fly properly")

b=bird()
h=hen()
b.fly()
h.fly()
