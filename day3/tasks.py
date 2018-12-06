from functions import reshaper, collision_counter


f = open('task.data', 'r')
lst = []
for line in f:
    for item in line.replace('\n','').split(' '):
        lst.append(item)
f.close()

data = reshaper(lst)
ans = collision_counter(data)
print(f"Task 1: {ans['count']}")
grid = ans['grid']
id = 0
for d in data:
    over_lapped_count = 0
    for x in range(int(d['area'][0])):
        for y in range(int(d['area'][1])):
            if grid[x+int(d['shift'][0])][y+int(d['shift'][1])]['count'] > 1:
                over_lapped_count += 1
    if over_lapped_count is 0:
        id = d['id']
        break

print(f'Task 2: {id}')