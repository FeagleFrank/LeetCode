class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parentheses = {'(': ')', '[': ']', '{': '}', }
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in ('(', '[', '{'):
                stack.append(i)
            else:
                if len(stack) > 0 and parentheses[stack.pop()] == i:
                    continue
                else:
                    return False
        if len(stack) > 0:
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("[()]"))


# Runtime: 36ms
