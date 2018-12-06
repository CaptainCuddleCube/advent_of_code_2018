import string
def create_reaction_pairs():
    lst = []
    unit_pairs = create_base_units()
    for unit_pair in unit_pairs:
        pair1 = unit_pair[0] + unit_pair[1]
        pair2 = unit_pair[1] + unit_pair[0]
        lst.append(pair1) 
        lst.append(pair2)
    return lst

def create_base_units():
    lst = []
    letters = list(string.ascii_lowercase)
    for letter in letters:
        lst.append([letter, letter.upper()])
    return lst

def react(polymer_str):
    length = 0
    remove_pairs = create_reaction_pairs()
    while length != len(polymer_str):
        length = len(polymer_str)
        for pair in remove_pairs:
            polymer_str = polymer_str.replace(pair, '')
    return polymer_str

def polymer_optimizer(polymer_str):
    unit_pairs = create_base_units()
    result = []
    for pair in unit_pairs:
        tmp_str = polymer_str
        tmp_str = tmp_str.replace(pair[0],'').replace(pair[1],'')
        result.append({
            'count': len(react(tmp_str)),
            'pair' : ''.join(pair) 
        })
    result.sort(key=lambda e: e['count'])
    return result
