class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Determine which side is sorted
            if nums[left] <= nums[mid]:  # Left side is sorted
                if nums[left] <= target < nums[mid]:  # Target is in the left side
                    right = mid - 1
                else:  # Target is in the right side
                    left = mid + 1
            else:  # Right side is sorted
                if nums[mid] < target <= nums[right]:  # Target is in the right side
                    left = mid + 1
                else:  # Target is in the left side
                    right = mid - 1
                    #return value

        return -1