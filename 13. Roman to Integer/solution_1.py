class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        if s == '':
            return 0

        pre = num_map[s[0]]
        num = 0
        for n in s:
            m = num_map[n]
            if m > pre:
                num -= 2 * pre
            num += m
            pre = m
        return num






if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt('MMMCCCXXXIII'))


# Runtime: 136 ms


# Ⅰ（1）、Ⅴ（5）、Ⅹ（10）、Ⅼ（50）、Ⅽ（100）、Ⅾ（500）、Ⅿ（1000）