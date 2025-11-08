class parent:
    def sound(self):
        print("Hello i am father")
class child(parent):
    def sound(self):
        print("Hello i am child")
        super().sound()

c=child()
c.sound()        