p=['P1','P2','P3']
at=[0,0,0]
bt=[10,5,8]

n=len(p)

ct=[0]*n
tat=[0]*n
wt=[0]*n
done=[0]*n

t=0

for _ in range(n):
    idx=-1
    mn=999

    for i in range(n):
        if not done[i] and bt[i]<mn:
            mn=bt[i]
            idx=i

    t+=bt[idx]
    ct[idx]=t
    done[idx]=1

for i in range(n):
    tat[i]=ct[i]-at[i]
    wt[i]=tat[i]-bt[i]

avg_tat=sum(tat)/n
avg_wt=sum(wt)/n

print("P\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    print(p[i],"\t",
          at[i],"\t",
          bt[i],"\t",
          ct[i],"\t",
          tat[i],"\t",
          wt[i])

print("\nAverage Turnaround Time =",avg_tat)
print("Average Waiting Time =",avg_wt)