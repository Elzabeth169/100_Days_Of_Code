# User function Template for python3


class Solution:

    # Function to find the smallest window in the string s consisting
    # of all the characters of string p.
    def smallestWindow(self, S, P):
        # code here
        from collections import Counter

        if len(P) > len(S):
            return "-1"

        required = Counter(P)
        window_counts = {}

        l, r = 0, 0
        formed = 0
        required_len = len(required)

        min_len = float('inf')
        min_window = (-1, -1)

        while r < len(S):
            char = S[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in required and window_counts[char] == required[char]:
                formed += 1

            while l <= r and formed == required_len:
                char = S[l]

                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = (l, r)

                window_counts[char] -= 1
                if char in required and window_counts[char] < required[char]:
                    formed -= 1

                l += 1

            r += 1

        if min_window == (-1, -1):
            return "-1"

        start, end = min_window
        return S[start:end + 1]