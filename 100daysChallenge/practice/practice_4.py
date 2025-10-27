def only_even(nums):
    result = []
    for i in nums:
        if i % 2 == 0:
            result.append(i)
    return result

print(only_even([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]
print(only_even([1, 3, 5]))           # []
print(only_even([]))                  # []