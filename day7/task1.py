def extract_parent_and_child_nodes(cmd: str):
    splt = cmd.split(' ')
    return [splt[1], splt[7]]

f = open('task.data', 'r')
cmds = [] 
for line in f:
    cmds.append(extract_parent_and_child_nodes(line.replace('\n','')))
f.close()

def find_parents(cmds):
    parents = list(set(map(lambda a: a[0], cmds)))
    children = list(set(map(lambda a: a[1], cmds)))
    super_parents = []
    for parent in parents:
        if parent not in children:
            super_parents.append(parent)
    return super_parents


parents = find_parents(cmds)

super_parent = '*'
for parent in parents:
    cmds.append(['*', parent])

available_tasks = []

order = super_parent
def get_available_tasks(cmds, parent):
    connected_to_master = {}
    for cmd in cmds:
        if cmd[0] != parent:
            connected_to_master[cmd[1]] = False
        elif cmd[1] not in connected_to_master:
            connected_to_master[cmd[1]] = True
    return list(set(map(lambda a : a[1], filter(lambda a: connected_to_master[a[1]] , cmds))))

while len(cmds) > 0:
    new_tasks = get_available_tasks(cmds, super_parent)
    available_tasks = list(set(available_tasks + new_tasks))
    available_tasks.sort()
    current_task = available_tasks[0]
    order += current_task
    available_tasks.remove(current_task)
    def mapper(a):
        if a[0] == current_task:
            a[0] = super_parent
        return a
    cmds = list(map(mapper,filter(lambda a: a[0]!= super_parent, cmds)))

print(order.replace('*',''))
