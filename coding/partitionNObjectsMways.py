"""

write a function that counts the number of ways you can  partition n objects using parts up to m assuming m >= 0

"""

def findPartitions(n, m, memory, debug = False):

    if debug == True:
        print(n, m)

    if n < 0 or m <= 0:
        return 0

    if n == 0 or n == 1:
        return 1

    key = str(n) + "-" + str(m)
    if key in memory:
        return memory[key]

    currentPartitions = findPartitions(n-m, m, memory, debug) + findPartitions(n, m - 1, memory, debug)

    if key not in memory:
        memory[key] = currentPartitions

    if debug:
        print(memory)

    return currentPartitions

res1 = findPartitions(1, 3, {}, False)
res2 = findPartitions(2, 3, {}, False)
res3 = findPartitions(3, 3, {})
res4 = findPartitions(4, 4, {})
res5 = findPartitions(50, 50, {})
# res5 = findPartitions(50, 50, memory)

assert res1 == 1
# assert res2 == 1
# assert res3 == 6
# assert res4 == 70
# assert res5 == 25477612258980856902730428600

print("\n\n---\n\n")
print(res1)
print(res2)
print(res3)
print(res4)
print(res5)