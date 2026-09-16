class stack_array:
    def __init__(self,size=1000):
        self.stack=[0]*size
        self.capacity=size
        self.top=-1