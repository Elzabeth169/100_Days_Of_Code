# User function Template for python3
from collections import deque


class Solution:
    # Function to reverse the queue.
    def rev(self, q):
        # add code here
        stack = deque()

        while not q.empty():
            stack.append(q.get())

        while stack:
            q.put(stack.pop())

        return q
Im