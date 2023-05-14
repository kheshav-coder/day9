s="the quick brown fox jumps over the lazy dog"
def check(s):
    l=s.split(" ")
    k=""
    for i in l:
        k+=i
    x=0
    d={}
    for i in k:
        d[i]=x
        x+=1
    return len(d)==26

print(check(s))