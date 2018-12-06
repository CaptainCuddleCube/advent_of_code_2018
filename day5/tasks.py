from functions import react, polymer_optimizer
f = open('task.data', 'r')
polymer_str = '' 
for line in f:
    polymer_str += str(line.replace('\n',''))
f.close()

print(f"Task 1: {len(list(react(polymer_str)))}")
# NOTE, reacting the sequence first will provide the same answer, but will
# improve the execution time massively.
print(f"Task 2: {polymer_optimizer(react(polymer_str))[0]}")
