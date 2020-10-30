import math, random


def generate_otp():
    digits = "0123456789"
    code = ""
    for i in range(6) :
        code += digits[math.floor(random.random() * 10)]
    return code
