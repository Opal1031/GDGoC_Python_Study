

import sys
input = sys.stdin.readline

while True:
    a = input() 

    if not a: 
        break 

    print(a, end="")

'''
Comment:

EOFError을 except로 처리하는 방법도 있지만, 이렇게 입력이 없을 때 break하는 방법도 있습니다.
둘 중 어떤 방법이든 상관없습니다.
'''