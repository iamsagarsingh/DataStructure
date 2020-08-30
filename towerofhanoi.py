n = 4 
def towerofhanoi(n,s,a,d): 
	if n>=1:
		towerofhanoi(n-1,s,d,a)
		print("disk {}. {} -> {}".format(n,s,d))
		towerofhanoi(n-1,a,s,d)


towerofhanoi(n,'A','B','C')
