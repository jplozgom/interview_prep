#!/bin/python3

import os
import sys

class TrieNode:
    def __init__(self, isEndWord):
        self.children = {}
        self.isEndWord = isEndWord
        self.numWords = 0

    def insert(self, characters):

        self.numWords += 1

        """
        Inserts a character into a Trie node by checking the dictionary that stores the childs. If the characters left has no       characters it means that it is an endNode
        """
        character = str(characters[0])

        #if node representing character doesn't exists insert it in children of parent
        if self.hasCharacter(character) == False:
            isEndWord = False
            self.children[character] = TrieNode(isEndWord)

        if len(characters) == 1:
            self.children[character].isEndWord = True
            self.children[character].numWords += 1
            return
        else:
            #insert remaining characters in recently inserted node
            self.children[character].insert(characters[1:])

    def search(self, characters, fullWord = False):
        """
        Searches for a string in a Trie node by checking the dictionary that stores the childs. If the characters left has no characters left and it is a every character was present the string matches
        """

        character = str(characters[0])

        #if node representing character doesn't exists search it in children of parent
        if self.hasCharacter(character) == False:
            return False, None, 0

        if len(characters) == 1 and fullWord == False:
            return True, self.children[character], self.children[character].numWords

        if len(characters) == 1 and fullWord == True and self.children[character].isEndWord == True:
            return True, self.children[character], self.children[character].numWords

        #search remaining characters in children
        return self.children[character].search(characters[1:])

    def hasCharacter(self, character):
        """
        Checks if a node has a character in it's childs
        """
        if character in self.children:
            return True
        return False

    def countChildEndWords(self):
        count = 0;
        """
        Checks if a node has a character in it's childs
        """
        if self.isEndWord:
            count += 1
        if len(self.children) == 0:
            return count

        for node in self.children.values():
            count += node.countChildEndWords()

        return count

class Trie:

    def __init__(self):
        isEndWord = False
        self.root = TrieNode(isEndWord)

    def insert(self, characters):
        self.root.insert(characters)

    def search(self, stringToSearch):

        found, lastLetterNode, numWords = self.root.search(stringToSearch)

        if found:
            return numWords
            # return lastLetterNode.countChildEndWords()

        return 0

#
# Complete the contacts function below.
#
def contacts(queries):
    database = Trie()
    matchesOutput = []
    if queries is not None:
        for queryParts in queries:
            # add operation
            if queryParts[0] == "add":
                database.insert(queryParts[1])

            # find operation
            elif queryParts[0] == "find":
                searchQuery = queryParts[1]
                matches = database.search(searchQuery)
                matchesOutput.append(matches)

    return matchesOutput




if __name__ == '__main__':
    queries_rows = 4
    # queries = [
    #     ["add", "hack"],
    #     ["add",  "hackerrank"],
    #     ["find",  "hac"],
    #     ["find",  "hak"]
    # ]

    queries = [
        ["add", "s"],
        ["add", "ss"],
        ["add", "sss"],
        ["add", "ssss"],
        ["add", "sssss"],
        ["find", "s"],
        ["find", "ss"],
        ["find", "sss"],
        ["find", "ssss"],
        ["find", "sssss"],
        ["find", "ssssss"]
    ]

    result = contacts(queries)
    print(result)
