list1=['a','e','i','o','u']

while True:
    sen=input().lower()
    if sen == '#':
        break
        
    count=0
    
    for i in list1:
        for j in sen:
            if i==j:
                count += 1
            
    print(count)