class Solution:


  # we are Defined an class called Solution
    def productExceptSelf(self, nums: List[int]) -> List[int]:

      # created a array called nums  
        n = len(nums)
      # The element n holds the lenght of the array num
        leftProducts = [1] * n
        rightProducts = [1] * n
        result = [0] * n
        
        # Calculate products of all elements to the left
        for i in range(1, n):
            leftProducts[i] = leftProducts[i - 1] * nums[i - 1]
        
        # Calculate products of all elements to the right
        for i in range(n - 2, -1, -1):
            rightProducts[i] = rightProducts[i + 1] * nums[i + 1]
        
        # Multiply left and right products
        for i in range(n):
            result[i] = leftProducts[i] * rightProducts[i]
        
        return result
