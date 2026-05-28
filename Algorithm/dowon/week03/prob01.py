def ans(s):
    s=s.lower()
    return s.count('p')==s.count('y')

'''
Good!

s.lower()을 여러 번 호출하는 것보다, 한 번만 호출해서 소문자로 변환한 문자열을 변수에 저장하는 것이 효율적입니다.
이렇게 하면 코드가 더 깔끔해지고, 성능도 향상됩니다.
'''