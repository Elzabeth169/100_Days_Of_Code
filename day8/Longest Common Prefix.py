class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        i = 0
        for s in strs:
            n = min(len(prefix), len(s))
            for i in range(0, n):
                if s[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
        return prefix
