#O(n^n)
def fib_cal(n):
    if n<=2:
        return 1
    else:
        return fib_cal(n-1)+fib_cal(n-2)

#O(n)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    else:
        memo[n]=fib_cal(n-1)+fib_cal(n-2)
        return memo[n]

#O(n)
def fib_tab(n):
    list_n=[0]*n
    list_n[:2]=[1,1]
    for i in range(2,n):
        list_n[i]=list_n[i-1]+list_n[i-2]
    return list_n[-1]

import time

n=40

t0=time.time()

print(fib_memo(n)) 
t1=time.time()
print(f'time={t1-t0}')

print(fib_tab(n)) 
t2=time.time()
print(f'time={t2-t1}')

print(fib_cal(n)) 
t3=time.time()
print(f'time={t3-t2}')
