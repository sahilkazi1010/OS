n = int(input("Enter number of requests: "))

requests = []

for i in range(n):
    requests.append(int(input("Enter request: ")))

head_position = int(input("Enter head position: "))

total_seek = 0

print("Sequence:")
print(head_position, end="")

for request in requests:

    total_seek += abs(request - head_position)

    head_position = request

    print(f" -> {head_position}", end="")

print(f"\nTotal Head Movement = {total_seek}")  
