import sys

def solver(*args):
    answer = 0
    for arg in args:
        answer += int(arg)
    return answer

print(solver(*sys.argv[1:]))

