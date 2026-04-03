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

'''
Comment:

except만 except EOFError로 좁히거나,
아에 except 없이 if not line: break로만 처리해도 될 것 같습니다.

except는 예상치 못한 에러가 발생할 수 있기 때문에, 최대한 좁히는 것이 좋습니다.
'''