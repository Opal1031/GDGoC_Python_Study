q = input("").split(" ")

a, b = map(int, q)

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")