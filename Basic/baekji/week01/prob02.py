A,B=input().split()
A=int(A)
B=int(B)
if B<A:
  print(">")
elif A<B:
  print("<")
else:
  print("==")