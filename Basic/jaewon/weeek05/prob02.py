def solution(num):
    
    numbers = {"Even":" ", "Odd"," "}
    if num % 2 == 1:
        numbers["Odd"] = num
    elif num % 2 == 0:
        numbers["Even"] = num
    
    answer = numbers
    
    return answer

# 원래는 이런 식으로 풀려고 했는데 도저히 for문으로 answer 변수를 적는 로직이 생각이 안나서.... 일단 이 상태로라도 올려봅니다.....
# 웬지 더 쉽게 풀 수 있는 방법이 있을 것 같은데, 
