import sys
from itertools import permutations
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()

max_sum=0
for i in permutations(arr):
    sum=0
    for j in range(n-1):
        sum+=abs(i[j]-i[j+1])
    max_sum=max(max_sum,sum)

print(max_sum)