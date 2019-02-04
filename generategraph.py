import random
import string

num = int(input("How many nodes: "))
alphabet = list(string.ascii_lowercase)
strings = []
x = 0
y = 1
while len(strings) < num:
    try:
        strings.append(alphabet[x] * y)
        x += 1
    except IndexError:
        x = 0
        y += 1
distances = []
for i in strings:
    for t in strings:
        distances.append(i + " " + t + " " + str(random.randint(1, num + 1)))
with open("distance", "w") as wf:
    for x in distances:
        wf.write(x + "\n")
