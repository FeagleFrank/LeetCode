class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(s) + '#'
        RL = [0] * len(s)
        MaxRigtht = 0
        pos = 0
        MaxLen = 0
        Maxs = s[0]

        for i in range(len(s)):
            if i < MaxRigtht:
                RL[i] = min(RL[2*pos-i], MaxRigtht - i)
            else:
                RL[i] = 1
            while i-RL[i] >= 0 and i+RL[i] < len(s) and s[i-RL[i]] == s[i+RL[i]]:
                RL[i] += 1
            if RL[i] + i -1 > MaxRigtht:
                MaxRigtht = RL[i] + i - 1
                pos = i
            # MaxLen = max(MaxLen, RL[i])
            if MaxLen < RL[i]:
                MaxLen = RL[i]
                Maxs = s[i-MaxLen+1:i+MaxLen]

        return ''.join(Maxs.split('#'))

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("abcbcbcab"))

# Manacher 算法
# RunTime: 188ms
