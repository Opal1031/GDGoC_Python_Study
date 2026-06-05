grade=input()
if grade[0]=="A":
    score=4.0
elif grade[0]=="B":
    score=3.0
elif grade[0]=="C":
    score=2.0
elif grade[0]=="D":
    score=1.0
else:
    score=0.0

if len(grade)>1:
    if grade[1]=="+":
        score+=0.3

    elif grade[1]=="-":
        score-=0.3

print(score)


# import sys
# grade=input()
# if grade[0]=="A":
#     score=4.0
# elif grade[0]=="B":
#     score=3.0
# elif grade[0]=="C":
#     score=2.0
# elif grade[0]=="D":
#     score=1.0
# else:
#     print(0.0)
#     sys.exit()

# if len(grade)>1:
#     if grade[1]=="+":
#         score+=0.3
#     elif grade[1]=="-":
#         score-=0.3

# print(score)

'''
Comment:

딕셔너리를 사용하여 학점과 점수를 매핑하는 것이 더 효율적입니다.
예를 들어, dic = {'A+':'4.3', 'A0':'4.0', 'A-':'3.7', ...}와 같이 딕셔너리를 정의한 후, 입력된 학점에 해당하는 점수를 출력할 수 있습니다.
'''