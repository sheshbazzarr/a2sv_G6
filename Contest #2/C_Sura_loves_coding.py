a = int(input())
word = input().strip()
new_word = []
for i in range(a - 1, -1, -1):
    mid = len(new_word) // 2
    new_word.insert(mid, word[i])
print(''.join(new_word))

