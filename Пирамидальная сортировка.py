from array import array
import sys
sys.setrecursionlimit(1000000)

def collect(arr, n, i):
    the_biggest = i
    l = 2*i+1
    r = 2*i+2
    if l < n and arr[l] > arr[the_biggest]:
        the_biggest = l
    if r < n and arr[r] > arr[the_biggest]:
        the_biggest = r
    if the_biggest != i:
        arr[i],arr[the_biggest] = arr[the_biggest],arr[i]
        collect(arr, n, the_biggest)

def PyramidSort(arr,n):
    for i in range(n//2-1,-1,-1):
        collect(arr,n,i)
    for i in range(n-1,-1,-1):
        arr[0], arr[i] = arr[i], arr[0]
        collect(arr,i,0)

n = int(input())
Arr = array('i',[int(i)-1 for i in input().split()])
PyramidSort(Arr,n)
Arr = [i+1 for i in Arr]
print(*Arr)
