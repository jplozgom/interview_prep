import sys

def minSteps(number, memory, target):
    # if in memory return number
    if number in memory:
        return memory[number]

    if number  == target:
        return 0

    steps1 = minSteps(number - 1, memory, target)
    steps2 = findDivisionSteps(number, 2, memory, target)
    steps3 = findDivisionSteps(number, 3, memory, target)

    memory[number] = min(steps1, steps2, steps3) + 1
    return memory[number]


def findDivisionSteps(number, divisor, memory, target):
    if number % divisor == 0:
        return minSteps( number / divisor, memory, target)
    return sys.maxsize



if __name__ == '__main__':
    memory = {}
    print(minSteps(6, memory, 1))
    memory = {}
    print(minSteps(15, memory, 1))
    memory = {}
    print(minSteps(900, memory, 1))
