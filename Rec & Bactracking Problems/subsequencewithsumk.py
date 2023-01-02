A = [1,2,1,5,6]
k = 11
count = 0
def findsubk(ind,ds,s):
    global count
    if ind == len(A):
        if s == k:
            print(ds)
            count+=1
        return

    ds.append(A[ind])
    s+=A[ind]
    findsubk(ind+1, ds, s)
    ds.remove(A[ind])
    s-=A[ind]
    findsubk(ind+1, ds, s)

findsubk(0, [], 0)

print(count)