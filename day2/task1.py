import sys

def solver(*args):
    freqs = {0: True} 
    acc = 0
    while True:
        for arg in args:
            acc += int(arg)
            if acc in freqs:
                return acc
            freqs[acc] = True 
    return acc

def dupes_table(args: list):
    freqs = {}
    for arg in args:
        if arg in freqs:
            freqs[arg] += 1
        else: 
            freqs[arg] = 1
    return freqs

def counter(dupes_dict, *targets):
    counts = {
        target: 0 for target in targets
    }
    for v in dupes_dict.values():
        if v in targets:
            counts[v] = 1
    return counts
def count_accumulator(new_counts, acc_counts):
    for k, v in new_counts.items():
        if k in acc_counts:
            acc_counts[k] += v
        else:
            acc_counts[k] = v
    return acc_counts

def mult(args: list):
    value = 1
    for arg in args:
        value *= arg
    return value

def input_handler(args: list):
    accum_counts = {}
    for arg in args:
        dupes = dupes_table(args=list(arg))
        counts = counter(dupes, 2, 3)
        accum_counts = count_accumulator(counts, accum_counts)
    return mult(accum_counts.values())



freqs = {}
print(input_handler(sys.argv[1:]))

