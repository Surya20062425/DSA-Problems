class Solution:
    def reverseWords(self, s: str) -> str:
        # Split by any whitespace (handles multiple spaces) and filter out empty strings
        words = s.split()
        #s.split() is used to split the string s 

        
        # Reverse the list and join with single space
        return ' '.join(reversed(words))
         # join() function combines elements stored in the word without the spaces
