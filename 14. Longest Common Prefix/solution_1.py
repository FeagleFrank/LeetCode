class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = ''
        if not len(strs):
            return common
        for i in range(len(strs[0])):
            c = strs[0][0:i+1]
            for j in range(1, len(strs)):
                try:
                    if not strs[j][0:i+1] == c:
                        return common
                except:
                    return common
            common = c

        return common


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix([]))


# Runtime: 44 ms
