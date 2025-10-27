def square_all(nums):
    result = []
    for i in nums:
        result.append(i ** 2)
    return result


print(square_all([1, 2, 3]))     # [1, 4, 9]
print(square_all([0, -2, 5]))    # [0, 4, 25]
print(square_all([]))            # []