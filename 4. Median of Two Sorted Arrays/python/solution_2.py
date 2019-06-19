class Solution:
    def findK(self, nums1, nums2, k):

        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        ia, ib = len(nums1) // 2, len(nums2) // 2
        ma, mb = nums1[ia], nums2[ib]
        if ia + ib < k:
            if ma > mb:
                return self.findK(nums1, nums2[ib + 1:], k - ib - 1)
            else:
                return self.findK(nums1[ia + 1:], nums2, k - ia - 1)
        else:
            if ma > mb:
                return self.findK(nums1[:ia], nums2, k)
            else:
                return self.findK(nums1, nums2[:ib], k)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)
        l = l1 + l2
        if l % 2 == 1:
            return float(self.findK(nums1, nums2, l // 2))
        else:
            return (self.findK(nums1, nums2, l // 2) + self.findK(nums1, nums2, l // 2 - 1)) / 2.0


if __name__ == "__main__":
    s = Solution()
    input_nums1 = [1, 3]
    input_nums2 = [2, 4, 6, 8]
    print(s.findMedianSortedArrays(input_nums1, input_nums2))

# Run Time: 179 ms
