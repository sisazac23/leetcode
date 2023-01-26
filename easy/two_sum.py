class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array_dic = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in array_dic:
                return [array_dic[diff],i]
            array_dic[n] = i