'''
Lab 6
Yi Su
COP3502C
Section 12309
Version Change
'''


def encode(password):
    result = ""
    for digit in password:
        result += str(int(digit) + 3)
    return str(result)


