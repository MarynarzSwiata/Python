def check_driving_eligibility(age, has_license):
    if age < 18:
        return "You are not allowed to drive."
    elif age >= 18 and has_license == "yes":
        return "You are allowed to drive."
    elif age >= 18 and has_license == "no":
        return "You need a driver's license to drive."
    else:
        return "Invalid input for driver's license."


age = int(input("Enter your age: "))
driver_license = (
    input("Do you have a driver's license? (yes/no): ").strip().lower()
    if age >= 18
    else "no"
)

print(check_driving_eligibility(age, driver_license))
