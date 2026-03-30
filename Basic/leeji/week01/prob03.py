mou = "aeiouAEIOU"

while True:
    sen = input()
    count = 0
    if sen == '#':
        break
    for i in sen:
        if i in mou:
            count += 1
    print(count)
