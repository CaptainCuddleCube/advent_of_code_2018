import string
BASE_TASK_TIME = 60
NUMER_OF_WORKERS = 5
def extract_parent_and_child_nodes(cmd: str):
    splt = cmd.split(' ')
    return [splt[1], splt[7]]

def task_time(task_id, base_time=BASE_TASK_TIME):
    return string.ascii_uppercase.index(task_id) + 1 + base_time 

f = open('task.data', 'r')
cmds = [] 
for line in f:
    cmds.append(extract_parent_and_child_nodes(line.replace('\n','')))
f.close()

# Tests to make sure we are getting consistent time steps.
assert task_time('A') == 61
assert task_time('Z') == 86

def run_task(task_id, now):
    def task(time):
        return (task_id, 'completed') if task_time(task_id) - (time - now) == 0 \
                           else (task_id, 'working')
    return task

# Making sure the task runners are working
assert run_task('A', 10)(15) == ('A', 'working')
assert run_task('A', 10)(70) == ('A', 'working')
assert run_task('A', 10)(71) == ('A', 'completed')

# we will now get the children and parents in the cmds. From here, we can 
# determin which tasks can be started (have no dependencies)
def get_parents(cmds):
    parents = list(set(map(lambda a: a[0], filter(lambda a: a[0] != '', cmds))))
    parents += list(set(map(lambda a: a[1], filter(lambda a: a[0] == '', cmds)))) 
    parents = list(set(filter(lambda a: a[0] != '', parents)))
    parents.sort()
    return parents

assert get_parents([['A','B'],['B','C']]) == ['A', 'B']
assert get_parents([['B','C'],['B','D']]) == ['B']
assert get_parents([['','C'],['B','D']]) == ['B','C']
assert get_parents([['', 'E']]) == ['E']

def get_children(cmds):
    children = list(set(map(lambda a: a[1], filter(lambda a: a[0] != '' and a[1] != '', cmds))))
    children.sort()
    return children

assert get_children([['A', 'B'], ['B', 'C']]) == ['B', 'C']
assert get_children([['C', 'C'], ['B', 'C']]) == ['C']
assert get_children([['', 'C'], ['B', '']]) == []

def get_available_tasks(parents, children, workers):
    available_tasks = []
    def parse_worker(worker):
        (id, _) = worker(0)
        return id
    busy_tasks = list(map(parse_worker, workers))
    for parent in parents:
        if parent not in children and parent not in busy_tasks:
            available_tasks.append(parent)
    available_tasks.sort(reverse=True)
    return available_tasks

def return_A(val):
    return ('A', val)
assert get_available_tasks(['A','B'],['C','B'],[return_A]) == []

def workers_to_add(current_workers, total_workers, tasks_available):
    workers = total_workers - current_workers
    workers = workers if workers >= 0 else 0
    return workers if workers < tasks_available else tasks_available

assert workers_to_add(5, 5, 3) == 0
assert workers_to_add(3, 5, 3) == 2
assert workers_to_add(0, 5, 4) == 4
assert workers_to_add(0, 5, 6) == 5

time = 0
worker_pool = []
order = ''
while len(cmds) > 0:
    delete_workers = []
    for index, worker in enumerate(worker_pool):
        (id, status) = worker(time)
        if status == 'completed':
            delete_workers.append({
                'worker': worker,
                'id': id
            })

    for worker in delete_workers:
        # print(f"Removing {worker['id']} at time: {time}")
        worker_pool.remove(worker['worker'])
        order += worker['id']
        def mapper(a):
            if a[0] == worker['id']:
                a[0] = ''
            return a
        cmds = list(map(mapper, filter(lambda a: a[0]!= '' and a[1] != '', cmds)))

    parents  = get_parents(cmds)
    children = get_children(cmds)
    available_tasks = get_available_tasks(parents, children, worker_pool)
    workers = workers_to_add(len(worker_pool),
                            NUMER_OF_WORKERS,
                            len(available_tasks))
    for i in range(workers):
        worker_pool.append(run_task(available_tasks.pop(), time))
    time += 1
print(f"The order: {order}, in time :{time-1}")
