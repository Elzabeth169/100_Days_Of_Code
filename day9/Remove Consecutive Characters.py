# User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        # Edge case: If the string is empty, return an empty string
        if not S:
            return ""

        # Initialize the result with the first character of S
        result = [S[0]]

        # Iterate through the string starting from the second character
        for i in range(1, len(S)):
            # Add the character to the result if it is different from the last character in the result
            if S[i] != S[i - 1]:
                result.append(S[i])

        # Join the list into a string and return it
        return "".join(result)
