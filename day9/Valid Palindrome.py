class Solution(object):
    def isPalindrome(self, s):
        a = ''.join([char.lower() for char in s if char.isalnum()])
        if (a == a[::-1]):
            return True
        else:
            return False


