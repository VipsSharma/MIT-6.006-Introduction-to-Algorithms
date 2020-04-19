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

def maximaRow(a,col):
    row=0
    for i in range(0,len(a)-1):
        if( a[i][col] > a[i+1][col]):
            row=i
        else:
            row=i+1
    return row

def peak(a):

    midc=int(len(a[0])/2)-1

    if( midc < 0 ):
        row=maximaRow(a,0)
        print("Peak is "+str(a[row][0]))
        print("--- %s seconds ---" % (time.time() - start_time))
        sys.exit()

    row=maximaRow(a,midc)

    if( midc > 0 and a[row][midc-1] > a[row][midc] ):
        narr=[]
        for i in range(0,len(a)):
            tmp=[]
            for j in range(0,midc):
                tmp.append(a[i][j])
            narr.append(tmp)
        peak(narr)

    elif( a[row][midc+1] > a[row][midc] ):
        narr=[]
        for i in range(0,len(a)):
            tmp=[]
            for j in range(midc+1,len(a[0])):
                tmp.append(a[i][j])
            narr.append(tmp)
        peak(narr)

    else:
        print("Peak is "+str(a[row][midc]))
        print("--- %s seconds ---" % (time.time() - start_time))

peak(arr)
    