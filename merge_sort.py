def merge(left,right):
  result=[]
  i_left=0
  i_right=0
  while i_left<len(left) and i_right<len(right):
    if left[i_left]<right[i_right]:
      result.append(left[i_left])
      i_left+=1
    elif left[i_left]==right[i_right]:
      result.append(left[i_left])
      result.append(right[i_right])
      i_left+=1
      i_right+=1
    else:
      result.append(right[i_right])
      i_right+=1

  return result+left[i_left:]+right[i_right:]

def merge_sort(arr):
  if len(arr)<=1:
    return arr
  mid = len(arr)//2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])
  return merge(left,right)
  

if __name__ == "__main__":
  arr=[3,5,2,7,9,1,8,4,0]
  result=merge_sort(arr)
  print(result)
  
  