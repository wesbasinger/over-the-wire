from sys import argv
import operator

register = ["", "", "", "", "", ""]

if argv[2] == "_":

	register[0] = "_"

else:

	register[0] = int(argv[2])

if argv[3] == "_":

	register[1] = "_"

else:

	register[1] = int(argv[3])

if argv[4] == "_":

	register[2] = "_"

else:

	register[2] = int(argv[4])

if argv[5] == "_":

	register[3] = "_"

else:

	register[3] = int(argv[5])

if argv[6] == "_":

	register[4] = "_"

else:

	register[4] = int(argv[6])

if argv[7] == "_":

	register[5] = "_"

else:

	register[5] = int(argv[7])

def shift(char, i):

        normed_value = ord(char) - 65

        shifted_value = (normed_value + i) % 26

        return chr(shifted_value + 65)

def process(text):

        result = ""

        for i in range(len(text) - 1):

				if i % 6 == 0:

					if register[0] == "_":

						result += "_"

					else:

						result +=  shift(text[i], register[0]) # 22 looked GOOD (W)
				elif i % 6 == 1:

					if register[1] == "_":

						result += "_"

					else:

						result += shift(text[i], register[1])
				
				elif i % 6 == 2:

					if register[2] == "_":

						result += "_"

					else:

						result += shift(text[i], register[2])

				elif i % 6 == 3:

					if register[3] == "_":

						result += "_"

					else:

						result += shift(text[i], register[3])

				elif i % 6 == 4:

					if register[4] == "_":

						result += "_"

					else:

						result += shift(text[i], register[4])

				elif i % 6 == 5:

					if register[5] == "_":

						result += "_"

					else:

						result += shift(text[i], register[5])

        return result

with open(argv[1]) as f:

        result = process(f.read())

        print result

        letter_count = {}

        for letter in result:

                try:

                        letter_count[letter] += 1

                except KeyError:

                        letter_count[letter] = 1

        s_letter_count = sorted(letter_count.items(), key=operator.itemgetter(1), reverse=True)

        print s_letter_count

