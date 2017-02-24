###		Leetcode TwoSum Problem ####

###		My Solution ###
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        for index1, x1 in enumerate(nums):
        	x2 = target - x1
        	if x2 in nums:
        		index2 = nums.index(x2)
        		if index1 != index2:
        			return [index1, nums.index(x2)]


####   Best Solution ####
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i