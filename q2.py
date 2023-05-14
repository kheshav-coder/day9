s="hello"
def find(s):
    x=1
    d={}
    for i in s:
        d[i]=x
        x+=1
    return (len(s)-len(d))

print(find(s))
