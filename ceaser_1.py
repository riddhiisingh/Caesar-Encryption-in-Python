from string import ascii_lowercase, ascii_uppercase, punctuation
import string

def ceasar(text, shift, alphabets):
    def shift_alphabet(alphabet) :
        return alphabet[shift: ] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabets = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabets, final_shifted_alphabet)
    return text.translate(table)

plain_text = "This is a test"
print(ceasar(plain_text,7,[ string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))