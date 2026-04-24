blocks = [200,100,323,67,78,232]
psize = 212
used = [False]*len(blocks)

idx = -1
mn = 9999

for i in range(len(blocks)):
    if blocks[i] >= psize and not used[i]:
        if blocks[i] < mn:
            mn = blocks[i]
            idx = i

if idx == -1:
    print("No block allocated")
else:
    used[idx] = True
    print(f"Best Fit: Block {blocks[idx]} allocated to {psize}")

print(f"Occupancy: {used}")