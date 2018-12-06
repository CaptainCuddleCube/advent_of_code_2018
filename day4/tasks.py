from functions import parse_input_data,\
                      sort_by_date,\
                      create_states,\
                      find_longest,\
                      find_most_often,\
                      look_for_best

f = open('task.data', 'r')
lst = []
for line in f:
    lst.append(line.replace('\n',''))
f.close()

data = parse_input_data(lst)
data.sort(key=sort_by_date())
data = create_states(data)
best = find_longest(data)
most_often = find_most_often(data[best['id']])
print(f"Task 1: {most_often[0] * best['id']}")
task2_best = look_for_best(data)[0]
print(f"Task 2: {task2_best['min'] * task2_best['id']}")