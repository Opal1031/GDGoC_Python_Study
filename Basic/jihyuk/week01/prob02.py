a, b = map(int, input().split())

a = int(a)
b = int(b)

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")

'''
Comment:

map 함수를 사용하여 입력받은 문자열을 이미 int형으로 변환하였습니다.
따라서, a와 b는 이미 정수형이므로, 다시 int()로 변환할 필요가 없습니다.
'''