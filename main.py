'''def getmonth():
    x = int(input())
    month = {1:"january", 2:"february", 3:"march",4:"april", 5:"may", 6:"june",7:"july",8:"august",9:"september", 10: "october", 11:"november",12:"december"}

    if x in month:
        print(month[x])
    else:
        print("Invalid Number")
getmonth()
'''
'''def line():
    x = input("Enter Your Word: ")
    words = x.split()
    cap_word=[word.capitalize() for word in words]
    return ''.join(cap_word)
line()
'''
x=alan
y=joseph
z=alice
a=input()
b=input()
j= [x,y,z]
age = int(input())
m = male
f = female
if a in j:
    print(x,"is a",m,'with age',age)
elif b in j:
    print(y,"is a",m,"with age",age)
else:
    print("she's a",f)
