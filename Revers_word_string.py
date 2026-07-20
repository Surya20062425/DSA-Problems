class Solution:
    def reverseWords(self, s: str) -> str:
        # Split by any whitespace (handles multiple spaces) and filter out empty strings
        words = s.split()
        # Reverse the list and join with single space
        return ' '.join(reversed(words))
