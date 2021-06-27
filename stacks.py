#stack class 
class Stack:
    s=[]
    def pushItem(self,data):
        self.s.append(data)
        return print(self.s)

    def popItem(self):
        self.s.pop()
        return print(self.s)

#initial conditions to enter loop
n='y'
m='y'

#create stack1 object
stack1=Stack()

#loops to push and pop items from stack
while(n!='n'):
    n=input("Enter the number to be added to\nthe stack or enter n to exit.\n")
    if n!='n':stack1.pushItem(n)
       
while(m!='n'):
    m=input("Press y to remove the latest number from the stack or enter n to exit.\n")
    if m!='n':stack1.popItem()
    if (stack1.s==[]):
        print("Stack is empty")
        break
      

