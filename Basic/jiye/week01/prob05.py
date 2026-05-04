g=str(input())

if g=="A+":
    print("4.3")
elif g=="A0":
    print("4.0")
elif g=="A-":
    print("3.7")
elif g=="B+":
    print("3.3")
elif g=="B0":
    print("3.0")
elif g=="B-":
    print("2.7")
elif g=="C+":
    print("2.3")
elif g=="C0":
    print("2.0")
elif g=="C-":
    print("1.7")
elif g=="D+":
    print("1.3")
elif g=="D0":
    print("1.0")
elif g=="D-":
    print("0.7")
else:
    print("0.0")
    
'''
Comment:

딕셔너리를 사용하여 학점과 점수를 매핑하는 것이 더 효율적입니다.
예를 들어, dic = {'A+':'4.3', 'A0':'4.0', 'A-':'3.7', ...}와 같이 딕셔너리를 정의한 후, 입력된 학점에 해당하는 점수를 출력할 수 있습니다.
'''