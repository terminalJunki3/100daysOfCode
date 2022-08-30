import string

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
exit = False


def caesar(text, shift, direction):
    if shift > 26:
        print("Select shift between 0 and 26. Try again.")
    encrypted = list()
    for i in text:
        try:
            if direction == "encode":
                if alphabet.index(i) + shift >= 26:
                    encrypted.append(alphabet[alphabet.index(i) + shift - 26])
                else:
                    encrypted.append(alphabet[alphabet.index(i) + shift])
            elif direction == "decode":
                encrypted.append(alphabet[alphabet.index(i) - shift])
        except ValueError as a:
            encrypted.append(i)

    print(''.join(encrypted))


caesar(text=text, shift=shift, direction=direction)
