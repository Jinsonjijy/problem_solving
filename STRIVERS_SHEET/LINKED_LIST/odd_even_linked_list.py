"""

110. Segregate odd and even nodes in Linked List
Given the head of a singly linked list. Group all the nodes with odd indices followed by all the nodes with even indices and return the reordered list.

Consider the 1st node to have index 1 and so on. The relative order of the elements inside the odd and even group must remain the same as the given input.

Example 1:
Input: linkedList = [1, 2, 3, 4, 5]

Output: [1, 3, 5, 2, 4]

Explanation:

The nodes with odd indices are 1, 3, 5 and the ones with even indices are 2, 4.

Example 2:
Input: linkedList = [4, 3, 2, 1]

Output: [4, 2, 3, 1]

Explanation:

The nodes with odd indices are 4, 2 and the ones with even indices are 3, 1
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def seggregate_odd_even(l1):
    head=l1
    even=head.next#even
    odd=head#odd
    even_head=even
    while even and even.next:
        odd.next=even.next
        odd=odd.next
        even.next=odd.next
        even=even.next

    odd.next=even_head
    return head
if __name__=="__main__":
    n1=Node(1)
    n2=Node(2)
    n3=Node(3)
    n4=Node(4)
    n5=Node(5)
    n1.next=n2
    n2.next=n3
    n3.next=n4
    n4.next=n5
    head=n1
    head=seggregate_odd_even(head)
    curr=head
    while curr:
        print(curr.data,end="->")
        curr=curr.next
