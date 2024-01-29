import string
import random

def generate_password(length, use_special_charts=False):
    characters = string.ascii_letters + string.digits
    if use_special_charts:
        characters +=string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password



def main():
    print("Password Generator")
    try:
        length=int(input("Enter the desired password length: "))
        use_special_charts = input("Include special character? y/n: ").lower()=='y'
        if length<=0:
            print("password length should be a positive number.")
        else:
            password = generate_password(length,use_special_charts)
            print("Your Generated Password=",password)
    except:
        print("Invalid Input")
if __name__=="__main__":
    main()