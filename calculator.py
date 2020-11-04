print("this will only work with 2 numbers")
def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print('what do you want to calculate?')
print("1: add")
print("2: subtract")
print('3: multiply')
print('4: divide')
while True:
    choice = input('add:1, subtract:2, multiply:3, divide:4, which one do you want? ')
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input('first number: '))
        num2 = float(input('second number: '))
        
        if choice == '1':
            print(num1, 'plus', num2, 'equals', plus(num1, num2))
        
        elif choice == '2':
            print(num1, 'minus', num2, 'equals', minus(num1, num2))
        
        elif choice == '3':
            print(num1, 'divided by', num2, 'equals', multiply(num1, num2))
        
        elif choice == '4':
            print(num1, 'divided by', num2, 'equals', divide(num1, num2))
    break