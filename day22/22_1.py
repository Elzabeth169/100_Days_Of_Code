class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # Left pass: calculate product of all elements to the left of each index
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # Right pass: calculate product of all elements to the right of each index
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
