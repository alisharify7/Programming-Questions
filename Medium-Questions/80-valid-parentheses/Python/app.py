class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_mapper = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = set()
        for char in s:
            if char in "{[(":
                stack.add(char)
            elif open_mapper[char] == stack.pop():
                continue
            else:
                return False

        return True




if __name__ == '__main__':
    s = "([])"
    print(Solution().isValid(s))