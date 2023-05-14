a={1:"apple",2:"banana",3:"orange",4:"strawberry"}
b={5:"pineapple",6:"guvava",7:"jackfruit"}

def add(a,b):
    return {**a,**b}

print(add(a,b))