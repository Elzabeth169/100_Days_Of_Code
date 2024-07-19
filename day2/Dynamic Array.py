def dynamicArray(n, queries):
    a = [[] for _ in range(n)]  # Initialize n empty arrays
    lastAnswer = 0

    for query in queries:
        qtype = query[0]
        x = query[1]
        y = query[2]

        if qtype == 1:
            idx = (x ^ lastAnswer) % n
            a[idx].append(y)
        elif qtype == 2:
            idx = (x ^ lastAnswer) % n
            size = len(a[idx])
            lastAnswer = a[idx][y % size]
            print(lastAnswer)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
