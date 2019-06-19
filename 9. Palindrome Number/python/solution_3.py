class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        res = 0
        y = x
        while x != 0:
            res = res * 10 + x % 10
            x //= 10
        return True if res == y else False

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(1001))

# Runtime: 641 ms
