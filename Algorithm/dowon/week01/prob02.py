import sys
import math
input = sys.stdin.readline

M, N=map(int, input().split())

for i in range(M, N+1):
    if i < 2:
        continue
    
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            break
    
    else:
        print(i)

'''
Comment:

소수를 구하는 방법은 여러 가지가 있지만, 가장 효율적인 방법 중 하나는 에라토스테네스의 체입니다.
이 방법은 2부터 N까지의 모든 수를 나열하고, 2부터 시작하여 각 소수의 배수를 제거하는 방식으로 작동합니다.

소수 판별을 위해 i의 제곱근까지만 검사하면, 큰 수에 대해서도 효율적으로 소수를 판별할 수 있습니다.
'''