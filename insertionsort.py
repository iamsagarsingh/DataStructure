a= [8,1,2,10,6,3,5,4]
print("Unsorted Array:",a)
for i in range(1,len(a)):
	temp = a[i]
	j = i -1
	while(j>=0 and a[j] > temp):
		a[j+1] = a[j]
		j -=1
	a[j+1] = temp

print("Sorted array:",a)
