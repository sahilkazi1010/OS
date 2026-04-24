# Priority Scheduling Algorithm (Non-Preemptive)

p = ['P1', 'P2', 'P3', 'P4', 'P5']

at = [0, 2, 6, 7, 13]

bt = [4, 16, 12, 8, 2]

pr = [2,1,3,2,1 ]

n = len(p)

ct = [0] * n

tat = [0] * n

wt = [0] * n

done = [0] * n

t = 0

for _ in range(n):

    idx = -1

    mn = 999

    # Find process with highest priority
    for i in range(n):

        if not done[i] and pr[i] < mn:

            mn = pr[i]

            idx = i

    # Execute process
    t = t + bt[idx]

    ct[idx] = t

    done[idx] = 1

# Calculate TAT and WT
for i in range(n):

    tat[i] = ct[i] - at[i]

    wt[i] = tat[i] - bt[i]

# Display Output
print("P\tAT\tBT\tPR\tCT\tTAT\tWT")

for i in range(n):

    print(p[i], "\t",
          at[i], "\t",
          bt[i], "\t",
          pr[i], "\t",
          ct[i], "\t",
          tat[i], "\t",
          wt[i])