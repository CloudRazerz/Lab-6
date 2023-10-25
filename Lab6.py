def encode(password):
    result = ""
    for digit in password:
        result += str(int(digit) + 3)
    return str(result)