# FCFS Scheduling Algorithm

processes = ["P1", "P2", "P3", "P4", "P5"]
arrival_time = [0, 2, 6, 7, 13]
burst_time = [4, 16, 12, 8, 2]

n = len(processes)

completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

# Calculate Completion Time
completion_time[0] = arrival_time[0] + burst_time[0]

for i in range(1, n):

    if completion_time[i - 1] < arrival_time[i]:
        completion_time[i] = arrival_time[i] + burst_time[i]
    else:
        completion_time[i] = completion_time[i - 1] + burst_time[i]

# Calculate Turnaround Time and Waiting Time
for i in range(n):

    turnaround_time[i] = completion_time[i] - arrival_time[i]

    waiting_time[i] = turnaround_time[i] - burst_time[i]

# Display Output
print("Process\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):

    print(processes[i], "\t",
          arrival_time[i], "\t",
          burst_time[i], "\t",
          completion_time[i], "\t",
          turnaround_time[i], "\t",
          waiting_time[i])

# Average Times
avg_tat = sum(turnaround_time) / float(n)
avg_wt = sum(waiting_time) / float(n)

print("\nAverage Turnaround Time =", avg_tat)

print("Average Waiting Time =", avg_wt)