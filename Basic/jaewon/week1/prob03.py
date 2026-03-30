play = True

sentence = [ ]

while play:
    line = input("")

    if line == "#":
        play = False
    else:
        sentence.append(line)

for sentences in sentence:
    a = sentences.count("a")
    b = sentences.count("i")
    c = sentences.count("u")
    d = sentences.count("e")
    e = sentences.count("o")

    print(a+b+c+d+e)

'''
Comment:

대문자 모음도 포함하여 개수를 세는 것이 좋습니다.

play 변수를 사용할 필요 없이, while True: 루프를 사용하여 입력을 계속 받을 수 있습니다.
입력이 "#"인 경우 break 문을 사용하여 루프를 종료할 수 있습니다.

해당 형태로 Flag를 사용하는 문제들도 존재하니, Flag 변수를 사용하는 방법도 익혀두는 것은 좋습니다.
'''