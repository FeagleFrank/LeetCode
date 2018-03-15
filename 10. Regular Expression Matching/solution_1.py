class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not bool(s)

        first_match = bool(s) and p[0] in [s[0], '.']
        if len(p) > 1 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

if __name__ == '__main__':
    s = Solution()
    print(s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c*b"))

# Runtime:Time Limit Exceeded

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
