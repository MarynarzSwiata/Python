minutes = int(input("Enter number of minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(
    f"{hours} hour{'s' if hours != 1 else ''} and {remaining_minutes} minute{'s' if remaining_minutes != 1 else ''}"
)
