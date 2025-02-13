a = int(input())
s = input().strip()
new_word = []
for i in range(a - 1, -1, -1):
    mid = len(new_word) // 2
    new_word.insert(mid, s[i])
print(''.join(new_word))


"""
a = int(input())
word = input().strip()
new_word = []
while a>=0:
    a//=2
    new_word.append(word[a])
    word = word[:a] + word[a+1:]
    a=len(word)-1
print(''.join(new_word[:-1]))

"""
