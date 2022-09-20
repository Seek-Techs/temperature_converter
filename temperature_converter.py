# Temperature Converter

def menu():
    print('\n1. Celsius to Fahreheint')
    print('2. Fahreheint to Celsius')
    print('3. Exit')
    pick = int(input('\nEnter a choice: '))
    return pick

def toCelsius(c):
    return int(c - 273.15)

def toFahreheint(f):
    return int(f * (100/212))

def main():
    choice = menu()
    while True:
        if choice == 1:
            c = eval(input('Enter degree celsius: '))
            print('The temperature of ' + str(c) + 'C is equivalent to ' + str(toFahreheint(c)) + 'F')
        elif choice == 2:
            f = eval(input('Enter degree celsius: '))
            print('The temperature of ' + str(f) + 'F is equivalent to ' + str(toCelsius(f)) + 'C')
        elif choice == 3:
            print('Program Exited')
            break
        else:
            print('invalid entry')
        choice = menu()
        
        
main()