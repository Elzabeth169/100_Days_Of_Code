from collections import deque


class Solution:
    def modifyQueue(self, q, k):
        # Step 1: Dequeue the first K elements from the queue and push them onto a stack
        stack = []
        for _ in range(k):
            stack.append(q.popleft())

        # Step 2: Pop all elements from the stack and enqueue them back to the queue
        while stack:
            q.append(stack.pop())

        # Step 3: Dequeue the remaining elements of the queue and enqueue them back
        size = len(q)
        for _ in range(size - k):
            q.append(q.popleft())

        return q


# Utility function to print the queue
def printQueue(q):
    print(" ".join(map(str, q)))


if __name__ == "__main__":
    # Example 1
    q1 = deque([1, 2, 3, 4, 5])
    k1 = 3
    solution = Solution()
    modified_q1 = solution.modifyQueue(q1, k1)
    printQueue(modified_q1)  # Expected Output: 3 2 1 4 5

    # Example 2
    q2 = deque([4, 3, 2, 1])
    k2 = 4
    modified_q2 = solution.modifyQueue(q2, k2)
    printQueue(modified_q2)  # Expected Output: 1 2 3 4