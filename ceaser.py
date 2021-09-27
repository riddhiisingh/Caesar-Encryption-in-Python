import string
 
#text to be encrypted
plain_text = "hello world"

shift = 80
shift %=26

alphabet = string.ascii_lowercase

#starting the point of shift
shifted = alphabet[shift: ] + alphabet[:shift]

#translation table

table = str.maketrans(alphabet, shifted) #map the individual characters

encrypted = plain_text.translate(table)
print(encrypted)