import math

n, m, a = map(int, input().split())
flagstones = math.ceil(n / a) * math.ceil(m / a)
print(flagstones)