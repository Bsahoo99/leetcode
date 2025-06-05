# Last updated: 6/5/2025, 2:10:50 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}

        for i,j in enumerate(nums) :
            difference = target - j
            if difference in Map:
                return [Map[difference],i]
            Map[j] = i    