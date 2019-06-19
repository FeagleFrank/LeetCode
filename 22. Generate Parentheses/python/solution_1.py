class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []

        def loop(s, stack, count):
            if stack == 0 and count == 0:
                l.append(s)
                return
            elif stack == 0:
                loop(s+'(', stack+1, count-1)
            elif count == 0:
                loop(s+')', stack-1, count)
            else:
                loop(s+'(', stack+1, count-1)
                loop(s+')', stack-1, count)

        loop('', 0, n)
        return l


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))


# Runtime: 40 ms
