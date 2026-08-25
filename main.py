from utils import square, is_even, celsius_to_fahrenheit, greet
number = float(input("Enter a number: "))

print("Square:", square(number))

if is_even(number):
    print("Even: True")
else:
    print("Even: False")

print("Fahrenheit:", celsius_to_fahrenheit(number))


name = input("Enter your name: ")
print(greet(name))