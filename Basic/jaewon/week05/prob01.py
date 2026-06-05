def solution(numbers):
    p = {i:0 for i in range(10)}
    for number in numbers:
        if 0 <= number <= 9:
            p[number] += 1
            #형 그런데 왜 여기에 p뒤에 [number] 붙여줘야하는지 이해가 잘 안가요..;;; -> 개인적인 생각: 에러메세지가 딕셔너리에는 사칙연산이 불가능하다고 했고 number의 값들이 p 안의 key 값들로 있으니까 그리고 결국에는 value 값들을 올려줘야하니까 p의 값을 호출해줘야하니까 [number]를 붙인거네요.... 질문 하다가 보니까 깨달아버림.. ㅋㅋ
        else:
            p[number] = 0
    answer = sum(filter(lambda x: p[x] == 0, p.keys()))
    
    #그냥 저번에 쓴 람다 써봤는데 이렇게 쓰는 거 맞나요...? 원래는 answer = sum(p.values(), if p[number] != 0) 이랬는데 오류나서 바꿔서 썼어서 filter는 람다 AI한테 문법 물어보다가 추천해줘서 넣어봤어요.
    
    return answer

'''
Comment:

[이번 주제와의 연관성]
이번 주제인 '딕셔너리 활용'에 부합하는 풀이입니다.
딕셔너리를 통해 0부터 9까지의 등장 여부를 관리하고, 등장하지 않은 숫자만 골라 합산하는 흐름이 잘 드러납니다.

[답변]
- p[number]처럼 대괄호로 접근하는 이유는 딕셔너리의 key에 해당하는 값을 읽거나 수정하기 위해서입니다.
- p[number] += 1은 key가 number인 항목의 value를 1 증가시키는 표현입니다.
- filter와 lambda를 함께 쓴 방식도 올바릅니다. 조건에 맞는 key만 걸러서 더하는 구조라 충분히 자연스럽습니다.

[보완하면 좋은 점]
- 현재 코드에는 10보다 큰 수에 대해 p[number] = 0을 넣고 있는데, 문제 조건상 보통 0~9만 들어오므로 없어도 됩니다.
- answer = sum(filter(...)) 방식은 가능하지만, minseo 풀이처럼 딕셔너리 전체를 순회하며 0인 값의 key를 더하는 방식도 더 읽기 쉽습니다.
'''