# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

#O(d) time | O(d) space where d is the height of the descendant who is the lowest in the tree


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    ancestors1 = []
	ancestors2 = []
	findAncestors(descendantOne, ancestors1)
	findAncestors(descendantTwo, ancestors2)

	idx1 = len(ancestors1) - 1
	idx2 = len(ancestors2) - 1
	commonAncestor = None

	while idx1 >= 0 and idx2 >= 0:
		if ancestors1[idx1].name == ancestors2[idx2].name:
			commonAncestor = ancestors1[idx1]
		idx1 -= 1
		idx2 -= 1
	return commonAncestor


def findAncestors(treeNode, ancestors):
	ancestors.append(treeNode)
	if treeNode.ancestor is not None:
		findAncestors(treeNode.ancestor, ancestors)
