"""
    in this we mainly implementing the stack


"""
class stack_array:
    def __init__(self,size=1000):
        self.stack=[0]*size
        self.capacity=size
        self.top=-1
    def push (self,x):
        if self.top>=self.capacity:
            print("The stack is overflow")
            return
        self.top+=1
        self.stack[self.top]=x
    def pop(self):
        if self.top==-1:
            print("No elements to pop")
            return
        top_element=self.stack[self.top]
        self.top-=1
        return top_element
    def top_element(self):
        if self.isEmpty():
            print("stack is empty")
            return -1
        return self.stack[self.top]
    def isEmpty(self):
        return self.top==-1
if __name__=="__main__":
    stack=stack_array(10)
    stack.push