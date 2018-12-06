import string
import operator
x = list(string.ascii_letters)

f = open('task.data', 'r')
lst = []
index = 0
for line in f:
    pair = line.replace('\n','').split(', ')
    pair[0] = int(pair[0])
    pair[1] = int(pair[1])
    lst.append({
        'key': x[index],
        'pair':pair
    })
    index += 1
f.close()

def max(args, index):
    max = args[0]['pair'][index]
    for arg in args:
        if arg['pair'][index] > max:
            max = arg['pair'][index]
    return max
def min(args, index):
    min = args[0]['pair'][index]
    for arg in args:
        if arg['pair'][index] < min:
            min = arg['pair'][index]
    return min

def generate_grid(x, y):
    grid = []
    for i in range(max_x):
        grid.append([])
        for _ in range(max_y):
            grid[i].append({})
    return grid

def calculate_distance(point, key, grid, min_x, min_y):
    for x_point, y_points in enumerate(grid):
        for y_point, grid_point in enumerate(y_points):
            shifted_x = point[0] - min_x
            shifted_y = point[1] - min_y
            distance = abs(shifted_x - x_point) + abs(shifted_y - y_point)

            if grid_point == {}:
                grid[x_point][y_point] = {
                    'owner' : key,
                    'distance': distance
                }
            else:
                if distance < grid_point['distance']:
                    grid[x_point][y_point] = {
                        'owner': key,
                        'distance': distance
                    }
                elif distance == grid_point['distance']:
                    grid[x_point][y_point] = {
                        'owner': '*',
                        'distance': distance
                    }
    return grid

def populate_grid(points, grid, min_x, min_y):
    for point in points:
        grid = calculate_distance(point['pair'], point['key'], grid, min_x, min_y)
    return grid

def count_areas(grid, owners):
    tallies = {}
    for owner in owners:
        tallies[owner] = {
            'count': 0,
            'include' : True
        }
    tallies['*'] = {
        'count': 0,
        'include': False
    }
    for index in range(len(grid)):
        tallies[grid[index][0]['owner']]['include'] = False
        tallies[grid[index][len(grid[0])-1]['owner']]['include'] = False
    
    for index in range(len(grid[0])):
        tallies[grid[0][index]['owner']]['include'] = False
        tallies[grid[len(grid)-1][index]['owner']]['include'] = False
    for y_points in grid:
        for grid_point in y_points:
            if tallies[grid_point['owner']]['include']:
                tallies[grid_point['owner']]['count'] += 1
    return tallies

def largest_area(areas):
    max = next(iter(areas.values()))['count']
    for value in areas.values():
        if value['count'] > max:
            max = value['count']
    return max


def find_largest_safe(threshold, points):
    max_x = max(lst, 0)
    max_y = max(lst, 1)
    min_x = min(lst, 0)
    min_y = min(lst, 1)
    size = 0
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            sum = 0
            for point in points:
                sum += abs(point['pair'][0] - x) + abs(point['pair'][1] - y)
            if sum < threshold:
                size +=1
    return size

max_x = max(lst, 0)
max_y = max(lst, 1)
min_x = min(lst, 0)
min_y = min(lst, 1)

grid = generate_grid(max_x - min_x, max_y - min_y)
populated_grid = populate_grid(lst, grid, min_x, min_y)
areas = count_areas(populated_grid, x)

print(f"Task 1: {largest_area(areas)}")
print(f"Task 2: {find_largest_safe(10000, lst)}")