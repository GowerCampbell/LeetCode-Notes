class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # If the string is empty, return 0
        if  not s:
            return 0
            
        # dictionary to store here each character viewed
        char_index = {}
        # keeo track of the longest set of characters in the string
        max_length = 0
        # left pointer starts at the beginning

        # Move the right pointer one step at a time
        for right in range(len(s)):
            # check if the current character is selected in the dictionary
            if s[right] in char_index and char _index[s[right]] >= left:
            # move left pointer to just after the last time we saw this character
            left = char_index[s[right]] + 1
         
         else:
             # No repeat! checks if this is the longest so far 
             max_length = max(max_length, right - left + 1)
             
        # Write downs the characters
         char_index[s[right]] = right
    return max_length




