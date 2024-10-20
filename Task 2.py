def methods(i, number):
    result = 1
    number = str(number)

    if i == 1:
        digit0 = number[0]
        digit1 = number[1]
        digit2 = number[2]
        digit3 = number[3]

        result = int(digit0) * int(digit1) * int(digit2) * int(digit3)
        return result
    elif i == 2:
        for digit in number:
            result *= int(digit)
        return result
    else:
        print('The method is not found!')

a = int(input('Enter a four-digit number: '))

try: chosen = int(input('Number of the method (1-2): '))
except ValueError: print('The task is not found!')
else: print(methods(chosen, a))