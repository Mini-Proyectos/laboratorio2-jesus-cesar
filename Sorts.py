def MergeSort(A:[int],p:int,r:int):
    if p<r-1:
        
        q=(p+r)//2
        
        MergeSort(A,p,q)
        
        MergeSort(A,q,r)
        
        Merge(A,p,q,r)

    return A

def Merge(A:[int],ini:int,mit:int,fin:int):


    L,R=[],[]

    for i in range(ini,mit):
        L.append(A[i])
    
    for i in range(mit,fin):
        R.append(A[i])

    L.append(float('inf'))
    R.append(float('inf'))

    i,j=0,0

    for k in range (ini,fin):
        if L[i]<=R[j]:
            A[k]=L[i]
            i+=1
    
        else:
            A[k]=R[j]
            j+=1

    return A 