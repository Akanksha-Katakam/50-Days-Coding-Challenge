# Day 12 - Move Zeroes

nums = list(map(int,input().split()))

left = 0

for right in range(len(nums)):
    if nums[right] != 0:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1

print(nums)