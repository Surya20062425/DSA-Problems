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

      # the elment in array that satisifie the lenfght of the array 

      # then it equals to the letter that hold the value of lenght 

    # it is the required element we need to evaluate
      ans += 1

      # then we increase the value of the ans by 1

      if count > 1:
        # the above condition evaluates
        # the condition evaluates when the count is greater than 1
        for c in str(count):
          # the loop that iterrates according to the c is an value 
          # c value is useed to iterate the loop 

          #  the count is the integer

          # the integer is to be turned into the string 

          # the transformed string is to be added into the array 
          chars[ans] = c

          # In the array of cahrs 

          # if the element that satisfies the value of lenght of the array 

          # the element that is to be assigned to the value c
          
          ans += 1

         # the value of the leght -- ans to be increased by 1

    return ans

# the value to be returned  is the lenght of the new array
