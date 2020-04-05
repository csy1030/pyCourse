class Solution:
    def merge(self, nums1, nums2):
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        while i < len(nums1) and nums2:

            if nums1[i] > nums2[0]:
                nums1.insert(i, nums2[0])
                del nums1[-1]
                del nums2[0]
            i += 1
        res = len(nums2)
        for i in range(res):
            del nums1[-1]

        for item in nums2:
            nums1.append(item)
        return nums1
s = Solution()
print(s.merge([2,0],[1]))