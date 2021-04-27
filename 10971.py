import sys
from itertools import permutations

n=int(sys.stdin.readline())
cost=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]


arr=[i for i in range(n)]

min_cost=n*1000000+1
for i in permutations(arr):
    result=0
    for j in range(n):
        if(j==n-1):#마지막도시
            n1=i[j]
            n2=i[0]
            if cost[n1][n2]==0:
                break
            else:
                result+=cost[n1][n2]
                min_cost=min(min_cost,result)
        else:
            n1 = i[j]
            n2 = i[j + 1]
            if cost[n1][n2]==0:
                break
            else:
                result+=cost[n1][n2]

print(min_cost)
