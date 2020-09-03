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
