class Solution:
    def countSubstrings(self, s: str) -> int:

        if not s:
            return ""

        start, end = 0, 0

        def expand_around_center(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count

        c = 0
        for i in range(len(s)):
            o = expand_around_center(i, i)
            l = expand_around_center(i, i + 1)

            c = c + o + l

        return c
