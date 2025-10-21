age = int(input("Enter your age: "))
driver_license = input("Do you have a driver's license? (yes/no): ").strip().lower()

if age >= 18 and driver_license == "yes":
    print("You are allowed to drive.")
elif age >= 18 and driver_license == "no":
    print("You need a driver's license to drive.")
else:
    print("You are not allowed to drive.")
