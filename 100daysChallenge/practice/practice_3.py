def first_last(nums):
    return (None, None) if not nums else (nums[0], nums[-1])

print(first_last([10, 20, 30]))  # (10, 30)
print(first_last([5]))           # (5, 5)
print(first_last([]))            # (None, None)