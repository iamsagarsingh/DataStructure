A = [7,6,10,5,9,2,1,15,7,0,1,99,100,43,23,12,65,34,87,97]
print("Unsorted Array:",A)
def partion(arr,lft,rgt):
	pivot = arr[lft]
	start = lft
	end = rgt
	#print(arr,start,end,pivot)
	while(start < end):
		while(arr[start] <= pivot and start < end):
			start +=1
		while(arr[end] > pivot):
			end -=1
		if start < end:
			arr[start],arr[end] = arr[end],arr[start]
	arr[lft],arr[end] = arr[end],arr[lft]
	return end
def quicksort(arr,lft,rgt):
	if lft < rgt:
		loc = partion(arr,lft,rgt)
		quicksort(arr,lft,loc-1)
		quicksort(arr,loc+1,rgt)

quicksort(A,0,len(A)-1)
print("Sorted Array:",A)
