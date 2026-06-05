def solution(s):
    
    ss = {"a" : s.count("P") + s.count("p") , "b" : s.count( "Y" ) + s.count( "y" ) }
    if ss["a"]==ss["b"]:
        return True
    else:
        return False

'''
Comment:

[이번 주제와의 연관성]
이번 주제인 '딕셔너리 활용'에 부합하는 풀이입니다.
문자별 개수를 딕셔너리에 담아 비교하는 방식이라 의도가 잘 보입니다.

[답변]
- s.count("P") + s.count("p")처럼 대소문자를 각각 세는 방식도 맞습니다.
- 다만 문자열을 한 번 lower()로 통일한 뒤 세면 더 간단해집니다.
- minseo 풀이처럼 counts[ch] = counts.get(ch, 0) + 1 방식으로 누적하면 딕셔너리 활용이 더 자연스럽게 드러납니다.

[보완하면 좋은 점]
- ss["a"], ss["b"]처럼 의미가 덜 드러나는 키보다는 p_count, y_count 같은 이름이 더 읽기 쉽습니다.
- 마지막은 return ss["a"] == ss["b"]처럼 바로 반환해도 충분합니다.
'''