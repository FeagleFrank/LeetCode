class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        half = len(x) // 2
        if half == 0:
            return True
        if x[:half] == x[-half:][::-1]:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(1001))

# Runtime: 526 ms
