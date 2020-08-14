arr = [1,5,7,9,23,56,89,99,100,105]  # sample array
s = 1000  # put the element you want to search.
lft = 0  # left index
rgt = len(arr) #right index
while(lft<rgt):
	mid = (lft+rgt)//2
	if arr[mid] == s:
		print("Element found at:",mid)
		break  #search over element found
	elif arr[mid] > s:
		rgt = mid  #altering the indexes
	else:
		lft = mid+1
	if lft == rgt and arr[mid] != s:
		print("Element not found")


