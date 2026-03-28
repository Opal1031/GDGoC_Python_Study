list1=['a','e','i','o','u']

while True:
    sen=input().lower()

    if sen == '#':
        break
        
    count=0
    
    for i in list1:
        for j in sen:
            if i==j:
                count += 1
            
    print(count)

'''
Comment:

모음 리스트를 문자열로 표현하는 것이 더 간결합니다.
예를 들어, vowels = "aeiouAEIOU"로 표현하면, 리스트 대신 문자열로 모음을 관리할 수 있습니다.

대소문자를 구분하지 않도록 입력을 소문자로 변환하는 것은 좋은 방법입니다.
'''