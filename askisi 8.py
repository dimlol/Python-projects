import random
nums=[random.randrange(-30,31) for _ in range (30)]
result = []
nums.sort()
r=len(nums)-1
for i in range(len(nums)-2):
    l = i + 1 
    while (l < r):
        sum_ = nums[i] + nums[l] + nums[r]
        if (sum_ < 0):
            l = l + 1
        if (sum_ > 0):
            r = r - 1
        if not sum_:  
            result.append([nums[i],nums[l],nums[r]])
            l = l + 1  
if (result==[]): 
    print ("Den yparxei tetoios syndyasmos")			
else:
	print(result)


