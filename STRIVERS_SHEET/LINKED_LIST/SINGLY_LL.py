"""
implementing SINGLY LINKED LIST
"""
class node:
    data:int
    next
    def __init__(self,data):
        self.data=data
        self.next=None
def traversal(head):
    curr=head
    while curr:
        print(curr.data,end="->")
        if curr.next==None:
            print("None")
            break
        curr=curr.next
    return
def insert_begin(head,x):
    n = node(x)
    if head==None:
        head=n
        return head
    n.next=head
    head=n
    return head
def insert_end(head,x):
    n=node(x)
    if head==None:
        head=n
        return head
    curr=head
    while curr:
        if curr.next==None:
            curr.next=n
            return head
        curr=curr.next

def insert_kth_position(head,x,position):
    n=node(x)
    if head==None:
        head=n
        return head
    if position==0:
        return insert_begin(head,x)
    k=0
    curr=head
    while curr:
        if k==position:
            n.next=curr.next
            curr.next=n
            return head
        k+=1
        curr=curr.next


n1=node(int(input()))
n2=node(int(input()))
n3=node(int(input()))
n1.next=n2
n2.next=n3
head=n1

head=insert_begin(head,input())
head=insert_end(head,input())
head=insert_kth_position(head,input("enter data"),int(input("enter position")))
traversal(head)