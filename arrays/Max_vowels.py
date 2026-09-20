class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        # created a set for storing the vowels
     
        current_vowels = 0

      # created a vowel 
        for i in range(k):# we using this loop for checking the elments in string s 
            if s[i] in vowels: # checks the string woth the set vowels 
                current_vowels += 1
                # increasing the coutn 

      # when we found the elment in s 
        max_vowels = current_vowels
      # assigned coutn to max_vowel
        
        
        for right in range(k, len(s)):
            left = right - k  # Calculate left index dynamically
            # comming from left 
            if s[left] in vowels:
                current_vowels -= 1
       # comming from right 
            if s[right] in vowels:
                current_vowels += 1
                
            # Update max vowels found so far
            max_vowels = max(max_vowels, current_vowels)
            
            # Optimization: If max_vowels reaches k, we can't do better!
            if max_vowels == k:
                return k
                
        return max_vowels
