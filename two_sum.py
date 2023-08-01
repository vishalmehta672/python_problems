
def twoSum(nums, target):
    num = 0
    for i in range(len(nums)):
        num = nums[i]
        for j in range(nums[i]):
            if j + num == target:
                return i ,j
            
nums = [2,7,11,15]
target = 9     
twoSum(nums, target)
            

        