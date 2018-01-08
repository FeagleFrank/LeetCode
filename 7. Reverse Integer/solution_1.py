class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            xx = - int(str(x)[1:][::-1])
        else:
            xx = int(str(x)[::-1])

        # if -2**31 <= xx <= 2**31-1:
        #     return xx
        # else:
        #     return 0
        # return xx if xx.bit_length()<32 else 0

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-123))


# Runtime: 106 ms
