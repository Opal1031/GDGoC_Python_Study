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