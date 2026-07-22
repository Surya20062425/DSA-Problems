class Solution:

  # created the class solutionn 

  # the class is created to satisfie the leetcode compiler 
    def moveZeroes(self, nums: List[int]) -> None:

      # created a function movezeros
      # nums: List[int]  is to be used to create an array  nums 
      # the array consists of integer
        snowBallSize = 0

      # snowBallSize is the varialbe 
      # the initial value assigned is 0
      
        for i in range(0, len(nums)):
             # the loop that iterates from 0 to lenght of nums 
            if nums[i] == 0:

              # The condition 
              # if the element in the nums equal to 0

              # Then the condition to be evaluated 
                snowBallSize += 1

          # if the condition satidfied 

          # then the  snowBallSize  the value increased by 1
            elif snowBallSize > 0:

              # The second condition 

              # if  snowBallSize  is greater than 0 
                t = nums[i]

              # t value assigned to the elmnent in nums
              
                nums[i] = 0

              # the element i is to be reseted 

              # for the further iteration 
                nums[i - snowBallSize] = t

                 # the final array is to be modified 

                  # we returned the final array 

                 # the aray is consists of the zeros at the end 


      # returned the final array
