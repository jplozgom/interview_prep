def cycleInGraph(edges):
    visited = set()
    recStack = set()

    for edgeIdx in range(len(edges)):
       if edgeIdx not in visited:
           hasCycle = findCycle(edges, edgeIdx, visited, recStack)
           print(edges[edgeIdx], visited)
           if hasCycle:
               return True
    return False


def findCycle(edges, edgeIdx, visited, recStack):
    visited.add(edgeIdx)
    if edgeIdx in recStack:
        return True
    else:
        recStack.add(edgeIdx)

    connectedEdges = edges[edgeIdx]
    for neighborIdx in connectedEdges:
        hasCycle = findCycle(edges, neighborIdx, visited, recStack)
        if hasCycle:
            return True

    recStack.remove(edgeIdx)

    return False


""" ************************************************************************

************************************************************************ """

edges = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]
edges2 = [[1, 2], [2], []]

res1 = cycleInGraph(edges)
res2 = cycleInGraph(edges2)

print(res1)
print(res2)

assert res1 == True
assert res2 == False
