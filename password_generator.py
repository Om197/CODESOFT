
import random
import string
def password_generator():
    length = int(input("Enter desired password length: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated password: {password}")

password_generator()
