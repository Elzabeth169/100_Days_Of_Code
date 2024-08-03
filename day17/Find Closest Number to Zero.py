class Solution:
    def absolute(x):
        if x < 0:
            return -x
        else:
            return x

    def findClosestNumber(self, nums: List[int]) -> int:
        length = len(nums)
        min = float('inf')
        for i in range(length):
            abso = abs(nums[i])
            if abso < min or (abso == min and nums[i] > closest):
                min = abso
                closest = nums[i]

        return closest
