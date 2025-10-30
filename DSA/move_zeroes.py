def move_zero(nums):
    pos=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[pos],nums[i]=nums[i],nums[pos]
            pos+=1
    return nums
nums=[0,0,0,20,21,17,30,0]
print("the arr after moving zeroes",move_zero(nums))