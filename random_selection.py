#rank start from 0
def random_selection(arr,rank):

  mid = len(arr)//2
  pivot_point=arr[mid]

  left=[]
  middle=[]
  right=[]
  
  for i in arr:
    if i<pivot_point:
      left.append(i)
    elif i==pivot_point:
      middle.append(i)
    elif i>pivot_point:
      right.append(i)

  if rank+1 <= len(left):
    return random_selection(left,rank)

  elif len(left) < rank+1 <= len(left)+len(middle):
    return pivot_point

  elif len(left)+len(middle) < rank+1:
    return random_selection(right,rank-len(left)-len(middle))

  

if __name__ == "__main__":
  arr=[3,5,2,7,9,1,8,4,0]

  rank=7
  result=random_selection(arr,rank)

  print(result)
  arr.sort()
  print(arr[rank])



  
  
  