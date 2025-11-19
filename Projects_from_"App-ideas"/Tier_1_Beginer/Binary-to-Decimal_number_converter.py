def Bin2Dec (bin_number:str) -> int:
    power = len(bin_number) - 1
    total = 0
    for digit in bin_number:
        total += int(digit) * 2 ** power
        power -= 1
    return total
def Dec2Bin (dec_number:int) -> str:
    total=""
    while dec_number > 0:
        total = str(dec_number % 2) + total
        dec_number //= 2
    return total
def decision():
    try:
        print("What do you choose?\n")
        print("'1' for converting binary to decimal\n")
        print("'0' for converting decimal to binary\n")
        d = input("Option: ")
        if d not in {'1', '0'}:
            raise ValueError("Invalid option!")
    except ValeError as e:
        print(e)
    if int(d):
        while True:
            try:
                binNumber=input("Enter the binary number: ")
                if any(c not in {'1', '0'} for c in binNumber) or len(binNumber) > 8:
                    raise ValueError("Not a binary number or length is more than 8 digits!")
                break
            except ValueError as e:
                print(e)
        print(Bin2Dec(binNumber))
    else:
        while True:
            try:
                decNumber=int(input("Enter the decimal number: "))
                if 0>decNumber or decNumber>255:
                    raise ValueError("Invalid decimal number!")
                break
            except ValueError as e:
                print(e)
        print(Dec2Bin(decNumber))
decision()