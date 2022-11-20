def decimalToBinary(decimalNumber):
    if decimalNumber > 0:
        decimalToBinary(decimalNumber//2)
    print(decimalNumber%2, end='');

binary = decimalToBinary(20)