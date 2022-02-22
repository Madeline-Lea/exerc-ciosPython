# Declarations

balance_hour = float(input("Type your employer hour salary: "))
month_hour = int(input("Type the hours your employer worked: "))

salary = balance_hour * month_hour
extra_hour = balance_hour * 1.5 + salary


if month_hour > 176:
    print(f"Employer salary with extra worked hours: {extra_hour}")
    print(f"Press enter to shutdown...")
elif month_hour <= 0:
    print("Please type your salary, shutting down...")
    print(f"Press enter to shutdown...")
else:
    print(f"Employer salary: {extra_hour}")
    print(f"Press enter to shutdown...")
