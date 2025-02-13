n, t = map(int, input().split())
 
x0 = 10 ** (n - 1)
# Largest n-digit number
X = 10**n - 1
 
# Find the smallest n-digit number divisible by t
if x0 % t == 0:
    print(x0)
else:
    # Calculate the next number divisible by t
    y = x0 + (t - (x0 % t))
    if y <= X:
        print(y)
    else:
        print(-1)