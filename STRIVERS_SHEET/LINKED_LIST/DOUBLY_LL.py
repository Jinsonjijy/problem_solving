"""
implementing doubly linked list in which it has two pointer 1 data part
    1.prev ptr
    2.next ptr
    3. data part
application:
            *mainly used in musice players
            *undo/redo operation 
"""
class node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
def insert_begin(head,data):
    if head is None:
        head=node(data)
        return head
    n=node(data)
    n.next=head
    head=n
    return head
def traveral(head):
    curr=head
    while curr:
        print(curr.data,end="->")
        curr=curr.next
    return 
if __name__== "__main__":
    head=node(10)
    head.next=node(20)
    head.next.prev=head
    head.next.next=node(30)
    head.next.next.prev=head.next
    head=insert_begin(head,int(input()))
    traveral(head)