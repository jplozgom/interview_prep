"""
This problem was asked by Airbnb.

We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSC300'].

"""

def courseDependencyManager(courses):
    courseListPerLevel = {}
    memory = {}
    maxLevel = 0
    for courseCode in courses.keys():
        maxLevel = findCourseList(courses, courseCode, memory, 0, courseListPerLevel)

    courseList = []
    for i in range(maxLevel, -1, -1):
        courseList += courseListPerLevel[i]

    # print(courseListPerLevel)
    return courseList

def findCourseList(courses, courseCode, memory, level, courseListPerLevel):

    if courseCode in memory:
        return memory[courseCode]

    maxLevel = level
    if len(courses[courseCode]) > 0:
        for depCourseCode in courses[courseCode]:
            maxLevel = max(maxLevel, findCourseList(courses, depCourseCode, memory, level + 1, courseListPerLevel))

    if level not in courseListPerLevel:
        courseListPerLevel[level] = []

    courseListPerLevel[level].append(courseCode)
    memory[courseCode] = maxLevel
    return maxLevel

"""
tests

data = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
data = {'CSC400': ['CSC300'], 'CSC300': ['CSC100', 'CSC200'], 'CSC350': ['CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}


"""
data1 = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
data2 = {'CSC400': ['CSC300'], 'CSC300': ['CSC100', 'CSC200'], 'CSC350': ['CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}

res1 = courseDependencyManager(data1)
res2 = courseDependencyManager(data2)

print(res1)
print(res2)

assert res1 == ['CSC100', 'CSC200', 'CSC300']



