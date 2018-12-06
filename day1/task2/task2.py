import sys
import pandas as pd

def solver(*args):
    freqs = [0]
    acc = 0
    duplicate = False
    iteration = 0
    while not duplicate:
        iteration += 1
        for arg in args:
            acc += int(arg)
            freqs.append(acc)
        if  iteration % 144  is 0:
            print(f"Iteration: {iteration}")
            tmp = pd.DataFrame(freqs)

            dupes = tmp[tmp.duplicated(keep='first')]

            if len(dupes) > 0:
                duplicate = True
                print(f'dupes: {len(dupes)}')
                acc = dupes.iloc[0,0]
                print(f'all freq {len(freqs)}')
            else:
                print("nothing")
                dupes = []
    return acc


print(solver(*sys.argv[1:]))

