def put(d, a, b):
    if a in d:
        d[a].append(b)
    else:
        d[a] = [b]


def main():
    for n in ns[::-1]:
        r = [tt[s] for s in tree[n] if s != f[n]]
        bst = {s: [gl[n], n, 0] for s in queries[n]}
        if r:
            o = max(range(len(r)), key=lambda a: len(r[a]))
            if len(r[o]) > len(bst): r[o], bst = bst, r[o]
        ry = {}
        for ae in r:
            for y, v in ae.items():
                put(ry, y, v)
        for y, r in ry.items():
            eq, z, t = 0, 0, 0
            if len(r) == 1 and y not in bst:
                bst[y] = r[0]
                continue
            if y in bst: r.append(bst.pop(y))
            for d, v, c in r:
                eq += (d - gl[n]) * v + c
                z += v
            for d, v, c in r:
                c += (d - gl[n]) * v
                diff = (eq - c) * v
                t += diff
            returns[y] += t
            bst[y] = (gl[n], z, eq)
        tt[n] = bst


def locate():
    q = [r]
    level = 0
    while q:
        level += 1
        tmp = []
        ns.extend(q)
        for n in q:
            for s in tree[n]:
                if s not in f:
                    f[s] = n
                    gl[s] = level
                    tmp.append(s)
        q = tmp


tree = {}
tt = {}
n, q = map(int, input().split())
returns = [0] * q
for _ in range(n - 1):
    a, b = map(int, input().split())
    put(tree, a, b)
    put(tree, b, a)
queries = {a: set() for a in tree}
for y in range(q):
    input()
    for x in map(int, input().split()): queries[x].add(y)
r = next(iter(tree))
ns = []
f = {r: None}
gl = {r: 0}
locate()
main()
for s in returns: print(s % (10 ** 9 + 7))