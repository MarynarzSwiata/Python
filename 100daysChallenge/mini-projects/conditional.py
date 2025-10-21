"""#1"""

x = 10

status = "Active" if x > 5 else "Inactive"
print(status)

""" #2 """


def check_number(x):
    score = "Even" if x % 2 == 0 else "Odd"
    return score


print(check_number(int(input("Enter your number: "))))

""" #3 """


def check_sign(number):
    return "Positive" if number > 0 else "Negative" if number < 0 else "Zero"


print(check_sign(int(input("Enter a number: "))))

""" #4 """

numbers = [1, -10, 25, 0, -8, 100, -3]

categorized_list = [
    (
        f"{num} is Positive"
        if num > 0
        else f"{num} is Negative" if num < 0 else f"{num} is Zero"
    )
    for num in numbers
]

print(categorized_list)
