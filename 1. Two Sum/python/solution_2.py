class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_x = []
        for i in nums:
            if (target - i) in nums_x:
                return nums.index(target - i), len(nums_x)
            else:
                nums_x.append(i)


if __name__ == '__main__':
    input_nums = [3, 3]
    input_target = 6
    s = Solution()
    print(s.twoSum(input_nums, input_target))

# Run Time: 562 ms

