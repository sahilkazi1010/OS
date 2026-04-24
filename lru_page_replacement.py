
pages = [7,0,1,2,0,3,0,4,2,3,0,3,2,3]
frames = 4

mem = []
recent = {}
fault = 0
t = 0

for p in pages:
    t += 1

    if p in mem:
        recent[p] = t
        print(f"{p} -> Hit  {mem}")
    else:
        fault += 1

        if len(mem) < frames:
            mem.append(p)
        else:
            x = min(mem, key=lambda i: recent[i])
            mem[mem.index(x)] = p

        recent[p] = t
        print(f"{p} -> Fault {mem}")

print(f"Total Page Faults = {fault}")



