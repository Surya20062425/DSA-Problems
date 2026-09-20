# In this program we are reverse the string that have given 

# example :
#   [1,3,4,6] -> [6,4,3,1]

class ListNode(object):

# we have created  a classs  ListNode 

  # it contains the values
    def __init__(self,val=0,next =None):
        self.val= val
        self.next=  next
class Solution(object):

    def reverseList(self,head):

      # created a linked list 
        prev =None

        curr =head 

      # we are staring from the first as curr  

      # And we are printig  reversed  list in prev

        while curr :
            temp =curr.next
            curr.next =prev

            prev = curr 
            curr =temp

        return prev #prev is the reversed list
