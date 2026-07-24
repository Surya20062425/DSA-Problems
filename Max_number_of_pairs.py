class solution :
  # created a class for leetcode compilation 

  def (self , nums :list(), k:int) -> int :
  # we have created a array nums 
  # Created a variabe k - integer
  nums.sort()
  # we have sorted nums array using sort() method 
   i, j=0,len(nums)-1
    count=0
# created a variable count and initialized it to  0
    while i< j:

      # The loop runs under the condition i<j
      total = nums[i]+nums[j]
      # Total = element at index i+ element at index j
      if total == k:

        # if total becomes k 
        # we are increment the count value by 1
        count +=1
        i +=1
        # incremented due to move to next element
        j -=1
        # the i and j are in oposite direction
           # so i comes from  starting and j from ending 
      elif total>k:
        j-=1
        # moving to next element
      else:
        i+=1
        # moving to next element 

return count # returning the number of pairs 
  

  


