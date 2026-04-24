n = int(input("Enter no of requests: "))

req = list(map(int, input("Enter requests: ").split()))

head = int(input("Enter head position: "))

seek = 0

print("Sequence:")
print(head, end="")

while req:

    x = min(req, key=lambda i: abs(i - head))

    seek += abs(x - head)

    head = x

    print(f" -> {head}", end="")

    req.remove(x)

print(f"\nTotal Head Movement = {seek}")