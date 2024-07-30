
def pivot(arr,l,r):
  piovot=arr[r]
  curr=l

  for i in range(l,r-1):
    if arr[i]<piovot:
      arr[i],arr[curr]=arr[curr],arr[i]
      curr+=1
  print(arr)
  print(len(arr))

  print(curr)
  arr[curr],arr[r]=arr[r],arr[curr]

  return curr

def median(arr,k):
  l=0
  r=len(arr)-1
  pos=-1

  while pos<=k:
    curr=pivot(arr,l,r)
    if curr>k:
      r=curr-1
    elif curr<k:
      l=curr+1
    else:
      return arr[curr]
  
  return arr[curr]


if __name__ == "__main__":
  arr=[3,5,2,7,9,1,8,4,0]
  result=median(arr,len(arr)//2)
  print(arr)
  print(result)
  
  