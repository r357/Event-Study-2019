import numpy as np
import pandas as pd 
import EventStudy_tools as es

data = pd.DataFrame(data={"A":[1,2,3,4,5,6,7,8,9,10], 
                          "B":[1,3,3,4,5,6,7,8,9,10],
                      "event":[0,0,0,0,1,0,0,0,1,0]})

event_window = es.EventWindow(data, n=1)
est_win = es.EstimationWindow(data, n=1)
print (event_window,3*"\n", est_win)


