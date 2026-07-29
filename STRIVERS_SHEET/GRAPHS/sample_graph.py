"""

sample graph creating with my own knowledge
"""
from tarfile import data_filter


class node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
n2=node(4,None)
n1=node(8,n2)
print(n2.data,n1.next)
n3=node(3,None)
