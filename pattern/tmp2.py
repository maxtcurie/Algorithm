s2='#'+'#'.join(s)+'#'
n=len(s2)

p_rad=[0]*n  
r=center=0

for i in range(n):
    #
    r_tmp=2*center-i 
    if i<r:
        p_rad[i] =min(l-i,p_rad[r_tmp])