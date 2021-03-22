a=int(input())
b=1
for i in range(0,a):
    for j in range((a-i),0,-1):
        print(" ",end=" ")
    for j in range(0,i):
        print(b,end=" ")
        b+=1
    print()
