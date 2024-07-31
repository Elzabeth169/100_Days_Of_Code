class Solution:
    def maxSubArray(self, num: List[int]) -> int:
        current_sum=num[0]
        max_sum=num[0]
        for i in range(1,len(num)):
            current_sum=max(num[i],current_sum+num[i])
            max_sum=max(max_sum,current_sum)
        return max_sum
