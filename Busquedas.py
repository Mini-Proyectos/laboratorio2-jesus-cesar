def InsertionSort (a:[int],p:int,r:int):
        j=p
        for j in range(len(a)):
                key=a[j]
                i=j-1
                while i>=p and a[i]>key:
                        a[i+1]=a[i]
                        i-=1
                a[i+1]=key
        return a

