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

midi=int((len(arr[0])/2)-1)
midj=int((len(arr)/2)-1)


def peak2D(mi,mj):
    up,down,right,left=0,0,0,0

    if ( mj > 0 ):
        left=arr[mi][mj-1]
    if( mi != len(arr)-1 ):
        down=arr[mi+1][mj]
    if( mj != len(arr[0])-1):
        right=arr[mi][mj+1]
    if( mi != 0 ):
        up=arr[mi-1][mj]

    if( left>down and left>right and left>up ):
        peak2D(mi,mj-1)
    elif( down>left and down>right and down>up ):
        peak2D(mi+1,mj)
    elif( right>left and right>down and left>up ):
        peak2D(mi,mj+1)
    else:
        print("2D Peak is "+str(arr[mi][mj]))
        print("--- %s seconds ---" % (time.time() - start_time))

peak2D(midi,midj)
    
