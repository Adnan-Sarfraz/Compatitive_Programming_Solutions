#single inharitance
class parent:
    def greet(self):
        print("i am the parent")
class child(parent):
    def greet(self): 
        print("i am the child")

'''c=child()
c.greet()
p=parent()
p.greet()'''

#multiple inharitance
class father:
    def greet(self):
        print("HELLO I AM FATHER ")
class mother:
    def greet(self):
        print("HELLO I AM MOTHER")
class child(father, mother):
    def greet(self):
        print("HELLO I AM A CHILD")


#multilevel inharitance
class A:
    def greet(self):
        print("HELLO WORLD FROM A")
class B(A):
    def greet(self):
        print("HELLO WORLD FROM B")
class C(B):
    def greet(self):
        print("HELLO WORLD FROM C")


#hiracical inharitance
class parent:
    def greet(self):
        print("HELLO I AM FATHER ")
class child1(parent):
    def greet(self):
        print("HELLO FROM CHILD 1")
class child2(parent):
    def greet(self):
        print("HELLO FROM CHILD 2")

#diamond problem
class GrandParent:
    def info(self):
        print("I am GrandParent")

class Parent1(GrandParent):
    def info(self):
        print("I am Parent1")

class Parent2(GrandParent):
    def info(self):
        print("I am Parent2")

class Child(Parent1, Parent2):
    pass

c = Child()
c.info()  # I am Parent1  <- Python uses first parent in MRO
