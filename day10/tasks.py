f = open('task.data', 'r')
coords = []
for line in f:
    numbers = line.replace('\n','').replace('<',' ').replace('-',' -').replace(',', '').replace('>','').replace('  ', ' ').split(' ')
    coords.append({
        "position": [int(numbers[2]), int(numbers[1])],
        "velocity": [int(numbers[5]), int(numbers[4])]
    })
f.close()

# print(coords)

def update_poistions(coords):
    for index, val in enumerate(coords):
        coords[index]['position'][0] += val['velocity'][0]
        coords[index]['position'][1] += val['velocity'][1]
    return coords

def min_max(coords):
    min_x = coords[0]['position'][0]
    min_y = coords[0]['position'][1]
    max_x = coords[0]['position'][0]
    max_y = coords[0]['position'][1]
    for val in coords:
        if val['position'][0] < min_x:
            min_x = val['position'][0]
        elif val['position'][0] > max_x:
            max_x = val['position'][0]
        if val['position'][1] < min_y:
            min_y = val['position'][1]
        elif val['position'][1] > max_y:
            max_y = val['position'][1]
    
    return (min_x, min_y, max_x, max_y)

def smallest_size(coords):
    (min_x, min_y, max_x, max_y) = min_max(coords) 
    return (max_x - min_x) * (max_y - min_y)

def display(coords):
    (min_x, min_y, max_x, max_y) = min_max(coords)
    x = 0
    y = 0
    grid = []
    # print(f"{min_x}, {min_y}, {max_x}, {max_y}")
    while x <= (max_x - min_x):
        grid.append([])
        while y <= (max_y - min_y):
            grid[x].append(' ')
            y += 1
        y = 0
        x += 1
    for val in coords:
        # print(f" X: {val['position'][0] }, Y: {val['position'][1]}")
        grid[val['position'][0] - min_x][val['position'][1] - min_y] = "#"
    f = open('message', 'w')
    for val in grid:
        f.write(''.join(val)+'\n')
    f.close()

def copier(coords):
    cpy = []
    for val in coords:
        cpy.append({
            "position": [val["position"][0], val["position"][1]],
            "velocity": [val["velocity"][0], val["position"][1]]
        })
    return cpy

iterations = coords
smallest = smallest_size(coords)
it = 0
for i in range(20000):
    if smallest_size(coords) < smallest: 
        it = i
        iterations = copier(coords)
        smallest = smallest_size(coords)
    coords = update_poistions(coords)

print(f"Wait period: {it}")
display(iterations)