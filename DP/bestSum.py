def how_sum(a,k,memo={}):
    if k in memo:
        return memo[k]

    if k==0:
        return []
    elif k<0:
        return None
    

    for i in a:
        res=how_sum(a,k-i)
        memo[k-i]=res

        if res!=None: 
            return res+[i]

    return None
        



a=[2,4,4,5,2]
k=200
print(how_sum(a,k)) 