number = input("enter any number you want:")
number = int(number)
if number % 5 == 0:
    print("Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
else:
    print(f"only the {number}")