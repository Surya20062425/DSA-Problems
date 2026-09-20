from typing import List

class Solution:
    """Min cost climbing stairs — DP without mutating input."""

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = cost + [0]  # ponytail: copy to avoid mutating input
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])
