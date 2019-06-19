class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = 0
        longest_s = s[0]
        for i in range(len(s)):
            j, k = i-1, i+1
            while j >= 0 and k < len(s):
                if s[j] == s[k]:
                    if k-j+1 > longest:
                        longest = k-j+1
                        longest_s = s[j:k+1]
                    j -= 1
                    k += 1
                else:
                    break

        for i in range(len(s)):
            j, k = i, i+1
            while j >= 0 and k < len(s):
                if s[j] == s[k]:
                    if k-j+1 > longest:
                        longest = k-j+1
                        longest_s = s[j:k+1]
                    j -= 1
                    k += 1
                else:
                    break

        return longest_s

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))

# RunTime: Time Limit Exceeded
