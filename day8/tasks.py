f = open('task.data', 'r')

license_data = []
for line in f:
    numbers = line.replace('\n','').split(' ')
    license_data = list(map(lambda n : int(n), numbers))
f.close()

def get_metadata(index, data):
    if data[index] == 0:
        offset = index + 2
        segment_length = len(data[index:data[index+1] + offset])
        metadata = data[offset:data[index+1] + offset]
        value = sum(data[offset:data[index+1] + offset])
        return (segment_length, metadata, value)
    else:
        metadata = []
        values = {}
        offset = index + 2
        length = 2
        for i in range(1, data[index]+1):
            (l, new_meta, new_value) = get_metadata(offset, data)
            offset += l
            length += l
            metadata += new_meta
            values[i] = new_value
        length += data[index + 1]
        metadata += data[offset: offset+data[index+1]]
        value = []
        for ref in data[offset: offset+data[index+1]]:
            if ref in values:
                value.append(values[ref])
            else:
                value.append(0)
        return (length, metadata, sum(value))

assert get_metadata(0, [0, 3, 10, 11, 12, 13, 14]) == (5, [10, 11, 12], 33)
assert get_metadata(0, [1, 1, 0, 1, 99, 2 ]) == (6, [99, 2], 0)
assert get_metadata(0, [2, 2, 0, 1, 2, 0, 1, 3, 1, 2]) == (10, [ 2, 3, 1, 2],5)
assert get_metadata(0, [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]) \
== (16, [10, 11, 12, 99, 2, 1, 1, 2], 66)

(_, metadata, value) = get_metadata(0, license_data)

print(f"Task 1 : {sum(metadata)}")
print(f"Task 1 : {value}")