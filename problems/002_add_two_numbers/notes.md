# My Understanding of 002 add two numbers

## What’s confusing: 
I think its the core mechanics and how it all comes together, especially when your extracting numbers from an operation and then reversing them into a list with an array of numbers that sit in a node thats apart of a linked list.


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












