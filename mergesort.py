a = [15,23,16,2,1,0,54,223,431,76,34,98,12,764,3,99,77,55,745,422,854,993]
print("Unsorted Array:",a)
def merge(a,lft,mid,rgt):
	i =  lft
	k = lft
	j = mid+1
	b = [0 for c in range(rgt+1)]
	while(i <= mid and j <= rgt):
		if a[i] < a[j]:
			b[k] = a[i]
			i +=1
		else:
			b[k] = a[j]
			j +=1
		k +=1
	if i > mid:
		while(j <= rgt):
			b[k] = a[j]
			j +=1
			k +=1
	elif j > rgt:
		while(i <= mid):
			b[k] = a[i]
			i+=1
			k +=1
	for _ in range(lft,rgt+1):
		a[_] = b[_]

def mergesort(a,lft,rgt):
	if lft < rgt:
		mid = (lft+rgt)//2
		mergesort(a,lft,mid)
		mergesort(a,mid+1,rgt)
		merge(a,lft,mid,rgt)


mergesort(a,0,len(a)-1)

print("Sorted Array:",a)
