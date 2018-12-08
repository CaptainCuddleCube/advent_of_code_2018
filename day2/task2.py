import sys
import time

def diffs(val1, val2):
    length = len(val1)
    diff = {
        'count':0,
        'locations':[]
    }
    for i in range(length):
        if val1[i] is not val2[i]:
            diff['count'] += 1
            diff['locations'].append(i)
    return diff

def diff_handler_On_2(args: list):
    for arg in args:
        arg_l = list(arg)
        for arg2 in args:
            diff = diffs(arg_l, list(arg2))
            if diff['count'] is 1:
                arg_l.remove(arg_l[diff['locations'][0]])
                return ''.join(arg_l)

def diff_handler_2(args: list):
    tree = {0:{}, 1:{}}
    seg = 2
    for arg in args:
        length = int(len(arg)/seg)
        for x in range(seg):
            if arg[x*length: length*(x+1)] in tree[x]:
                tree[x][arg[x*length:length*(x+1)]].append(arg)
            else: 
                tree[x][arg[x*length:length*(x+1)]] = [arg]
    for arg in args:
        length = int(len(arg)/seg)
        arr = tree[0][arg[0:length]] + tree[1][arg[length:length*2]]
        arg_l = list(arg)
        for arg2 in arr:
            diff = diffs(arg_l, list(arg2))
            if diff['count'] is 1:
                arg_l.remove(arg_l[diff['locations'][0]])
                return ''.join(arg_l)

    return "nothing found"


def diff_handler_3(args: list):
    tree = {
        0: {},
        1: {}
    }
    seg = 2
    l = int(len(args[0])/seg)
    for arg in args:
        for x in range(seg):
            start = x*l
            end = (x+1)*l
            if arg[start:end] in tree[x]:
                arg_l = list(arg)
                for arg2 in tree[x][arg[start:end]]:
                    diff = diffs(arg_l, list(arg2))
                    if diff['count'] is 1:
                        arg_l.remove(arg_l[diff['locations'][0]])
                        return ''.join(arg_l)
                tree[x][arg[start:end]].append(arg)
            else:
                tree[x][arg[start:end]] = [arg]
    return "nothing found"

tic = time.perf_counter()
print(diff_handler_On_2(sys.argv[1:]))
delta1 = time.perf_counter() - tic
tic = time.perf_counter()
print(diff_handler_2(sys.argv[1:]))
delta2 = time.perf_counter() - tic
tic = time.perf_counter()
print(diff_handler_3(sys.argv[1:]))
delta3 = time.perf_counter() - tic
print(f"Time for On2 search: {delta1}")
print(f"Time for refined search: {delta2}")
print(f"Time for highly optimized search: {delta3}")

print(f"Delta2 is {delta1/delta2} times faster than delta1")
print(f"Delta3 is {delta1/delta3} times faster than delta1")
print(f"Delta3 is {delta2/delta3} times faster than delta2")
