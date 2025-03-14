n=input()
l=len(n)
change=n[0].upper()
print(change+n[1:l+1])



n = input()
print(n[0].upper() + n[1:])
"""" 
Avoids using len(n): Since slicing already handles out-of-bounds cases, n[1:] works directly.
Removes redundant variable: The change variable is unnecessary.
Simplifies slicing: n[1:l+1] is equivalent to n[1:].
"""

# more effient code 
n=input()
print(n[:1].upper()+n[1:])
"""  
Why is this efficient?
n[:1] instead of n[0]: This avoids an IndexError if n is empty.
Concatenation remains minimal: We modify only the first character and keep the rest unchanged.
String slicing (n[1:]) is already optimized in Python: It doesn't create unnecessary copies beyond what's needed.
"""