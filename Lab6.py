'''
Lab 6
Yi Su
COP3502C
Section 12309
Version Change
'''

#Yi
def encode(password):
    result = ""
    for digit in password:
        result += str(int(digit) + 3)[-1]
    return str(result)

#Will
def decode(word):
    result = ""
    for i in range(0, len(word)):
        num = int(word[i])
        num += 10
        num -= 3
        if num >= 10:
            num -= 10
            result = result + str(num)
        else:
            result = result + str(num)
    return result

#Menu
if __name__ == "__main__":
    running = True
    password = ""
    while running:
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit
              """)
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!\n")
        if choice == 2:
            print(f"The encoded password is {password}, and the original password is {decode(password)}.")
        if choice == 3:
            running = False
            break