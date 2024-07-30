def can_sum(a,k):
    sum_pre=0
    sum_dict={0:-1}
    for i in range(len(a)):
        sum_tmp=sum_pre+a[i]
        sum_pre=sum_tmp

        if sum_tmp-k in sum_dict:
            return True
        
        sum_dict[sum_tmp]=i

    return False



a=[2,4,4,5,2]
k=6
print(can_sum(a,k)) 