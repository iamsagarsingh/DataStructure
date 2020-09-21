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
