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

'''
Comment:

문제 풀이에는 이상이 없으나, 모음 리스트를 문자열로 표현하는 것이 더 간결합니다.
예를 들어, vowels = "aeiouAEIOU"로 표현하면, 리스트 대신 문자열로 모음을 관리할 수 있습니다.
'''