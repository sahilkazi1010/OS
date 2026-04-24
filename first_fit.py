blocks = [100,200,312,400,564]
psize = 212
used = [False]*len(blocks)

for i in range(len(blocks)):
    if blocks[i] >= psize and not used[i]:
        used[i] = True
        print(f"First Fit: Block {blocks[i]} allocated to {psize}")
        break
else:
    print("No block allocated")

print(f"Occupancy: {used}")
