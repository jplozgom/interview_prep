class Solution:

    def __init__(self):

        self.longestSubstring = ""
        self.lengthLongestSubstring = -1
        self.memory = set()

    def longestPalindrome(self, s: str) -> str:

        self.findLongestPalindrome(s, 0, len(s) - 1)
        return self.longestSubstring


    def findLongestPalindrome(self, s: str, start, end):

        substring = s[start:end+1]
        key = str(start) + "-" + str(end)

        if key in self.memory:
            return

        self.memory.add(key)

        if len(substring) == 0:
            return ""


        isPalindrome = True
        i = 0
        j = len(substring) - 1
        while i <= j and i < len(substring) and j >= 0:
            if substring[i] != substring[j]:
                isPalindrome = False
                break
            i += 1
            j -= 1

        if isPalindrome and len(substring) > self.lengthLongestSubstring:
            self.lengthLongestSubstring = len(substring)
            self.longestSubstring = substring


        self.findLongestPalindrome(s, start + 1, end)
        self.findLongestPalindrome(s, start, end - 1)

        return self.longestSubstring

    def isPalindrome(self, str, i, j):
        i = 0
        j = len(str)
        while i <= j and i < len(str) and j >= 0:
            if substring[i] != substring[j]:
                isPalindrome = False
                break
            i += 1
            j -= 1


if __name__ == '__main__':
    palindromeEvaluator = Solution()
    palindromeEvaluator.longestPalindrome("abba")

    for number in result:
        print(number)


