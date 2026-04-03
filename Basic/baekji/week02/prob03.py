import sys
input=sys.stdin.readline

while True:
    try:
        line=input()

        if not line:
            break

        a,b=map(int,line.split())

        print(a+b)

    except EOFError:
        break

    except:
        break

'''
Comment:

현제 코드에서는 EOFError가 발생할 때와 그 외의 에러가 발생할 때 모두 break로 처리하고 있는데,
EOFError만 처리하도록 except를 좁히는 것이 좋습니다.

또한, if not line: break로만 처리하면 EOFError를 명시적으로 처리하지 않아도 되므로,
코드가 더 간결해질 수 있습니다.

둘 중 하나의 방법을 선택하여 코드를 수정해도 될 것 같습니다.
'''