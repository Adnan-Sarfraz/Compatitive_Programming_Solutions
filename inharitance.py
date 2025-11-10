class animal:
    def run(self):
        print("There are some animals which can run")

class tiger(animal):
    def roar(self):
        print("Tiigher can roar ")

a=animal()
t=tiger()
a.run()
t.roar()
t.run()