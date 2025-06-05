# Last updated: 6/5/2025, 10:58:21 AM
class Solution(object):
    def containsDuplicate(self, nums):
        
        seen = set()

        for n in nums:
            if n in seen :
                return True
            seen.add(n)
        return False    