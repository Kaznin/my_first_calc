import get_summation

def get_sum():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    z = input('Choose operation (+, -, *, /): ')

    if z == '+':
        print(get_summation(a, b))
