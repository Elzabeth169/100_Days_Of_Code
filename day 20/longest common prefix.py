class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # Take the first string as the initial prefix
        prefix = strs[0]

        for string in strs[1:]:
            # Compare the prefix with each string
            i = 0
            while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
                i += 1
            # Update the prefix to the common part
            prefix = prefix[:i]
            # If the prefix becomes empty, return an empty string
            if not prefix:
                return ""

        return prefix
