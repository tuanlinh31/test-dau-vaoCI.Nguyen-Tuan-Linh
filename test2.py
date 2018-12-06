



def product(target_product,test_list):

    result=[]
    for i,j in enumerate(test_list):
        t = test_list[i+1:]
        # print(t)
        for l, v in enumerate(t):
            s = j * v
            if s == target_product:  
                # result.append(j)
                # result.append(v)
                # result.append(i)
                print(j,v,"có vị trí là:", i+1, "và", i+l+2)
                # print("tại vị trí ", i+1, "và", i+l+2)      
    return result


def remove_duplicate(x):
    final_result = []
    for m in x:
        if m not in final_result:
            final_result.append(m)
        else:
            final_result.append(0)
    return final_result


