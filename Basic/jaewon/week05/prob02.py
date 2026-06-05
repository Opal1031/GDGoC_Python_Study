def solution(num):
    
    # numbers = {"Even":" ", "Odd"," "}
    numbers = {"Even": " ", "Odd": " "}

    if num % 2 == 1:
        numbers["Odd"] = num
    elif num % 2 == 0:
        numbers["Even"] = num
    
    answer = numbers
    
    return answer

# 원래는 이런 식으로 풀려고 했는데 도저히 for문으로 answer 변수를 적는 로직이 생각이 안나서.... 일단 이 상태로라도 올려봅니다.....
# 웬지 더 쉽게 풀 수 있는 방법이 있을 것 같은데, 

'''
Comment:

[이번 주제와의 연관성]
이번 주제는 '딕셔너리 활용'입니다.
나머지 값에 따라 결과를 매핑하려는 방향 자체는 주제와 잘 맞습니다.

[답변]
- for문이 꼭 필요한 문제는 아닙니다. num % 2의 결과를 바로 딕셔너리 키로 사용하면 됩니다.
- minseo 풀이처럼 parity = {0: 'Even', 1: 'Odd'} 형태로 두고 return parity[num % 2]로 마무리할 수 있습니다.

[보완하면 좋은 점]
- numbers = {"Even":" ", "Odd"," "} 부분은 딕셔너리 문법상 올바르지 않습니다. key:value 형태여야 합니다.
- 이 문제는 value를 저장하기보다 결과 문자열을 바로 반환하는 구조가 더 적합합니다.
'''
