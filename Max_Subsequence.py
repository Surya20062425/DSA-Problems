class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res, prefixSum, minHeap = 0, 0, []

      # we are using the min heap properties

        for a, b in sorted(list(zip(nums1, nums2)), key=itemgetter(1), reverse=True):
            prefixSum += a  # incrementing the prefix by a
            heappush(minHeap, a)
          
            if len(minHeap) == k:
                res = max(res, prefixSum * b)

              # finding the maximum 
                prefixSum -= heappop(minHeap)                           
        return res
