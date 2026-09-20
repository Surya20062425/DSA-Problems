class solution :

  # created  a class solution to pass leetcode compiler 
  def issubsequence(self,s:str,t:str) -> bool :
    for c in s :
      # Iterating the loop to find the elements in s 
      
      i = t.find(c) 
         if i == -1 :

           # if found ar -1 
           # Return false 
           return False 

         else :
            t =t[i+1:]
           # Else found the same elements in both s /t 
    return True
 # return true 
  # when the elments in the both strings are same 

# it return true if it was partially \\ totally matched
