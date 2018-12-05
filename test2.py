



def product(target_product,test_list):
    print("trong dãy số ",test_list )
    print("có các cặp số phân biệt sau có tích là",target_product,":")
    result=[]
    for i,j in enumerate(test_list):
        t = test_list[i+1:]
        # print(t)
        for k, v in enumerate(t):
            s = j * v
            if s == target_product:  
                result.append(j)
                result.append(v)
                # print(j,v, end = ' ')
                # print("tại vị trí ", i+1, "và", i+k+2)      
    return result


def remove_duplicate(x):
    final_result = []
    for m in x:
        if m not in final_result:
            final_result.append(m)
    return final_result


