# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

#O(d) time | O(1) space where d is the height of the descendant who is the lowest in the tree
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	height1 = findHeight(descendantOne, 1)
	height2 = findHeight(descendantTwo, 1)
	diff = abs(height1 - height2)

	if height1 > height2:
		return findAncestor(descendantOne, descendantTwo, diff)
	else:
		return findAncestor(descendantTwo, descendantOne, diff)

def findAncestor(lowestDescendant, highestDescendant, diff):
	while diff > 0:
		lowestDescendant = lowestDescendant.ancestor
		diff -= 1

	while lowestDescendant != highestDescendant:
		lowestDescendant = lowestDescendant.ancestor
		highestDescendant = highestDescendant.ancestor

	return highestDescendant

def findHeight(node, currentHeight):
	currentHeight += 1
	while node.ancestor is not None:
		node = node.ancestor
		currentHeight += 1
	return currentHeight