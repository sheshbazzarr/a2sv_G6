t=int(input())
for _ in range(t):
    I=int(input())
    a=I//4
    b=I%4
    c=b//2
    print(a+c)






t=int(input())
for _ in range(t):
    I=int(input())
    a=I/4
    b=I/2
    if a%2==0 and a%4!=0:
        cnt=a/2
        print(cnt)
    if a%2==0 and a%4!=0:
        cnt=a//4
        cnt+=a%4
        print(cnt)