A,B=input().split()

A=int(A)
B=int(B)

if B<A:
  print(">")
elif A<B:
  print("<")
else:
  print("==")

'''
Comment:

문제 풀이에는 이상이 업으나, A와 B를 비교할 때, A와 B의 순서를 바꿔서 비교하는 것이 더 직관적입니다.
예를 들어, A와 B를 비교할 때, A가 B보다 크면 ">"를 출력하는 것이 더 자연스럽습니다.
'''