text = input("Please enter a word: ")

histogram = {}
for c in text:
    if c not in histogram:
        histogram[c] = 1
    else:
        histogram[c] = histogram[c] + 1

for key, value in histogram.items():
    print("'%s': %d" % (key, value))
