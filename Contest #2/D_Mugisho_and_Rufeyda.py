n, t = map(int, input().split())

start = 10 ** (n - 1)
# Largest n-digit number
end = 10**n - 1

# Find the smallest n-digit number divisible by t
if start % t == 0:
    print(start)
else:
    # Calculate the next number divisible by t
    candidate = start + (t - (start % t))
    if candidate <= end:
        print(candidate)
    else:
        print(-1)