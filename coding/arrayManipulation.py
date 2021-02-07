"""
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

Example

n=10

q = [[1,5,3], [4,8,7], [6,9,1]]

Queries are interpreted as follows:
"""

n = 10
q = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]

n2 = 10
q2 = [[2,6,8],[3,5,7],[1,8,1],[5,9,15]]

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):

    maxValue = 0
    array = [0] * n

    for query in queries:
        start = query[0] - 1
        end = query[1]
        valueToAdd = query[2]

        array[start] += valueToAdd
        if end < n:
            array[end] -= valueToAdd

    runningSum = 0
    for value in array:
        runningSum += value
        if runningSum > maxValue:
            maxValue = runningSum

    return maxValue

res = arrayManipulation(n, q)
res2 = arrayManipulation(n2, q2)

assert res == 10
assert res2 == 31

print(res)
print(res2)
