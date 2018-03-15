class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == int(str(x)[::-1]):
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(12321))

# Runtime: 559 ms
