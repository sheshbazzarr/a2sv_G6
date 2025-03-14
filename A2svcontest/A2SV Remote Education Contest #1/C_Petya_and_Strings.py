# a=input()
# b=input()
# if a.upper()==b.upper():
#     print(0)
# elif a.upper()<b.upper():
#     print(-1)
# else:
#     print(1)

a = input().casefold()
b = input().casefold()

print((a > b) - (a < b))

"""  
Uses .casefold() instead of .upper()
.casefold() is better for case-insensitive comparisons since it handles special characters more accurately than .upper().
Reduces redundant function calls
Instead of calling .upper() twice on each string, we store the transformed values once.
Uses a compact comparison
(a > b) - (a < b) directly calculates the result in one line, making the code cleaner and avoiding multiple if-elif-else conditions.
"""