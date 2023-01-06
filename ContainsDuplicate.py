#Question No:217

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
         numsSet =  set(nums)
         if len(nums) == len(numsSet):
            return False
         return True
l1=Solution()
print(l1.containsDuplicate([1,1,2,3,4]))
