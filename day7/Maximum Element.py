#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(op):
    stack = []
    max_stack = []
    maxm = []

    for i in op:
        temp = list(map(int, i.split()))
        if temp[0] == 1:
            stack.append(temp[1])
            if not max_stack or temp[1] >= max_stack[-1]:
                max_stack.append(temp[1])
        elif temp[0] == 2:
            if stack:
                if stack[-1] == max_stack[-1]:
                    max_stack.pop()
                stack.pop()
        elif temp[0] == 3:
            if max_stack:
                maxm.append(max_stack[-1])

    return maxm
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()