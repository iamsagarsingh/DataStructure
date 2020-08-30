a = [6,5,2,9,7,1,3,4,8,0]
print("Unsorted array:",a)
swaps = 0
for i in range(len(a)):
	for j in range(len(a)-1):
		if a[j] > a[j+1]:
			a[j],a[j+1] = a[j+1],a[j]
			swaps +=1
print("Sorted Array:",a)
print("No of swaps performed:",swaps)

