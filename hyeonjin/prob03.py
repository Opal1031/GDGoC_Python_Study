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