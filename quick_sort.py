def pivot(arr):
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
  return left, middle, right

def quick_sort(arr):
  if len(arr)<=1:
    return arr
  left, middle, right = pivot(arr)
  return quick_sort(left) + middle + quick_sort(right)
  

if __name__ == "__main__":
  arr=[3,5,2,7,9,1,8,4,0]
  result=quick_sort(arr)
  print(result)
  
  