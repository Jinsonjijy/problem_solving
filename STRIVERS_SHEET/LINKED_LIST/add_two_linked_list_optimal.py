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
from add_two_num_sll import nodes
def add_linkedlist(l1,l2):
    dummy=nodes(0)
    curr=dummy

    curr1=l1
    curr2=l2
    carry=0
    while curr1 or curr2 or carry:
        # finding values  of each linked list
        x = curr1.data if curr1 else 0
        y = curr2.data if curr2 else 0
        #making digit and carry
        sum=x + y +carry
        digit= sum % 10
        carry = sum //10
        # create  a new node with digit data then append it with next
        curr.next=nodes(digit)# so this is how the linked list is made
        curr=curr.next
        if curr1:
            curr1=curr1.next
        if curr2:
            curr2=curr2.next
    return dummy.next

