def total(num):
    sum = 0
    for n in num:
        sum += n
    return sum


print(total([1,2,3])) #6
print(total([10,-5,2])) #7
print(total([])) #0
