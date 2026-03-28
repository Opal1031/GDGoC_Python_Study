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

'''
Comment:

문제 풀이에는 이상이 없으나, 모음 리스트를 문자열로 표현하는 것이 더 간결합니다.
예를 들어, vowels = "aeiouAEIOU"로 표현하면, 리스트 대신 문자열로 모음을 관리할 수 있습니다.
'''