



def product(target_product,test_list):
    print("trong dãy số ",test_list )
    print("có các cặp số phân biệt sau có tích là ",target_product)
    for i,j in enumerate(test_list):
        t = test_list[i+1:]
        # print(t)
        for k, v in enumerate(t):
            s = j * v
            if s == target_product:
                print(j,v, end = ' ')
                print("tại vị trí ", i+1, "và", i+k+1+1)
