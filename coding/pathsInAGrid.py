"""

find the total number of paths from left upper coner to the right bottom corner in an n*m grid assuming you can only move right or down.

"""

def findPaths(r, c, memory):

    key = str(r) + "-" + str(c)
    if r == 1 or c == 1:
        return 1

    else:
        if key in memory:
            return memory[key]

        paths = findPaths(r, c-1, memory) + findPaths(r-1, c, memory)
        memory[key] = paths
        return paths

memory = {}

res1 = findPaths(2, 2, memory)
res2 = findPaths(1, 1, memory)
res3 = findPaths(3, 3, memory)
res4 = findPaths(5, 5, memory)
res5 = findPaths(50, 50, memory)

assert res1 == 2
assert res2 == 1
assert res3 == 6
assert res4 == 70
assert res5 == 25477612258980856902730428600


print(res1)
print(res2)
print(res3)
print(res4)
print(res5)