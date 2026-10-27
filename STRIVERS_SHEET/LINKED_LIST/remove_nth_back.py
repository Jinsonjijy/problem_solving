"""
81. Remove Nth node from the back of the LL
Given the head of a singly linked list and an integer n. Remove the nth node from the back of the linked List and return the head of the modified list. The value of n will always be less than or equal to the number of nodes in the linked list.

Example 1:
Input: linkedList = 1 -> 2 -> 3 -> 4 -> 5, n = 2

Output: 1 -> 2 -> 3 -> 5

Explanation: The 2nd node from the back was the node with value 4.

Example 2:
Input: linkedList = 5 -> 4 -> 3 -> 2 -> 1, n = 5

Output: 4 -> 3 -> 2 -> 1

Explanation: The 5th node from the back is the first node.
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def remove_nth_node(l1,n):
    head=l1
    count=0
    curr=head
    while curr:
        count+=1
        curr=curr.next
    position=count-n
    if position == 0:
        return head.next

    curr=head
    c=0
    while curr:
        c += 1
        if position==c:
            curr.next=curr.next.next

        curr=curr.next
    return head





if __name__=="__main__":
    n=int(input("enter the number of nodes"))
    dummy=Node(-1)
    curr=dummy
    for i in range(n):
        d=int(input("data"))
        node=Node(d)
        curr.next=node
        curr=curr.next
    n=int(input("enter the position"))
    head = remove_nth_node(dummy.next,n)
    curr=head
    while curr:
        print(curr.data,end="->")
        curr=curr.next

