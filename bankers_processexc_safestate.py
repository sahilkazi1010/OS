p = 5
r = 3

allocation = [
    [0,1,0],
    [2,0,0],
    [3,0,2],
    [2,1,1],
    [0,0,2]
]

maximum = [
    [7,5,3],
    [3,2,2],
    [9,0,2],
    [2,2,2],
    [4,3,3]
]

available = [3,3,2]

need = [[0]*r for _ in range(p)]

for i in range(p):
    for j in range(r):
        need[i][j] = maximum[i][j] - allocation[i][j]

finished = [0]*p
safe_sequence = []

count = 0

while count < p:

    found = False

    for i in range(p):

        if not finished[i]:

            possible = True

            for j in range(r):

                if need[i][j] > available[j]:
                    possible = False
                    break

            if possible:

                for j in range(r):
                    available[j] += allocation[i][j]

                safe_sequence.append(i)
                finished[i] = 1
                found = True
                count += 1

    if not found:
        break

if count == p:

    print("System is in Safe State")
    print("Safe Sequence is:")

    for i in safe_sequence:
        print("P"+str(i), end=" ")

else:
    print("System is not in Safe State")