
a = int(input())
for _ in range(a):
    sz = int(input())
    word = input().strip()
    l = 0
    r = sz - 1
    while l < sz and word[l] == 'W':
        l += 1
  
    while r >= 0 and word[r] == 'W':
        r -= 1
    if l > r:
        size_ = 0
    else:
        size_ = r - l + 1
    
    print(size_)