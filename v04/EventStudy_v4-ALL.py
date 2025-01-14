import pandas as pd
import EventStudy_tools as es
path = '/Users/Alen/Documents/2_GitHub/Event-Study-2019/v04/'

file = [
#        "11_beat1.xlsx",
#        "11_miss1.xlsx",
#        "21_beat1.xlsx",
#        "21_miss1.xlsx",
        "31_beat1.xlsx",
#        "31_miss1.xlsx",
#        "41_beat1.xlsx",
#        "41_miss1.xlsx",
#        "51_beat1.xlsx",
#        "51_miss1.xlsx"
        ]

column_names = ["index",
                "ar-1", "ar-0", "ar+1",
                "-1", "0", "1"]

cols_to_del = [0,1,2,3]

days = [-1, 0, 1]
#days = [-3, -2, -1, 0, 1, 2, 3]

assets = ["r_LU13TRUU","r_LU35TRUU",	"r_LU57TRUU",
          "r_LU71TRUU","r_LU10TRUU","r_LU3ATRUU"	,
          "r_LU2ATRUU","r_LU1ATRUU","r_LUBATRUU",
          "r_LUATTRUU","r_LUACTRUU","r_2_equal","r_2_minvar"]

event = [
#        "CPEXEMUY", 
#        "ECCPEMUY", 
        "CPI_CHNG", 
#        "CPUPXCHG", 
#        "PCE_CMOM"
        ]


CAARs= []
for asset in assets:
    df = es.Excel3(path, file[0], asset, column_names, cols_to_del)
    caar = [df[column].mean(axis=0) for column in df]
    CAARs.append(caar)
    es.graph(asset, days, caar, 1, event[0], beat=1)

    
    
    
    
    
    
#    print(df.describe())
    exec('{} = pd.DataFrame(df)'.format(asset))
#    exec('{} = pd.DataFrame(df2)'.format("AR",asset))
print("done")
        
        



