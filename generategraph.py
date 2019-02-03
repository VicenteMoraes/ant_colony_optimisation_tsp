import random

alphabet = list(map(chr, range(97, 123)))
letters = []
distances = []
for x in range(1, int(input()) + 2):
    letters.append(random.choice(alphabet))
for i in letters:
    for t in letters:
        distances.append(i + " " + t + " " + str(random.randint(1, len(letters) + 1)))
with open("distance", "w") as wf:
    for x in distances:
        wf.write(x + "\n")
