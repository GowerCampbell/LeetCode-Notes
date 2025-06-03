"""
Plan the Algorithm
Start at the first node of both lists (l1 & l2)
Add the digits from ecah node (plus any carry from the previous step)
If the sum is 10 or more keep the ones digit (sum % 10) and the carry the tens digit (sum // 10)
Create a new node for the result digit
Move to the next nodes in both lists (if they exist)
Repeat until both lists are exhausted and theres no carry left

- Unequal list lengths (e.g. one list ends before the other)
- Carryover (e.g. 9 + 9 = 18)
- Creating a new linked list for the result
"""
class ListNode:
  def __init__(self, val=0, next=None:
    self.val = val
    self.next = next

def addTwoNumbers(l1, l2):
  """
  dummy; Create a dummy node to start the result list;
  pointer; Add a pointer to build out the result list;
  carry; Create a carryover to store the additions;
  """
  dummy = ListNode(0)
  pointer = dummy 
  carry = 0

  # Loop while there are digits in l1, l2, or a carry
  while l1 or l2 or carry:
    # Get digits from l1 and l2 (use 0 if list is exhausted)
    x = l1.val if l1 else 0
    y = l2.val if l2 else 0

    # Add digits and carry
    total = x + y + carry
    carry = total // 10 #Get carry for next digit 
    newNode = ListNode(total % 10) #Create newNode for added values

    #Create a pointer for the next variable
    pointer.next = newNode
    pointer = newNode

    # Move to next nodes, if they exist
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None

return dummy.next

"""
Conclusion:
Linked lists are chains, you proccess one node at a time, allowing the digits to be placed in reverse order 
you start with the least sigificant digit to the most, just like manual addition from the left. Handle carries 
like in school and the carry propagates to the next node. Using a dummy node avoids special cases for the head of
the result list. Unequal lengths like 9999 + 9 works because we assume 9 -> 0 -> 0 -> 0. Remember to iterate until done.
"""

  


