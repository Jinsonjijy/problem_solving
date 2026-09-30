"""
implementing SINGLY LINKED LIST
referring resource:"https://takeuforward.org/blogs/data-structure-and-algorithm/singly-linked-list"




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
        if k+1==position:
            n.next=curr.next
            curr.next=n
            return head
        k+=1
        curr=curr.next

def delete_begin(head):
    if head == None:
        print("No data")
        return head
    curr=head
    head=curr.next
    curr.next=None
    return head
def delete_end(head):
    if head == None:
        print("No data ")
        return head
    if head.next == None:
        return None
    curr=head
    while curr:
        if curr.next.next == None:
            curr.next=None
            return head
        curr=curr.next
def delete_k_position(head,position):
    if position==0:
        return delete_begin(head)
    k=0
    curr=head
    while curr:
        if k+1 == position:
            curr.next=curr.next.next
            return head
        
        curr=curr.next

head=None
while True:
    print(f"1 for traversal \n 2 for insertion at begin \n 3 for insertion at end \n 4 for insertion at k \n 5 for delete at begin\n 6 for deletion at end")
    
    choice=input("enter choice")
    if choice=="1":
        traversal(head)
    elif choice=="2":
        head=insert_begin(head,input())
    elif choice=="3":
        head=insert_end(head,input())
    elif choice=="4":
        head=insert_kth_position(head,input("data:"),int(input("position:")))
    elif choice=="5":
        head=delete_begin(head)
    elif choice == "6":
        head=delete_end(head)
    else:
        break