f = open('task.data', 'r')

icense_data = []
for line in f:
    numbers = line.replace('\n','').split(' ')
    license_data = list(map(lambda n : int(n), numbers))
f.close()

def get_data(index, data):
    if data[index] == 0:
        offset = index + 2
        segment_length = len(data[index:data[index+1] + offset])
        metadata = data[offset:data[index+1] + offset]
        return (segment_length, metadata)
    else:
        metadata = []
        offset = index + 2
        length = 2
        for _ in range(data[index]):
            (l, new_data) = get_data(offset, data)
            offset += l
            length += l
            metadata += new_data
        length += data[index + 1]
        metadata += data[offset: offset+data[index+1]]
        return (length, metadata)

assert get_data(0, [0, 3, 10, 11, 12, 13, 14]) == (5, [10, 11, 12])
assert get_data(2, [5, 5, 0, 3, 10, 11, 12, 13, 14]) == (5, [10, 11, 12])
assert get_data(0, [1, 1, 0, 1, 99, 2 ]) == (6, [99, 2])

assert get_data(0, [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]) \
== (16, [10, 11, 12, 99, 2, 1, 1, 2])

(_, metadata) = get_data(0, license_data)

print(f"Task 1: {sum(metadata)}")


def get_value(index, data):
    if data[index] == 0:
        offset = index + 2
        segment_length = len(data[index:data[index+1] + offset])
        metadata = sum(data[offset:data[index+1] + offset])
        return (segment_length, metadata)
    else:
        metadata = {}
        offset = index + 2
        length = 2
        for i in range(1, data[index]+1):
            (l, new_data) = get_value(offset, data)
            offset += l
            length += l
            metadata[i] = new_data
        length += data[index + 1]
        value = []
        for ref in data[offset: offset+data[index+1]]:
            if ref in metadata:
                value.append(metadata[ref])
            else:
                value.append(0)
        return (length, sum(value))


assert get_value(0, [0, 3, 10, 11, 12, 13, 14]) == (5, 33)
assert get_value(0, [1, 1, 0, 1, 99, 2 ]) == (6, 0)
assert get_value(0, [2, 2, 0, 1, 2, 0, 1, 3, 1, 2]) == (10, 5)
assert get_value(0, [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]) \
== (16, 66)

(_, value) = get_value(0, license_data)

print(f"Task 2 : {value}")