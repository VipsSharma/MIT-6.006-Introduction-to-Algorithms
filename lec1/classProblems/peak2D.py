import os
import sys
import time 

start_time = time.time()

arr=[]
row = int(input("Enter Number of Rows in 2D Array : "))
col = int(input("Enter Number of Columns in 2D Array : "))

for i in range(0,row):
    tmp=[]
    for j in range(0,col):
        tmp.append(int(input()))
    arr.append(tmp)

print()
for i in range(0,row):
    for j in range(0,col):
        print("{:<5}".format(arr[i][j]),end=" ")
    print()
print()

midi=int((len(arr[0])/2)-1)
midj=int((len(arr)/2)-1)


def peak2D(mi,mj):
    if ( mj > 0 and arr[mi][mj-1] > arr[mi][mj]):
            peak2D(mi,mj-1)
    
    elif( mi != len(arr)-1 and arr[mi+1][mj] > arr[mi][mj] ):
            peak2D(mi+1,mj)
    
    elif( mj != len(arr[0])-1 and arr[mi][mj+1] > arr[mi][mj] ):
            peak2D(mi,mj+1)

    elif( mi != 0 and arr[mi-1][mj] > arr[mi][mj] ):
            peak2D(mi-1,mj)

    else:
        print("2D Peak is "+str(arr[mi][mj]))
        print("--- %s seconds ---" % (time.time() - start_time))

peak2D(midi,midj)
    
