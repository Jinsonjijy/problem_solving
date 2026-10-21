"""
93. Add two numbers in Linked List
Given two non-empty linked lists linkedList1 and linkedList2 which represent two non-negative integers.

The digits are stored in reverse order with each node storing one digit.

Add two numbers and return the sum as a linked list.

The sum Linked List will be in reverse order as well.
The Two given Linked Lists represent numbers without any leading zeros, except when the number is zero itself.
Example 1:
Input: linkedList1 = [5, 4], linkedList2 = [4]

Output: [9, 4]

Explanation: linkedList1 = 45, linkedList2 = 4.

linkedList1 + linkedList2 = 45 + 4 = 49.

The sum is 49 and when prepare the linked list we reverse the number [9, 4]

Example 2:
Input: linkedList1 = [4, 5, 6], linkedList2 = [1, 2, 3]

Output: [5, 7, 9]

Explanation: linkedList1 = 654, linkedList2 = 321.

linkedList1 + linkedList2 = 654 + 321 = 975.

The sum is 975 and when prepare the linked list we reverse the number [5, 7, 9]The sum
"""



class nodes:
    def __init__(self,data):
        self.data=data
        self.next=None

def sum_two_numbers(l1,l2):
    curr=l1
    num1=""
    while curr:
        num1+=str(curr.data)
        curr=curr.next
    num1=num1[::-1]
    curr=l2
    num2=""
    while curr:
        num2+=str(curr.data)
        curr=curr.next

    num2=num2[::-1]
    num2=int(num2)+int(num1)
    temp=num2# just for storing
    dummy=nodes(0)
    curr=dummy
    while num2:
        n1=num2%10
        n=nodes(n1)
        curr.next=n
        curr=n
        num2=num2//10
    head=dummy
    return head
if __name__=="__main__":
    n1=nodes(5)
    n2=nodes(4)
    n1.next=n2
    head1=n1
    n3=nodes(7)
    n4=nodes(9)
    n3.next=n4
    head2=n3
    head=sum_two_numbers(head1,head2)
    curr=head
    while curr:
        print(curr.data,end="")
        curr=curr.next


