import numpy as np
import pandas as pd 

data = pd.DataFrame(data={"A":[1,2,3,4,5,6,7,8,9,10], 
                               "B":[1,3,3,4,5,6,7,8,9,10],
                               "event":[0,0,0,0,1,0,0,0,1,0]})

def EventWindow (data, n=3, dummy=1):
    '''
    data....data. Contains ALL data - reurns, and event dummies = event column
    dummy...event=1
    n.......days before/after
    '''
    idx = data.index.get_indexer_for(data[data.event==dummy].index)
    event_window = data.iloc[np.unique(np.concatenate([np.arange(max(i-n,0), min(i+n+1, len(data)))
                                                for i in idx]))]
    return(event_window)

d = EventWindow(data)

print(d)
