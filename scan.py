n = int(input("Enter no of requests: "))

requests = []

for i in range(n):
    requests.append(int(input()))

head_position = int(input("Enter head position: "))

disk_size = int(input("Enter disk size: "))

total_seek = 0

left = sorted([i for i in requests if i < head_position])

right = sorted([i for i in requests if i >= head_position])

print("Sequence:")
print(head_position, end="")

for request in right:

    total_seek += abs(request - head_position)

    head_position = request

    print(f" -> {head_position}", end="")

total_seek += abs((disk_size - 1) - head_position)

head_position = disk_size - 1

print(f" -> {head_position}", end="")

for request in reversed(left):

    total_seek += abs(request - head_position)

    head_position = request

    print(f" -> {head_position}", end="")

print(f"\nTotal Head Movement = {total_seek}")