# DataStructure

## Pseudo Codes
* Push & Pop Operation in Stack
```
set max
set top = -1
function push()
  if top == max-1     [check for overflow]
    write "Overflow!!"
    return
  else
    set top to top +1
    set arr[top] = data
function pop()
  if top == -1      [Check for underflow]
    write "Underflow!!"
    return
  else
    set arr[top] = 0
    set top to top -1
```
* Bubble Sort
```
function bubblesort(a)
  for i =0 to len(a):
    for j=0 to len(a)-1:
      if a[j] > a[j+1]:
        swap(a[j],a[j+1])
      end if
    end for
 end for
```
* Binary Search
```
function binarysearch(a,e)
set left to 0
set right to len(a)
while left < right do
  set mid to (left+right)//2
  if a[mid] == e
    write "element e found at mid"
    break
  else if a[mid] > e
    set right = mid
  else
    set left = mid +1
  if left == right and arr[mid] != e
    write "Element e does not exit"
end while
```
* Insertion Sort
```
function insertion(a)
for i =1 to len(a)
  set temp to a[i]
  set j to i-1
  while j>0 and a[j] > temp, do
    a[j+1] = a[j]
    j--;
  end while
  set a[j+1] to temp
end for
```
