def isNumber (item):
    digits = item.split('.')
    for digit in digits:
        if digit.isdigit() == False:
            return False
    return True

number = input()

if(isNumber(number)):
    print("it's a number")
else:
    print("it isn't a number")