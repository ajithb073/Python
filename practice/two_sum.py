# 5/11/2021


# [2,7,11,15]    9



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_1,val_1 in enumerate(nums):
            for idx_2,val_2 in enumerate(nums[idx_1+1:]):
                if val_1+val_2== target:
                   # print(i,j)
                   return [idx_1,idx_2+idx_1+1]
                
# op -> [0,1]
