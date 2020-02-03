"""

Program: decrypt.py
Author: Samuel Tijani

"""

code = input("Enter the coded text: ")
distance = eval(input("Enter the distance value: "))
plain_text = ""

for ch in code:
    ord_value = ord(ch)
    cipher_value = ord_value - distance
    if cipher_value < ord('a'):
        cipher_value = ord('z') - (distance - (ord('a') - ord_value + 1))
        plain_text += chr(cipher_value)
    else:
        plain_text += chr(cipher_value)
print(plain_text)