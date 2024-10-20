a = float(input('Enter the size of the base of the triangle in cm: '))
hA = float(input('Enter the height size in cm: '))

result = (1/2)*a*hA

if result.is_integer():
    result = int(result)

print(result)