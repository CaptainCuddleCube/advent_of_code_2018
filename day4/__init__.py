import pandas as pd
import re

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
