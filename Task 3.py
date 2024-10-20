m = float(input('Enter a number in meters (m) to convert to centimeters (cm), decimeters (dm), millimeters (mm), miles (mi): '))

print(f'cm: {m*100}\ndm: {m*10}\nmm: {m*1000}\nmi: {round(m*0.0006213712, 5)}')