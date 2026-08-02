# we are performing the task 
# where as we are checking the maximum sum of the twin elements 
# picking any set of  two- two  elements 

# forming the maximum sum from them 

# we are finally returning the maximum sum

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

      # created a linked-list

      
        half = []
        slow = fast = head

        while fast and fast.next:

          
            half.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        res = 0
        while slow:
            res = max(res, half.pop() + slow.val)


          # we are forming the maximum from above 
            slow = slow.next

      #  we have stored the max value in res
        return res 
