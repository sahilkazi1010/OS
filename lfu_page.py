# 12) LFU Page Replacement

pages = [3,2,5,6,1,3,2]
frames = 4

mem = []
freq = {}
time = {}
fault = 0
t = 0

for p in pages:
    t += 1

    if p in mem:
        freq[p] += 1
        time[p] = t
        print(f"{p} -> Hit  {mem}")
    else:
        fault += 1

        if len(mem) < frames:
            mem.append(p)
        else:
            x = min(mem, key=lambda i:(freq[i],time[i]))
            mem[mem.index(x)] = p

        freq[p] = 1
        time[p] = t
        print(f"{p} -> Fault {mem}")

print(f"Total Page Faults = {fault}")
