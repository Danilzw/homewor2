import random


counts = int(input("Сколько кустов:"))

arrayofcounts = []

for i in range(counts):
    arrayofcounts.append(random.randint(0,9))


print(arrayofcounts)

max = 0

for i in range(-1,len(arrayofcounts)):
    if i + 1 < len(arrayofcounts):
        if arrayofcounts[i] + arrayofcounts[i+1] + arrayofcounts[i-1] > max:
            max = arrayofcounts[i] + arrayofcounts[i+1] + arrayofcounts[i-1]
            print(max)

print(max)               