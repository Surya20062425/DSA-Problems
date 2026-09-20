class Solution:

    # The vowels are a , e,i , o,u 

    # we have to perform the pointer operation
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)  # Strings are immutable in Python, so convert to list
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer until we find a vowel
            while left < right and s[left] not in vowels:
                left += 1
            
            # Move right pointer until we find a vowel
            while left < right and s[right] not in vowels:
                right -= 1
            
            # Swap the vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return ''.join(s)
