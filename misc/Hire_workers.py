import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total_cost = 0
        left_min_heap = []
        right_min_heap = []
        l, r = 0, len(costs) - 1

        while l <= r and len(left_min_heap) < candidates:
            heapq.heappush(left_min_heap, costs[l])
            if l < r:
                heapq.heappush(right_min_heap, costs[r])
            l += 1
            r -= 1

        while k > 0:
            if not right_min_heap or (left_min_heap and left_min_heap[0] <= right_min_heap[0]):
                total_cost += heapq.heappop(left_min_heap)
                if l <= r:
                    heapq.heappush(left_min_heap, costs[l])
                    l += 1
            else:
                total_cost += heapq.heappop(right_min_heap)
                if l <= r:
                    heapq.heappush(right_min_heap, costs[r])
                    r -= 1
            k -= 1
            
        return total_cost
