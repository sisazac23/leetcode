class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        array_dic = {}
        for i,n in enumerate(numbers):
            diff = target - n
            if diff in array_dic:
                return [array_dic[diff],i+1]
            array_dic[n] = i+1