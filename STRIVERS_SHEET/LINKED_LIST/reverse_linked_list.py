class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def reverse_ll(l1):
    head=l1
    prev=None
    curr=head
    
    while curr:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node
        
    return prev
if __name__=="__main__":
    n=int(input("enter the number of nodes"))
    dummy=Node(-1)
    curr=dummy
    for i in range(n):
        node=Node(int(input("data:")))
        curr.next=node
        curr=curr.next
    head=reverse_ll(dummy.next)
    curr=head
    while curr:
        print(curr.data,end="->")
        curr=curr.next
    