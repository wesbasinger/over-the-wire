f = open("results.txt")

g = open("found1")

results = f.read()

squashed = g.read()

i = 0

while i < len(results):

	print results[i:i+109]
	print squashed[i:i+109]

	print "----------------------------"

	i += 108
