from typing import List

class Solution:
    """Longest subarray of 1s after deleting one element (sliding window)."""

    def longestOnes(self, nums: List[int], k: int) -> int:
        left = zeroCount = maxLength = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength
