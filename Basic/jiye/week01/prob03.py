list=['a','e','i','o','u','A','E','I','O','U']

while True:
    count = 0
    sen=input()
    if sen == '#':
        break
    for s in sen:
        if s in list:
            count += 1
    print(count)
