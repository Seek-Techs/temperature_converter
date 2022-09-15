
    
while True:
    tem = int(input('Enter temperature: '))
    
    unit = input('fahrenheit (f) or kelvin (k):? ')

    if unit.lower() == 'fahrenheit' or unit.lower() == 'f':
        converted = float(tem) - 273.15
        print(f'the temperature of {tem}Fahrenheit is equivalent to {converted}')
    elif unit.lower() == 'kelvin' or unit.lower() == 'k': 
        converted = float(tem) * (100/212)
        print(f'the temperature of {tem}Celsius is equivalent to {converted}')
    else:
        print('enter correct input')
    again = input('do you want to continue y/n ')
    if again.lower() == 'n':
        break
        

