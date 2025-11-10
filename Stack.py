class Stack:
    def __init__(self):
        self.list_=[]
        self.top=-1
       
    def push(self,item):
        self.top+=1
        self.list_.append(item)
        print(f"Item is pushed {self.list_}")
    
    def pop(self):
        if self.top==-1:
            print("Empty Stack")
        else:
            print("item poped", self.list_[self.top])
            self.top-=1
    
    def peek(self):
        if self.top==-1:
            print("Empty Stack")
        else:
            print("Item peaked ", self.list_[self.top])

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
stack.pop()
stack.peek()

# #---------------------------------------------LIFO--------------------------------------------
