class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if digits == "":
            return []
        al = [[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        l = al[int(digits[0])]

        for i in digits[1:]:
            ret = []
            for j in l:
                for k in al[int(i)]:
                    ret.append(j + k)
            l = ret.copy()
        return l




if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))


# Runtime: 40ms
