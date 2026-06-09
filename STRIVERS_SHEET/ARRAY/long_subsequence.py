

nums = [100, 4, 200, 1, 3, 2,0,1]
nums.sort()
count=1
max_count=0
for i in range(len(nums)-1):
    if nums[i]==nums[i+1]:
        continue

    if nums[i]+1==nums[i+1]:
        count+=1
        max_count = max(max_count, count)
    else:

        count=1
print(max_count)
        