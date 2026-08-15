# Day 13 - Find the Missing Number

nums = [1, 2, 3, 5, 6]

n = len(nums) + 1

expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

missing = expected_sum - actual_sum

print("Missing Number:", missing)


### Using Sort

nums = [1, 2, 3, 5, 6]

nums.sort()

for i in range(len(nums)):
    if nums[i] != i + 1:
        print("Missing Number:", i + 1)
        break
else:
    print("Missing Number:", len(nums) + 1)