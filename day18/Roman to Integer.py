class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        prev_value = 0
        for i in range(len(s) - 1, -1, -1):
            current_value = d[s[i]]
            if prev_value > current_value:
                sum = sum - current_value
            else:
                sum = sum + current_value
            prev_value = current_value

        return sum

# class Solution:
#     def romanToInt(s):
# roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# total = 0
# n = len(s)

# for i in range(n):
#     if i + 1 < n and roman_map[s[i]] < roman_map[s[i + 1]]:
#         total -= roman_map[s[i]]
#     else:
#         total += roman_map[s[i]]

# return total
