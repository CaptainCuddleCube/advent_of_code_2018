def reshaper(args):
    data = []
    i = 0
    while i <= len(args) - 4:
        data.append({
            'id': args[i],
            'shift': args[i+2].replace(':','').split(','),
            'area': args[i+3].split('x')
        })
        i += 4
    return data

def generate_grid():
    grid = []
    for i in range(1000):
        grid.append([])
        for _ in range(1000):
            grid[i].append({'count':0})
    return grid

def collision_counter(data):
    grid = generate_grid()
    count = 0
    for d in data:
        for x in range(int(d['area'][0])):
            for y in range(int(d['area'][1])):
                grid[x+int(d['shift'][0])][y+int(d['shift'][1])]['count'] += 1
                if grid[x+int(d['shift'][0])][y+int(d['shift'][1])]['count'] == 2:
                    count += 1
    return {
        'grid' : grid,
        'count' : count
    }