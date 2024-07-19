#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

def swapNodes(indexes, queries):

    def build_tree(indexes):
        tree = {i: (indexes[i-1][0], indexes[i-1][1]) for i in range(1, len(indexes) + 1)}
        return tree

    def in_order_traversal(root, tree):
        result = []
        stack = []
        node = root
        while stack or node != -1:
            while node != -1:
                stack.append(node)
                node = tree[node][0]
            node = stack.pop()
            result.append(node)
            node = tree[node][1]
        return result

    def swap_at_levels(tree, k):
        queue = [(1,1)]
        while queue:
            node, depth = queue.pop(0)
            if node == -1:
                continue
            if depth % k == 0:
                tree[node] = (tree[node][1], tree[node][0])
            queue.append((tree[node][0], depth + 1))
            queue.append((tree[node][1], depth + 1))

    tree = build_tree(indexes)
    results = []

    for k in queries:
        swap_at_levels(tree, k)
        result = in_order_traversal(1, tree)
        results.append(result)

    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
