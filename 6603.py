import sys
from itertools import combinations

while True:
    arr=list(map(int,sys.stdin.readline().split()))
    if(arr[0]==0):
        break
    S=arr[1:]
    for i in combinations(S,6):
        # for j in range(6):
             # if(j==5):
             #     print(i[j],end='\n')
             #     break
             # print(i[j],end=' ')
        print(*i)
    print()