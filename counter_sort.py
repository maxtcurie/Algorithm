#n=len(nums)
#m=max(nums)-min(nums)
# O(m+n)
from collections import Counter 

def counter_sort(nums):
    counter=Counter(nums)
    min_h=min(nums)
    max_h=max(nums)
        
    sorted_l=[]
    for i in range(min_h,max_h+1):
        if i in counter:
            sorted_l=sorted_l+[i]*counter[i]

    return sorted_l



if __name__ == "__main__":
  arr=[3,5,2,7,9,1,8,4,0]
  result=counter_sort(arr)
  print(result)