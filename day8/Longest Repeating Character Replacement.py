class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_count = 0
        count = [0] * 26
        start = 0

        for end in range(len(s)):
            count[ord(s[end]) - ord('A')] += 1
            max_count = max(max_count, count[ord(s[end]) - ord('A')])

            if end - start + 1 - max_count > k:
                count[ord(s[start]) - ord('A')] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)