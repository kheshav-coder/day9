c=[chr(i).lower() for i in range(65,91)]

s="paradox"
n=3
def mirror(s,n):
    global c
    k=""
    for i in range(n-1,len(s)):
        k+=list(reversed(c))[c.index(s[i])]
    return s[:n-1]+k

print(mirror(s,n))

