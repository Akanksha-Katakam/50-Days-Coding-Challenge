# Day - 11 -> Target Sum

nums = list(map(int, input().split()))
target = int(input())

found = False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
            found = True

if not found:
    print("No pair found")