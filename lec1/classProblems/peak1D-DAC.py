import os 
import sys
import math
import time

start_time = time.time()

#n = int(input("Enter number of elements : "))

arr=[]

for i in range(0, 1000000):
	#ele = int(input())
	ele = i
	arr.append(ele)

def peak(a,n):
	tmp=a
	#print(tmp)
	#print("Peak fun called with arr "+str(arr)+"  n is "+str(n))
	if ( n>1 and tmp[math.floor(n/2)] < tmp[math.floor(n/2)-1] ):
		tmp=tmp[:math.floor(n/2)]
		peak(tmp,len(tmp))
	elif( n>2 and tmp[math.floor(n/2)] < tmp[math.floor(n/2)+1] ):
			tmp=tmp[math.floor(n/2):]
			peak(tmp,len(tmp))
	else:
		print("Peak  Value is "+str(tmp[math.floor(n/2)]))
		print("--- %s seconds ---" % (time.time() - start_time))

peak(arr,len(arr))
