import sys
input = sys.stdin.readline

while True:
    sentence=input()

    if sentence=="#":
        break

    cnt=0

    for i in range(len(sentence)):
        b=sentence[i]
        
        if b=='a' or b=='e' or b=='i' or b=='o' or b=='u' or b=='A' or b=='E' or b=='I' or b=='O' or b=='U':
            cnt +=1

    print(cnt)

'''
Comment:

문제 풀이에는 이상이 없으나, 모음 리스트를 문자열로 표현하는 것이 더 간결합니다.
예를 들어, vowels = "aeiouAEIOU"로 표현하면, 리스트 대신 문자열로 모음을 관리할 수 있습니다.
'''