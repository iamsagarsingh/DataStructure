A = [3,2,1]

def printSubSequences(index,arr):
    if index >= 3:
        print(arr)
        return

    arr.append(A[index])
    printSubSequences(index+1, arr)

    arr.remove(A[index])
    printSubSequences(index+1, arr)



printSubSequences(0, [])


