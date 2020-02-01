f = open("found1")
g = open("found2")
h = open("found3")

found1 = f.read()
found2 = g.read()
found3 = h.read()

print "found1 length is " + str(len(found1))
print "found2 length is " + str(len(found2))
print "found3 length is " + str(len(found3))

combined = found1 + found2 + found3

def get_three_letter_combos():

	results = {}

	for i in range(len(combined)-3):

		try:

			results[combined[i:i+3]] += 1

		except KeyError:

			results[combined[i:i+3]] = 1

	marked_for_deletion = []

	for combo in results:

		if results[combo] < 5:

			marked_for_deletion.append(combo)

	for _key in marked_for_deletion:

		del results[_key]

	print results

get_three_letter_combos()	

def get_four_letter_combos():

	results = {}

	for i in range(len(combined)-4):

		try:

			results[combined[i:i+4]] += 1

		except KeyError:

			results[combined[i:i+4]] = 1

	marked_for_deletion = []

	for combo in results:

		if results[combo] < 5:

			marked_for_deletion.append(combo)

	for _key in marked_for_deletion:

		del results[_key]

	print results

get_four_letter_combos()

def scan_for_trigraph(text, trigraph):

	for i in range(len(text) - 3):

		if text[i:i+3] == trigraph:

			print i

scan_for_trigraph(found1, "ZAL")
scan_for_trigraph(found2, "ZAL")
scan_for_trigraph(found3, "ZAL")

def scan_for_quadgraph(text, trigraph):

	for i in range(len(text) - 4):

		if text[i:i+4] == trigraph:

			print i

print("0000000000000000000000")

scan_for_quadgraph(found1, "JYVB")
scan_for_quadgraph(found2, "JYVB")
scan_for_quadgraph(found3, "JYVB")


