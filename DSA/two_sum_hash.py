def two_sum(nums,target):
    seen={}
    for i,num in enumerate(nums):
        complement=target-num
        if complement in seen:
         print(f"first number {complement} the index:{seen[complement]}")
         print(f"second number {num} the index:{i}")
         return [seen[complement],i]
        seen[num]=i
nums=[3,7,10,32,23]
target=17
print(f"the index of two no{two_sum(nums,target)}")