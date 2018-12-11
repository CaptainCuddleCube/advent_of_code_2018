def rules(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = int((power_level - int(power_level / 1000) * 1000) / 100)
    power_level -= 5
    return power_level

assert rules(3,5,8) == 4
assert rules(122,79,57) == -5
assert rules(217,196,39) == 0
assert rules(101,153,71) == 4

def get_grid(n, serial_number):
    grid = {}
    x = 1
    y = 1
    while x <= n:
        while y <= n:
            grid[f"{x},{y}"] = rules(x, y, serial_number)
            y += 1
        y = 1
        x += 1
    return grid


def calc_power(x, y, n, grid):
    new_power = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            new_power += grid[f"{i},{j}"]
    return new_power


def calc_power_pp2(x, y, n, grid):
    new_power = 0

    if n % 2 == 0:
        for i in range(2):
            for j in range(2):
                new_power += grid[f"{x + i},{y + j},{int(n/2)}"]
    if n > 1:
        new_power = grid[f"{x},{y},{int(n - 1)}"]
        for j in range(0,n-1):
            new_power += grid[f"{x + n -1},{y + j}"] 
        for i in range(0,n):
            new_power += grid[f"{x + i},{y + n - 1}"]
    else:
        new_power = calc_power(x,y,n,grid)

    grid[f"{x},{y},{n}"] = new_power
    # print(f"{x},{y},{n}")
    return new_power

def find_cell(n, size, grid, it=False):
    x = 1
    y = 1
    total_power = 0
    points = [1, 1]
    while x <= (n - size):
        while y <= (n - size):
            if it:
                new_power = calc_power_pp2(x, y, size, grid)
            else:
                new_power = calc_power(x, y, size, grid)
            if new_power > total_power:
                total_power = new_power
                points = [x, y]
            y += 1
        y = 1
        x += 1
    return (points, total_power)

assert find_cell(300, 3, get_grid(300, 18)) == ([33, 45], 29)
assert find_cell(300, 3, get_grid(300, 42)) == ([21, 61], 30)

grid = get_grid(300, 4151)
print(find_cell(300, 3, grid))

grid1 = get_grid(300, 18)
find_cell(300, 1, grid1, it=True)
find_cell(300, 2, grid1, it=True)
print(find_cell(300, 3, grid1, it=True))
assert find_cell(300, 3, grid1, it=True) == ([33, 45], 29)

grid2 = get_grid(300, 42)
find_cell(300, 1, grid2, it=True)
find_cell(300, 2, grid2, it=True)
print(find_cell(300, 3, grid2, it=True))
assert find_cell(300, 3, grid2, it=True) == ([21, 61], 30)


def incrementor(grid):
    points = [1,1]
    total_power = 0
    size = 1
    # with larger sets - the average will tend to 0 since they are subtracting 
    # 5 from a random number between 0 and 9. 
    for n in range(1, 20):
        (new_points, new_power) = find_cell(300, n, grid, it=True)
        print(f"n: {n}, Power: {new_power}")
        if new_power > total_power: 
            total_power = new_power
            points = new_points
            size = n
    return (points, size, total_power)
print(incrementor(get_grid(300, 4151)))