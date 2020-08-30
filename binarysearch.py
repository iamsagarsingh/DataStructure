arr = [1,5,7,9,23,56,89,99,100,105]
s = 100
lft = 0
rgt = len(arr)
while(lft<rgt):
	mid = (lft+rgt)//2
	if arr[mid] == s:
		print("Element found at:",mid)
		break
	elif arr[mid] > s:
		rgt = mid
	else:
		lft = mid+1
	if lft == rgt and arr[mid] != s:
		print("Element not found")


