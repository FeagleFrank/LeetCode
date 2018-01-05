class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_x = {}
        for i in range(len(nums)):
            if (target - nums[i]) in nums_x:
                return nums_x[target - nums[i]], i
            else:
                nums_x[nums[i]] = i


if __name__ == '__main__':
    input_nums = [3, 2, 4]
    input_target = 6
    s = Solution()
    print(s.twoSum(input_nums, input_target))

# Run Time: 62 ms

