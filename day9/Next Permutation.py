class Solution:
    def nextPermutation(self, N, arr):
        # Step 1: Find the pivot, the first element from the end that is smaller than the element after it.
        pivot = -1
        for i in range(N - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break

        if pivot == -1:  # This means the array is in descending order
            arr.reverse()
            return arr

        # Step 2: Find the rightmost element that is greater than the pivot
        for i in range(N - 1, pivot, -1):
            if arr[i] > arr[pivot]:
                # Step 3: Swap the pivot with this element
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break

        # Step 4: Reverse the elements to the right of the pivot
        arr[pivot + 1:] = reversed(arr[pivot + 1:])

        return arr