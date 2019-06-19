class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l < 2:
            return l
        dp = 1
        visit = {s[0]: 0}
        last_start = 0
        longest = 1
        for i in range(1, len(s)):
            if s[i] in visit:
                if last_start <= visit[s[i]]:
                    dp = i - visit[s[i]]
                    last_start = visit[s[i]] + 1
                    visit[s[i]] = i
                else:
                    dp += 1
                    visit[s[i]] = i
            else:
                dp += 1
                visit[s[i]] = i
            if dp > longest:
                longest = dp
        return longest


if __name__ == "__main__":
    s = Solution()
    input_string = 'abbca'
    print(s.lengthOfLongestSubstring(input_string))

# Run Time: 142 ms
