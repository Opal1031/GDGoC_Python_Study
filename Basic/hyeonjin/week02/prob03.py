import sys
input = sys.stdin.readline

while True:
    try:
        line = input()

        if not line:
            break

        A, B = map(int, line.split())

        print(A + B)

'''
Comment:

현재 코드는 빌드 시 에러가 발생합니다.
try에 대한 except가 없기 때문입니다.

try-except 구문을 사용하여 EOFError가 발생할 때 프로그램이 종료되도록 수정해보세요.
'''