import sys
input=sys.stdin.readline

while True:
    try:
        line=input()
        if not line:
            break
        print(line,end='')
    except:
        break