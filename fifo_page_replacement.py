pages = [3,2,5,6,1,3,2]
frames = 3

mem = []
ptr = 0
fault = 0

for p in pages:
    if p in mem:
        print(f"{p} -> Hit  {mem}")
    else:
        if len(mem) < frames:
            mem.append(p)
        else:
            mem[ptr] = p
            ptr = (ptr + 1) % frames

        fault += 1
        print(f"{p} -> Fault {mem}")

print(f"Total Page Faults = {fault}")


