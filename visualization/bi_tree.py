a =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15]

def childNodes(i):
     return (2*i)+1, (2*i)+2

def traversed(a, i=0, d = 0):
    if i >= len(a):
        return 
    l, r =  childNodes(i)
    traversed(a, r, d = d+1)
    print("   "*d + str(a[i]))
    traversed(a, l, d = d+1)

traversed(a)