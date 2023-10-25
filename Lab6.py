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

def decode(password):
    return

if __name__ == "__main__":
    running = True
    password = int
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
            print("Your password has been encoded and stored!")
        if choice == 2:
            print(f"The encoded password is {password}, and the original password is {decode(password)}.")
        if choice == 3:
            running = False
            break