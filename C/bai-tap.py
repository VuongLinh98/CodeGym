i = 0

j = 20

while True:

    j -= 2

    i += 3

    if i >= j:

        break

    if j > 15:

        continue

    print(i, j)

else:
    print(j)

print("a")