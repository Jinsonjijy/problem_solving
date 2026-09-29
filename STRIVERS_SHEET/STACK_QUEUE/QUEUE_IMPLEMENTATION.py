"""
this is the implementation of the queue datastrcuture
"""
class Queue:

    def __init__(self,size):
        self.size=size
        self.queue=[0]*self.size
        self.start=-1
        self.end=-1
        self.curr_size=0
    def enqueu(self,x):
        if self.curr_size==self.size:
            print("Queue is full")
            return
        if self.end==-1:
            self.start=0
            self.end=0
        else:
            self.end=(self.end+1)%self.size
        self.queue[self.end]=x
        self.curr_size+=1
    def dequeue(self):
        if self.start==-1:
            print("The queue is Empty")
            return
        popped=self.queue[self.start]
        if self.curr_size==1:
            self.start=-1
            self.end=-1
        else:
            self.start=(self.start+1)%self.size
        self.curr_size+=-1
        return popped
    def itrating(self):
        if self.start==-1:
            print("The Queue is empty")
            return
        for val in range(self.end,self.start+1):
            print(self.queue[val])


if __name__=="__main__":
    q=Queue(10)
    q.enqueu(10)
    q.itrating()
    


