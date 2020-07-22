import random


def extfst(str):
    return "".join(map(lambda x: x[0], str.split(" ")))


def randchr():
    return chr(random.randrange(97, 122))


def randchrs(low=290, hi=310):
    return "".join([randchr() for _ in range(random.randint(low, hi))])


print("""It is important to note the importance of importance. What may be
discarded as unimportant may actually be of great importance. Therefore place a
great deal of importance on how you assign importance to the seemingly
unimportant, because it is important.""", end="\n\n")
print("""In this case, it is important to note that this file is generated via
github actions and that the following characters are all randomized except for
6 of them, which points to another account.""",
      end="\n\n")
# naturally, that is something that can simply be done by looking at the source
print("{0}{1}{2}".format(randchrs(), extfst(
    # @
    "ruthless enemies infiltrated 20 hours undetected"), randchrs()))
