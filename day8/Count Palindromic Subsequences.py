class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def countPS(self, string):
        N = len(string)
        MOD = 10 ** 9 + 7

        dp = [[0] * N for _ in range(N)]

        for i in range(N):
            dp[i][i] = 1

        for length in range(2, N + 1):
            for i in range(N - length + 1):
                j = i + length - 1
                if string[i] == string[j]:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] + 1) % MOD
                else:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
        return dp[0][N - 1]