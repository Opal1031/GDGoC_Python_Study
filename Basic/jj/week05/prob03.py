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