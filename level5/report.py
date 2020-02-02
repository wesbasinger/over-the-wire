from sys import argv
import operator

f = open("found3")
text = f.read()

register = []

columns = [[], [], [], [], [], [], [], [], []]

for i in range(len(text)):

	columns[i % 9].append(text[i])

for i in range(1, len(argv)):

	print argv[i]

	if argv[i] == "_":

		register.append("_")

	else:

		register.append(int(argv[i]))


def shift(char, i):

        normed_value = ord(char) - 65

        shifted_value = (normed_value + i) % 26

        return chr(shifted_value + 65)

'''
for i in range(len(columns)):

	print "Letter frequency for register " + str(i)

	results = {}

	for letter in columns[i]:

		try:

			results[letter] += 1

		except KeyError:

			results[letter] = 1

	print results
'''

print register

final_result = ""

for i in range(len(text)):

	idx = i % len(register)

	if register[idx] == "_":

		final_result += "_"

	else:

		final_result += shift(text[i], register[idx])

print final_result

letter_count = {}

for letter in final_result:

	try:

		letter_count[letter] += 1

	except KeyError:

		letter_count[letter] = 1

s_letter_count = sorted(letter_count.items(), key=operator.itemgetter(1), reverse=True)

print s_letter_count
