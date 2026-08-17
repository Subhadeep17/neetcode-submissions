class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Result array
        res = [1]*len(nums)

        #prev array in resu
        prev=1
        for i in range(len(nums)):
            res[i]=prev
            prev*=nums[i]

        #suff array in res
        suff=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=suff
            suff*=nums[i]
        return res            