class Solution:
    def numTilings(self, n: int) -> int:
        dp = [[0] * 3 for _ in range(3)]
        dp[0][0] = 1
        dp[1][0] = 1
        MOD = 1_000_000_007

        for i in range(2, n + 1):
            curr = i % 3
            prev1 = (i - 1) % 3
            prev2 = (i - 2) % 3
            dp[curr][0] = (
                dp[prev1][0] + dp[prev2][0] + dp[prev1][1] + dp[prev1][2]
            ) % MOD
            dp[curr][1] = (dp[prev1][2] + dp[prev2][0]) % MOD
            dp[curr][2] = (dp[prev1][1] + dp[prev2][0]) % MOD
        return dp[n % 3][0]
