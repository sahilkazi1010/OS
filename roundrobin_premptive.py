p = ['P1', 'P2', 'P3', 'P4', 'P5']

at = [0, 2, 6, 7, 13]

bt = [4, 16, 12, 8, 2]

q = 4

n = len(p)

rt = bt[:]

ct = [0] * n

tat = [0] * n

wt = [0] * n

t = 0

while sum(rt) > 0:

    for i in range(n):

        if rt[i] > 0:

            x = min(q, rt[i])

            t = t + x

            rt[i] = rt[i] - x

            print(">", p[i], ">",)

            if rt[i] == 0:

                ct[i] = t

# Calculate TAT and WT
for i in range(n):

    tat[i] = ct[i] - at[i]

    wt[i] = tat[i] - bt[i]

# Display Output
print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):

    print(p[i], "\t",
          at[i], "\t",
          bt[i], "\t",
          ct[i], "\t",
          tat[i], "\t",
          wt[i])

# Average Times
avg_tat = sum(tat) / float(n)

avg_wt = sum(wt) / float(n)

print("\nAverage Turnaround Time =", avg_tat)

print("Average Waiting Time =", avg_wt)