# making combinations
def binarystring(i,n,arr):
    if i == n:                   # this is the base case
        print(arr)
        return
    else:                        # this is backtracking.
        arr[i] = 0
        binarystring(i+1,n,arr)
        arr[i] = 1
        binarystring(i+1,n,arr)


arr = [0,0,0]
binarystring(0,3,arr)


"""
Complexity: O(n*2^n)
"""
