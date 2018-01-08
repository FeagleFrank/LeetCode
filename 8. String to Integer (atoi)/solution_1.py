class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip()
        st = ''
        f = True
        si = 1
        for i in s:
            if i == '-' and f:
                si = -1
                f = False
                continue
            elif i == '-' and not f:
                return 0
            if i == '+' and f:
                f= False
                continue
            elif i == '+' and not f:
                return 0

            if i.isdigit():
                st += i
                f = False
            else:
                break
        if not st:
            return 0
        else:
            return max(-2**31, min(si*int(st), 2**31-1))




if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi(" b11228552307"))


# Runtime: 122 ms