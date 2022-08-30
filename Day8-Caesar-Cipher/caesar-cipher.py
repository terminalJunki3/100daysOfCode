import string
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
exit = False


def skip_special(letter):
    if letter.isalpha():
        print("hi")

def caesar(text, shift, direction):
        encrypted = list()
        for i in text:
            if direction == "encode":
                if alphabet.index(i) + shift >= 26:
                    encrypted.append(alphabet[alphabet.index(i) + shift - 26])
                else:
                    encrypted.append(alphabet[alphabet.index(i) + shift])
            elif direction == "decode":
                encrypted.append(alphabet[alphabet.index(i) - shift])

        print(''.join(encrypted))


caesar(text=text, shift=shift, direction=direction)
