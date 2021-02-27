n = int(input())
maxx = 0
dummy_list=[]
for i in range(n):
    inp = list(map(int,input().split(" ")))
    sums = sum(inp)
    if sums > maxx:
        maxx = sums
        dummy_list = inp
print(maxx)
print(dummy_list)
