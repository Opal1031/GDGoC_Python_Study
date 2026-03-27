str="aeiouAEIOU"
while True:
    words=input()
    if words=="#":
        break
    count=0
    for i in words:
        if i in str:
            count+=1
    print(count)
    


# str="aeiou"
# while True:
#     words=input()
#     if words=="#":
#         break
#     count=0
#     for i in words:
#         if i.lower() in str:
#             count+=1
#     print(count)



# def count_vowels(string):
#     str="aeiouAEIOU"
#     count=0
#     for i in string:
#         if i in str:
#             count+=1
#     return count

# while True:
#     s=input()
#     if s=="#":
#         break
#     print(count_vowels(s))
    