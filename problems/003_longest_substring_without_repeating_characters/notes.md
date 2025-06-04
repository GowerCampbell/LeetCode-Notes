## My Understanding
- **What’s confusing**:
  My mind always goes a little blank looking at this as it can't organise how to solve it without researching ways to implement this. I hope in time as I do more this comes easier but its worrying, the assumption is counting how many characters are repeated in the string. I remember this is a great way to put into practice organising any inputted data from reading files, I think what confused me is my understanding of the problem. Because we are looking for a substring where all the characters are unique and therefore- have no repeats, without duplicate characters. Finding the longest part of it without repeats.
- **Analogy**:
  Imagine a window over the string, the window is the part of the string we're looking and we want to make it as big as possibe without having any repeating characters. If we find a repeat, we shrink the window until the repeat is gone, then keep growing it again.
- **Key Insight**:
  
Out of a continuous piece of string data, we need to return the longest valid substring.
Example 3: "pwwkew"
"pw" has no repeats → length 2.
"pww" has a repeat ("w") → not valid.
"wke" has no repeats → length 3.
Final answer: 3 (not 4, because "pwke" skips characters, which isn’t a substring).
By using away to track the characters and where they are positioned



