# SRTF Scheduling Algorithm

process = ['P1', 'P2', 'P3', 'P4', 'P5']

arrival_time = [0, 2, 6, 7, 13]

burst_time = [4, 16, 12, 8, 2]

n = len(process)

remaining_time = burst_time[:]

completion_time = [0] * n

turnaround_time = [0] * n

waiting_time = [0] * n

time = 0

completed = 0

while completed < n:

    index = -1

    minimum = 999

    # Find process with minimum remaining time
    for i in range(n):

        if arrival_time[i] <= time and remaining_time[i] > 0:

            if remaining_time[i] < minimum:

                minimum = remaining_time[i]

                index = i

    # If no process is ready
    if index == -1:

        time += 1

        continue

    # Execute process for 1 unit
    remaining_time[index] -= 1

    time += 1

    # Process completed
    if remaining_time[index] == 0:

        completion_time[index] = time

        completed += 1

# Calculate Turnaround Time and Waiting Time
for i in range(n):

    turnaround_time[i] = completion_time[i] - arrival_time[i]

    waiting_time[i] = turnaround_time[i] - burst_time[i]

# Display Output
print("Process\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):

    print(process[i], "\t",
          arrival_time[i], "\t",
          burst_time[i], "\t",
          completion_time[i], "\t",
          turnaround_time[i], "\t",
          waiting_time[i])

# Average Times
average_turnaround_time = sum(turnaround_time) / float(n)

average_waiting_time = sum(waiting_time) / float(n)

print("\nAverage Turnaround Time =", average_turnaround_time)

print("Average Waiting Time =", average_waiting_time)