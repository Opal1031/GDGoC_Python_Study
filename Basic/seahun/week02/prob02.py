while True:
    try:
        print(input())

    except EOFError:
        break

'''
Comment:

EOFError를 이용해서 입력이 끝날 때까지 반복하는 방식으로 잘 구현했습니다.
'''