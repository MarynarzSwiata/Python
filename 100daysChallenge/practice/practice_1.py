def count_positives(nums):
    count = 0
    for num in nums:
        if num > 0:
            count += 1
    return count

# testy
print(count_positives([1, -2, 3, 0, 5]))  # oczekiwane: 3
print(count_positives([-1, -2, -3]))      # oczekiwane: 0
print(count_positives([]))                # oczekiwane: 0