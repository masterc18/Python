import random

LettersM = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
Lettersm = 'abcdefghijklmnñopqrstuvwxyz'
Numbers = '0123456789'
Symbols = "{}[]()*;/,._-"

all = LettersM + Lettersm + Numbers + Symbols
length = 16

Password = "".join(random.sample(all, length))

print(f"This is your new password\n {Password}")