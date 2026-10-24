"""
778. Sort a Linked List of 0's 1's and 2's
Given the head of a singly linked list consisting of only 0, 1 or 2.

Sort the given linked list and return the head of the modified list.

Do it in-place by changing the links between the nodes without creating new nodes.

Example 1:
Input: linkedList = [1, 0, 2, 0 , 1]

Output: [0, 0, 1, 1, 2]

Explanation: The values after sorting are [0, 0, 1, 1, 2].

Example 2:
Input: linkedList = [1, 1, 1, 0]

Output: [0, 1, 1, 1]

Explanation: The values after sorting are [0, 1, 1, 1].
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def seggregate(l1):
    head=l1
    dummy_zero=Node(-1)
    dummy_one=Node(-1)
    dummy_two=Node(-1)
    zero=dummy_zero
    one=dummy_one
    two=dummy_two
    curr=head
    while curr:
        if curr.data==0:
            zero.next=curr
            zero=zero.next
        elif curr.data==1:
            one.next=curr
            one=one.next
        elif curr.data==2:
            two.next=curr
            two=two.next
        curr=curr.next
    two.next=None
    zero.next=dummy_one.next if dummy_one.next else dummy_zero.next
    one.next=dummy_two.next
    head=dummy_zero.next
    return head
if __name__=="__main__":
    n=int(input())
    new_node=Node(0)
    head=new_node
    curr=head
    for i in range(n):
        new_one=Node(int(input()))
        curr.next=new_one
        curr=curr.next
    head=seggregate(head.next)
    curr=head
    while curr:
        print(curr.data,end="->")
        curr=curr.next
    print(None)


