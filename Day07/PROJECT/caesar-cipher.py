# 7th Day Project: Caesar Cipher
# This project demonstrates the concepts I've learned so far in Python by building a Caesar Cipher.

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar_cipher(start_text, shift, direction):
    end_text = ""
    if direction == 'decode':
        shift *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {direction}d text is {end_text}")

should_continue = True
while should_continue:
    direction = input("Enter encode to Encrypt, decode to Decrypt: ")
    start_text = input("Enter your message: ").lower()
    shift = int(input("Enter shift amount: "))
    shift %= 26
    caesar_cipher(start_text=start_text, shift=shift, direction=direction)

    result = input("If you want to continue say yes, else no: ").lower()
    if result == 'no':
        should_continue = False
        print("Goodbye")
