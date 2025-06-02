# My Understanding of 002 add two numbers

## What’s confusing: 
I think its the core mechanics and how it all comes together, especially when your extracting numbers from an operation and then reversing them into a list with an array of numbers that sit in a node thats apart of a linked list.

I found that in the solution the most confusing thing was these two operations and why they are needed:
carry = total // 10
digit % 10


## Analogy: 
**"Imagine a card game, where each card showing a digit. The cards are stacked in reverse order (the ones place is at the bottom, tens place above, hundreds place above that, etc. Your job is to add the numbers represented by the stcks and a new stack for the sum, also in reverse order. Remember: You can carry over an extra card when you add up the stack."**

## Key Insight: 
### Whats a linked list? 
Its like a chain of nodes, where each node has a digit (val) and a pointer to the node (next). 
For 2 -> 4 -> 3:  
Researching the use of linked lists; each card holds a digit and a pointer to the next car. The last card points to nothing (end of the pack of cards) 

### Viusualize the Addition
l1 = [1, 4, 3], l2 = [5, 6, 4]
Reverse order: 2 is the ones place, 4 is the tens place and 3 is the hundreds place (342
#### Addition: 
- Ones: 2 + 5 = 7
- Tens: 4 + 6 = 10 (write 0, carry 1 to the next digit)
- Hundreds: 3 + 4 + 1 (carry) = 8
- Result: 7 -> 0 -> (807 in reverse)
- 
Carry: When adding numbers (9 + 9 = 18) you write down 8 and carru 1 to the next digit.
As we move from adding the ones, tens and hundreds we use the "//" and  "%" to seperate them into what get carryed and what stays in the current nodes.

'''
current.next = ListNode(digit)
'''
Creates a new node with the value digit that I stored in the current node

'''
cuurent = current.next
'''
Moves the current pointer to the newly created node, so you can attach the next digit to it in the itertion.

'''
l1 = l1.next if l1 else None
l2 = l2.next if l2 else None
'''
Moves either the l1  or l2 pointer to the next node in the first linked list, or sets it to none if there are no more nodes

All together they add  new digit to the result list (current.next = ListNode(digit))
Move the result pointer to the new node (current = current.next)
Advance the input lists to their digits (l1 = l1.next if l1 else None
l2 = l2.next if l2 else None)













