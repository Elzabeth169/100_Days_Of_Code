#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#


def equalStacks(h1, h2, h3):
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]
    for i in range(1, len(h1)):
        h1[i] += h1[i - 1]
    for i in range(1, len(h2)):
        h2[i] += h2[i - 1]
    for i in range(1, len(h3)):
        h3[i] += h3[i - 1]
    while h1[-1] != h2[-1] or h1[-1] != h3[-1]:
        if h1[-1] >= h2[-1] and h1[-1] >= h3[-1]:
            h1.pop()
        elif h2[-1] >= h1[-1] and h2[-1] >= h3[-1]:
            h2.pop()
        elif h3[-1] >= h1[-1] and h3[-1] >= h2[-1]:
            h3.pop()
        if not h1 or not h2 or not h3:
            return 0

    return h1[-1]
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
