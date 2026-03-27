vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    sentence = input()
    if sentence == '#':
        break
    
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    print(count)