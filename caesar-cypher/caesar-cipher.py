import caesar_art, my_tools
from os import system

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(e_text,e_shift,e_direction):
    output =""
    for c in range(0,(len(e_text))):
        if e_text[c] not in alphabet :
            # non-alphabet chars
            output += e_text[c]
        else:
            if e_direction == "d":
                shift_index = alphabet.index(e_text[c]) - e_shift
            else:
                shift_index = alphabet.index(e_text[c]) + e_shift

            if abs(shift_index) >= len(alphabet):
                shift_index %= len(alphabet)
            output += alphabet[shift_index]
    
    print(f"RESULT:-\n{output}\n")

again = True
while again:
    my_tools.clrscr()
    print(caesar_art.title)
    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
    text = input("Type your message:\n").lower()

    while True:      # keep looping until we break out of the loop
        try:
            shift = int(input("Type the shift number:\n"))
            break    # exit the loop if the previous line succeeded
        except ValueError:
            print("ERROR: the shift number needs to be an integer!")
    
    encrypt(e_text=text,e_shift=shift,e_direction=direction)
    
    if "y" not in input("Again?"):
        again = False

my_tools.clrscr()
print(caesar_art.title)
print("Goodbye.")