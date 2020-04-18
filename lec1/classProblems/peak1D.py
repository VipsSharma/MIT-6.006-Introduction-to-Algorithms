import os
import sys
import time


start_time = time.time()

n = int(input("Enter number of elements : ")) 
arr = []


for i in range(0, n): 
	ele = int(input()) 
	arr.append(ele)


for item in enumerate(arr):
	if( item[0] == 0 ):
		if( len(arr) > 1):
			if( arr[1] < arr[0] ):
				print("1D array has a Peak at "+str(item[0])+" Index, Peak is "+str(item[1]))
				print("--- %s seconds ---" % (time.time() - start_time))
				sys.exit()
			else:
				continue
		else:
			print("1D array has a Peak at "+str(item[0])+" Index, Peak is "+str(item[1]))
			print("--- %s seconds ---" % (time.time() - start_time))
			sys.exit()
	elif( len(arr) > item[0] + 1 ):
		if( item[1] > arr[item[0] -1] and item[1] > arr[item[0] +1] ):
			print("1D array has a Peak at "+str(item[0])+" Index, Peak is "+str(item[1]))
			print("--- %s seconds ---" % (time.time() - start_time))
			sys.exit()
		else:
			continue
	else:
		if( item[1] > arr[item[0] -1] ):
			print("1D array has a Peak at "+str(item[0])+" Index, Peak is "+str(item[1]))
			print("--- %s seconds ---" % (time.time() - start_time))
			sys.exit()
		else:		
			print("No Peak Exists in Given Array")
			print("--- %s seconds ---" % (time.time() - start_time))

