import time


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        al = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        nl = (1, 5, 10, 50, 100, 500, 1000)

        if num == 0:
            return ''
        if num in nl:
            return al[nl.index(num)]

        index = 7
        for n in reversed(nl):
            index -= 1
            # print(num % nl[index])
            if index % 2 == 0:
                if 3 >= int(num / n) > 0:
                    return int(num / nl[index]) * al[index] + self.intToRoman(num % nl[index])
                elif int(num / n) > 3:
                    return al[index] + al[index+1] + self.intToRoman(num - nl[index + 1] + nl[index])
            else:
                if num >= nl[index + 1] - nl[index - 1]:
                    return al[index -1] + al[index + 1] + self.intToRoman(num - nl[index + 1] + nl[index - 1])
                elif int(num / n) > 0:
                    return al[index] + self.intToRoman(num - n)


        # if num / 1000 > 0:
        #     return num / 1000 * al[6] + self.intToRoman(num % 1000)





if __name__ == "__main__":
    s = Solution()
    d1 = time.clock()
    print(s.intToRoman(1800))
    d2 = time.clock()
    print(d2 - d1)


# Runtime: 176 ms


# Ⅰ（1）、Ⅴ（5）、Ⅹ（10）、Ⅼ（50）、Ⅽ（100）、Ⅾ（500）、Ⅿ（1000）