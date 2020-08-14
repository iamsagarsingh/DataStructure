n = 4 
def towerofhanoi(n,s,a,d): #recurisve function
	if n>=1:
		towerofhanoi(n-1,s,d,a)
		print("disk {}. {} -> {}".format(n,s,d)) #this statement exec when n==0
		towerofhanoi(n-1,a,s,d)

#function Calling.
towerofhanoi(n,'A','B','C')
