import sys

number = int(sys.stdin.readline())

for _ in range(number):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

'''
Comment:

Good!

sys 모듈을 사용할 때,
input = sys.stdin.readline
이렇게 입력받는 함수를 재정의해서 사용하는 방법도 있습니다.
'''