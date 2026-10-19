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
    head.prev=n
    head=n
    return head
def insert_end(head,data):
    if head==None:
        head=node(data)
        return head
    curr=head
    n=node(data)

    while curr.next:
        curr=curr.next
    curr.next=n
    n.prev=curr
    return head
def insert_after(head,target,data):
    if head is None:
        print("insertion is not possible")
        return head
    n=node(data=data)  
    curr=head
    while curr:
        if curr.data==target:
            break
        if curr.next==None:
            break
        curr=curr.next
    n.next=curr.next
    curr.next.prev=n
    n.prev=curr
    curr.next=n
    return head



        

def traversal(head):
    curr=head
    while curr:
        print(curr.data,end="<->")
        curr=curr.next
    print(None)
    return 
if __name__== "__main__":
    head=None
    while True:
        print("\n 1 for insert at begin\n2 for inset at end\n3 for insert after position")
        choice=int(input("enter the choice:"))
        if choice==1:
            data=int(input("data:"))
            head=insert_begin(head,data)
        elif choice==2:
            data=int(input("data:"))
            head=insert_end(head,data)
        elif choice==3:
            target=int(input("target"))
            head=insert_after(head,int(input()),target)
        elif choice == 7:
            traversal(head)

        else:
            break
