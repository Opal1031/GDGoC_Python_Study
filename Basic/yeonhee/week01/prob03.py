vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
num = 0
while True:
    sent = input()
    if sent=='#' :
        break
    for i in sent:
        if i in vowel:
            num += 1 

    print(num)

'''
Comment:

Good!
'''