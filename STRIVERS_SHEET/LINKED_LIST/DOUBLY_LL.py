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
    curr=head
    while curr:
        if curr.data==target:
            n=node(data)
            n.next=curr.next
            n.prev=curr

            if curr.next is not  None:
                curr.next.prev=n
            curr.next=n
            return head
        curr=curr.next
    print("target not found")
    return head
def insert_before(head,target,data):
    if head is None:
        print("insertion is possible")
        return head
    curr=head
    if head.data==target:
        return insert_begin(head,data)

    while curr.next:
        if curr.next.data==target:
            n=node(data)
            n.next=curr.next
            curr.next.prev=n
            n.prev=curr
            curr.next=n
            return head
        curr=curr.next
    print("target is not found")
    return head
def delete_begin(head):
    if head is None:
        print("deletion is not possible")
        return head
    head=head.next
    if head is not None:
        head.prev=None
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
