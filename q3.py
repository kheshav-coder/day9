test_list=["india","is","best"]
subs_dict={"india":[5,6,7,8,9,10],"is":[7,4,2]}
k=0

def out(test_list,subs_dict,k):
    for i in range(len(test_list)):
        if test_list[i] in subs_dict:
            test_list[i]=subs_dict[test_list[i]][k]
    return test_list

print(out(test_list,subs_dict,k))