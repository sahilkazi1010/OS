# 4) C-SCAN Disk Scheduling

n = int(input("Enter no of requests: "))
req = []

for i in range(n):
    req.append(int(input()))

head = int(input("Enter head position: "))
disk = int(input("Enter disk size: "))

seek = 0
left = sorted([i for i in req if i < head])
right = sorted([i for i in req if i >= head])

print("Sequence:")
print(head, end="")

for r in right:
    seek += abs(r - head)
    head = r
    print(f" -> {head}", end="")

seek += abs((disk - 1) - head)
head = disk - 1
print(f" -> {head}", end="")

seek += abs(head - 0)
head = 0
print(f" -> {head}", end="")

for r in left:
    seek += abs(r - head)
    head = r
    print(f" -> {head}", end="")

print(f"\nTotal Head Movement = {seek}")