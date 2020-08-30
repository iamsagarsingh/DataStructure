#a = [50,11,12,10,9,5,18,0,2,55,1]
#import random
#n = 1000
#a = [random.randint(0,1000) for i in range(n)]
a = [99,32,11,5,6,1,9,65,34]
print("Unsorted Array: ",a)
for i in range(len(a)):
	minind = i
	for j in range(i+1,len(a)):
		if a[j] < a[minind]:
			minind = j
	a[i],a[minind] = a[minind],a[i]

print("Sorted Array:",a)
print("Time Complexity: O(n^2)")
