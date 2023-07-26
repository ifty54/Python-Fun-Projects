#calculator
def add(x,y):
    return x + y
def substract(x,y):
    return x - y

def divide(x,y):
    return x / y

def multiply(x,y):
    return x * y

print("select operation")
print("1. Add")
print("2. Substract")
print("3. Divide")
print("4. Multiply")


#taking input from users
while True:
    choice = input("enter choice(1/2/3/4): ")

    if choice in ('1','2','3','4'):
        num1 = float(input("1st number: "))
        num2 = float(input("2nd number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", substract(num1, num2))

        elif choice == '3':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '4':
            print(num1, "*", num2, "=", multiply(num1, num2))

        break
    else:
        print("invalid input")
