Numbers=list(map(int,input().split()))
PrefixSum=[]
sum=0
for i in Numbers:
    sum+=i
    PrefixSum.append(sum)
print(*PrefixSum,sep="\t")
