class Solution:

  # DEfined the class to pass the leetcode compiler
    def maxArea(self, height: List[int]) -> int:


      # created an array height it stores integer

      # we have used  -> to ensure the output is integer
        left = 0 # We are creating two sides 
      # one is left and another one is right

      # And initialized the values to zero  --> left
        right = len(height) - 1

      # The right side is to be less than the lenght array -->  height
        maxArea = 0
         # created a variable to store the area

      # created a variable max_area and initialized it to zero 
        while left < right:

          # the loop iterates when left < right 
            currentArea = min(height[left], height[right]) * (right - left)

          # The currentArea ie calculated the minimum

          # from heigth -> left and height --> right * (right-left)
          
            maxArea = max(maxArea, currentArea)

          # we are selecting the max area among maxarea // currentarea

            if height[left] < height[right]:
              # if the left < right 
              # we are going to increment the value of left by 1
                left += 1
            else:

              # else we are going to decrement the value of right by 1
                right -= 1

        return maxArea

  # Returning the maximum area
