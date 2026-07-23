class solution :
  # created a class to pass the leetcode compiler 

  def issubsequence(self, s : str, t :str) -> bool :

    # created two strings s , t
    if len(s) == 0 :
      # Evaluating the condition 

      # lenght of s to zeo

      # if it satisfied we are returnig true 
      return True 
s_pointer =0
# created two pointers 

# And initialized to zero 
t_pointer =0
  while t_pointer < len(t) :

    # iterating the loop 

    # we are taken to while loop because we dont know how many times to iterate

    if t[t_pointer ] == s[s_pointer] :

      # checking the conditon  the two string consists of sny same element 

      
      s_pointer +=1

      # if foud increase the poinbter
      # to Check the next element 
      if  s_pointer =len(s) :

      # if the s_pointer and the lenght s are equal 

      # we are going to return the True 
      return true 

t_pointer +=1

# moving to next element 

return False 
