import pandas as pd
import EventStudy_tools as es
path = '/Users/Alen/Documents/2_GitHub/Event-Study-2019/v04/'

file = [
        "11_beat1.xlsx",    #event1
#        "11_miss1.xlsx",   #event1
#        "21_beat1.xlsx",   #event2
#        "21_miss1.xlsx",   #event2

#        "11_beat3.xlsx",
#        "11_miss3.xlsx",
#        "21_beat3.xlsx",
#        "21_miss3.xlsx",
        ]

beat_is_1_miss_is_0 = 1

column_names = ["index",
#                "ar-3", "ar-2", "ar-1", "ar-0", "ar+1", "ar+2", "ar+3",
#                "-3","-2","-1","0","1","2","3",
                
                "ar-1", "ar-0", "ar+1",
                "-1", "0", "1"
                ]


#cols_to_del = [0,1,2,3,4,5,6,7]
cols_to_del = [0,1,2,3]


#days = [-3,-2,-1,0,1,2,3]
days = [-1,0,1]



event = [
        "CPEXEMUY", 
#        "ECCPEMUY", 
        ]





###########################################################
assets = ['IB8A','QW1A', 'r_1_equal']

CAARs= []
for asset in assets:
    df = es.Excel3(path, file[0], asset, column_names, cols_to_del)
    caar = [df[column].mean(axis=0) for column in df]
    CAARs.append(caar)
    es.graph(asset, days, caar, max(days), event[0], beat=beat_is_1_miss_is_0)

    
    
    
    
    
    
#    print(df.describe())
    exec('{} = pd.DataFrame(df)'.format(asset))
#    exec('{} = pd.DataFrame(df2)'.format("AR",asset))
print("done")
        
        



