class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lr, rl = [], []

        lr_p, rl_p = 1, 1
        for i in range(len(nums)):
            lr.append(lr_p*nums[i])
            lr_p *= nums[i]

            rl.insert(0, nums[len(nums)-i-1]*rl_p)
            rl_p *= nums[len(nums)-i-1]

        res = []

        print(lr)
        print(rl)
        
        for i, x in enumerate(nums):
            if i == 0:
                res.append(rl[i+1])
            elif i == len(nums)-1:
                res.append(lr[i-1])
            else:
                res.append(lr[i-1]*rl[i+1])

        return res
