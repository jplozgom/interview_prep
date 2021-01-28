"""
This problem was asked by Airbnb.

We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSC300'].

"""

def courseDependencyManager(courses):
    courseListPerLevel = {}
    memory = set()
    maxLevel = 0
    courseList = []
    for courseCode in courses.keys():
        if courseCode not in memory:
            findCourseList(courses, courseCode, memory, courseList)

    return courseList

def findCourseList(courses, courseCode, memory, courseList):

    if courseCode in memory:
        return

    if len(courses[courseCode]) > 0:
        for depCourseCode in courses[courseCode]:
            findCourseList(courses, depCourseCode, memory, courseList)

    courseList.append(courseCode)
    memory.add(courseCode)

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



