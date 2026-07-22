class Solution:

  # created a class thst to pass the leetcode compiler
  def compress(self, chars: List[str]) -> int:
    # created a function to  solve the problem   
       # The Chars : List[str]  it defines a array with the characters 

    # SElf term is used to pass the leetcode compiler 
    # and used int to return the leght as integer
    
    ans = 0

    # created a variable ans and assigned the value as 0
    i = 0
    # we also created another variable i to use in iterating the loop
    while i < len(chars):


      # The loop iterates the i value becomes greater than the lenght of the array 
      letter = chars[i]

      # THe variabel letter that stores the each element indivisually 
      count = 0

      # The count variable used furthere in evaluating the condition
      while i < len(chars) and chars[i] == letter:

        #  WE have created a anothere while loop 

        # The loop iterates when it satisfy the both conditions due to the use of the term and condition involved in looping 
        count += 1

        # if the i satisfies both the conditions it increases the count to 1
        i += 1
          # if the i satisfies both the conditions it increases the i value  to 1
      chars[ans] = letter
      ans += 1
      if count > 1:
        for c in str(count):
          chars[ans] = c
          ans += 1

    return ans
