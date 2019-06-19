class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        r = [''] * numRows
        fl = numRows*2 - 2
        for i in range(len(s)):
            if i % fl < numRows:
                r[i % fl] += s[i]
            else:
                r[2 * numRows - 2 - i % fl] += s[i]

        return ''.join(r)

if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))


# Runtime: 148ms
