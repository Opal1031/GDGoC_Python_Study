import sys

number = int(sys.stdin.readline())

for i in range(1,number+1):
    print(i*"*")
    i += 1

'''
Comment:

for문에서 i는 자동으로 증가하기 때문에, 따로 증가시켜줄 필요가 없습니다.

또한, "문자열 * 변수" 의 형태로 작성하는 것이 더 간결하고 가독성이 좋은 편 입니다.
'''