while True:
    try:
        a,b=map(int,input().split())
        print(a+b)

    except:
        break

'''
Comment:

except 구문에서, 어떤 예외가 발생할지 명확히 하는 것이 좋습니다.
예를 들어, EOFError가 발생할 때 반복문을 종료하도록 하는 것이 좋습니다

except EOFError:
    break
'''