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

print(solver(*sys.argv[1:]))

