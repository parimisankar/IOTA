#Note: this is for python 3
#Note2: This one is cryptographically safe

from random import SystemRandom

ran = SystemRandom()

# build a character array of uppercase characters (A-Z) and append '9'
chars = [i for i in map(chr, range(65,91))]
chars.append('9')

# seed = an array of 81 random characters from the chararacter array
seed = [chars[ran.randrange(len(chars))] for x in range(81)]

# print the seed
for x in seed:
   print(x, end="")