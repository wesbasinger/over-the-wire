f = open("found3")

results = {}

text= f.read()

for i in range(len(text)-3):

	trigraph = text[i:i+3]

	try:

		results[trigraph].append(i)

	except KeyError:

		results[trigraph] = [i]

for trigraph in results:

	if len(results[trigraph]) > 3:

		print trigraph
		print results[trigraph]
