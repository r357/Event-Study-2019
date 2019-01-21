import EventStudy_tools as es
path = '/Users/Alen/Documents/2_GitHub/Event-Study-2019/v04/'
file = [
#        "11_miss1.xlsx",
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

assets = ["r_LU13TRUU","r_LU35TRUU",	"r_LU57TRUU",
          "r_LU71TRUU","r_LU10TRUU","r_LU3ATRUU"	,
          "r_LU2ATRUU","r_LU1ATRUU","r_LUBATRUU",
          "r_LUATTRUU","r_LUACTRUU","r_2_equal","r_2_minvar"]

for asset in assets:
    df = es.Excel3(path, file[0], asset, column_names)
    exec('{} = pd.DataFrame(df)'.format(asset))


        
        



