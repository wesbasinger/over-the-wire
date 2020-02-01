from sys import argv
import operator
import operator
import operator
import operator

register = ["",  "", ""]

for i in range(2,5):

	if argv[i] == "_":

		register[i-2] = "_"

	else:

		register[i-2] = int(argv[i])

print register

def shift(char, i):

        normed_value = ord(char) - 65

        shifted_value = (normed_value + i) % 26

        return chr(shifted_value + 65)

def process(text):

        result = ""

        for i in range(len(text) - 1):

				if i % 3 == 0:

					if register[0] == "_":

						result += "_"

					else:

						result +=  shift(text[i], register[0]) # 22 looked GOOD (W)
				elif i % 3 == 1:

					if register[1] == "_":

						result += "_"

					else:

						result += shift(text[i], register[1])
				
				elif i % 3 == 2:

					if register[2] == "_":

						result += "_"

					else:

						result += shift(text[i], register[2])

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

