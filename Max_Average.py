class Solution:

  # Defined a class solution
    def findMaxAverage(self, nums: List[int], k: int) -> float:

      # created a array nums containing integers

      # created a variable k - lenght  sub-array 

      # used float at the end 
      # because the average could be float value 
        our_sum= sum(nums[:k])

      #  variable or_sum

      # It stored the sum of elements in the array

      # by usiing sum method to the array nums
        max_sum = our_sum

      # created a variable max_sum

      # equated the sum of elements to the max_sum
        for  i in range(k,len(nums)):

          # used a for loop
          # it iterates from sub-array lenght value to the leght value of array nums 
            our_sum= our_sum-nums[i-k]+nums[i]
          # calculating the max value 
          # the elemnt i is substracted by lenght of sub array 

          # after added the elemnt i 
            max_sum = max(max_sum, our_sum)

      # checking the max value 
      # among the variable max_sum , our_sum

      


        return max_sum/k  # avg = sum of all elemnts / number of elements 
         # returned the average
