A,B = map(int, input().split(" "))
if A > B :
    print(">")
if A < B :
    print("<")
if A == B :
    print("==")

'''
Comment:

[input().split()]
input().split(" ") → input().split() (권장)
split()은 공백을 자동으로 분리하므로 더 간결합니다.
'''