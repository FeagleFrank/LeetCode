import numpy as np

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        dp = np.zeros((m+1, n+1))
        dp[0, 0] = 1

        for i in range(1, n+1):
            if i > 1 and p[i-1] == '*' and dp[0, i-2]:
                dp[0, i] = 1

        # print(dp)
        for i in range(1, m+1):
            flag = False
            for j in range(1, n+1):
                if p[j-1] == '*':
                    if dp[i][j-2] or ((s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j]):
                        dp[i][j] = 1
                        flag = True
                else:
                    # print(i,j)
                    if (p[j-1] == '.' or s[i-1] == p[j-1]) and dp[i-1][j-1]:
                        dp[i][j] = 1
                        flag = True
            if not flag:
                return False

        # print(dp)
        return bool(dp[m][n])

if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("aaab", "a*b"))

# Runtime: 140 ms

# TEST:
# "aa","a"
# "aa","aa"
# "aaa","aa"
# "aa", "a*"
# "aa", ".*"
# "ab", ".*"
# "aab", "c*a*b"
# "aaa", "a*a"
# "aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b"
# "aaa", "ab*a*c*a"                                         True
# "ab", ".*.."                                              True
