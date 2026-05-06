import random
import string

def generate_pass(length):
    # generate a random password of a given length.
    char= string.ascii_letters + string.digits + string.punctuation

    password= ''.join(random.choice(char) for _ in range(length))
    return password


print(generate_pass(10))
