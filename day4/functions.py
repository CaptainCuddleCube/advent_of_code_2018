import datetime as dt
import pandas as pd
import operator
import re

def sort_key_in_object_array(key: str):
    return lambda a : a[key]

def get_timestamp_sorter(key: str):
    return lambda e: e[key].timestamp()

def sort_by_date():
    return get_timestamp_sorter('date')

def parse_input_data(args):
    data = []
    for arg in args:
        spt = arg.split('] ')
        date =pd.to_datetime(re.sub(r'^\[15','20',spt[0]))
        state = spt[1]
        data.append({
            'date': date,
            'state': state
        })
    return data

def create_states(args):
    data = {}
    id = ''
    for arg in args:
        state = arg['state'].split(' ')
        if state[0] == 'Guard':
            id = int(state[1].replace('#',''))
            if id in data:
                data[id].append({
                    'date' : arg['date'],
                    'state' : 'awake'
                })
            else:
                data[id] = [{
                    'date' : arg['date'],
                    'state' : 'awake'
                }]
        elif state[0] == 'falls':
            data[id].append({
                'date': arg['date'],
                'state' : 'sleeping'
            })
        elif state[0] == 'wakes':
            data[id].append({
                'date' : arg['date'],
                'state' : 'awake'
            })
    return data


def find_longest(data):
    ranked = []
    for k, series in data.items():
        total_sleep_time = 0
        start_time = 0
        is_sleeping = False
        for step in series:
            if step['state'] == 'sleeping':
                is_sleeping = True
                start_time = step['date']
            if step['state'] == 'awake' and is_sleeping:
                is_sleeping = False
                if total_sleep_time == 0:
                    total_sleep_time = step['date'] - start_time
                else:
                    total_sleep_time += step['date'] - start_time
        if total_sleep_time != 0:
            ranked.append({
                'id' : k,
                'total_time': int(total_sleep_time.seconds / 60)
            })
    ranked.sort(key=sort_key_in_object_array('total_time'), reverse=True)
    return ranked[0]


def find_most_often(arg):
    times_asleep = {}
    start_time = 0
    is_sleeping = False
    for step in arg:
            if step['state'] == 'sleeping':
                is_sleeping = True
                start_time = step['date']
            if step['state'] == 'awake' and is_sleeping:
                is_sleeping = False
                delta = step['date'] - start_time
                delta = int(delta.seconds / 60 )
                for min in range(delta):
                    min_sleeping = (start_time + dt.timedelta(minutes=min)).minute
                    if min_sleeping in times_asleep:
                        times_asleep[min_sleeping] += 1
                    else:
                        times_asleep[min_sleeping] = 1
    x = sorted(times_asleep.items(), key=operator.itemgetter(1),reverse=True)
    if len(x) == 0:
        return [0,0]
    return x[0]

def look_for_best(args):
    data = []
    for key, value in args.items():
        x = find_most_often(value)
        data.append({
            'id': key,
            'count': x[1],
            'min': x[0]
        })
    data.sort(key=sort_key_in_object_array('count'), reverse=True)
    return data