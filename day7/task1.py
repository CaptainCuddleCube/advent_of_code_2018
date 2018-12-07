def extract_parent_and_child_nodes(cmd: str):
    splt = cmd.split(' ')
    return [splt[1], splt[7]]

f = open('task.data', 'r')
cmds = [] 
for line in f:
    cmds.append(extract_parent_and_child_nodes(line.replace('\n','')))
f.close()


print(cmds)
def find_parent(cmds):
    parents = list(map(lambda a: a[0],cmds))
    children = list(map(lambda a: a[1],cmds))
    super_parent = ''
    for parent in parents:
        if parent not in children:
            super_parent = parent
            break
    return super_parent
parent = find_parent(cmds)
available_tasks = []
print(parent)

order = parent

def get_available_tasks(cmds, parent):
    connected_to_master = {}
    for cmd in cmds:
        if cmd[0] != parent:
            connected_to_master[cmd[1]] = False
        elif cmd[0] not in connected_to_master:
            connected_to_master[cmd[1]] = True
    print(connected_to_master)

    return list(map(lambda a : a[1], filter(lambda a: connected_to_master[a[1]] , cmds)))


while len(cmds)>0:
    new_tasks = get_available_tasks(cmds, parent)
    available_tasks = available_tasks + new_tasks 
    print(f"Appended tasked {available_tasks}")
    # re-order tasks
    available_tasks.sort()
    if len(available_tasks) > 0:
        current_task = available_tasks[0]
        order += current_task
        available_tasks.remove(current_task)
    print(f"Adjusted tasks {available_tasks}")
    def mapper(a):
        if a[0] == current_task:
            a[0] = parent
        return a
    cmds = list(map(mapper,filter(lambda a: a[0]!= parent, cmds)))

    print(f"Updated cmds: {cmds}")
    print(order)