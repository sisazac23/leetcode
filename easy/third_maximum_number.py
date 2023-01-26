class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        to_list = sorted(list(set(nums)),reverse=True)
        if len(to_list) >= 3:
            return to_list[2]
        else:
            return to_list[0]