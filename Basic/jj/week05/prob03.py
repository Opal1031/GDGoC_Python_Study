def solution(s):
    answer = False
    s_dict={}
    
    s=s.lower()
    for char in s:
        if char=="p" or char=="y":
            s_dict[char]=s_dict.get(char,0)+1
    
    if (s_dict.get("p",0)==s_dict.get("y",0)):
        answer= True

    return answer

'''
Comment:

[이번 주제와의 연관성]
이번 주제인 '딕셔너리 활용'에 부합하는 풀이입니다.
딕셔너리를 통해 특정 문자의 등장 횟수를 효율적으로 셀 수 있습니다.
'''