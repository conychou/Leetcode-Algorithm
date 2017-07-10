class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rlist = []
        nums.sort()
        for i in range(0,len(nums)-1):
            if(nums[i] == nums[i+1]):
                rlist.append(nums[i])
        return rlist
