f = open("found3")
text = f.read()

results = open("results_total.txt", "w")


def shift(char, i):

        normed_value = ord(char) - 65

        shifted_value = (normed_value + i) % 26

        return chr(shifted_value + 65)

def process(text, register):

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

for i in range(26):

	for j in range(26):

		for h in range(27):

			iter_result = process(text, [i, j, h])

			results.write("REGISTER: " + str(i) + " " + str(j) + " " + str(h) + "\n")

			results.write(iter_result)

			results.write("++++++++++++++++++++++++++++++++++")

results.close()
