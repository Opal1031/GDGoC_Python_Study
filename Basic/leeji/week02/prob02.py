import sys
input = sys.stdin.readline

while True:
    line = input()

    if not line:
        break

    print(line, end='')

'''
Comment:

Good!
EOFError을 직접 활용해보는 방식도 있습니다.
'''