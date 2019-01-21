import pandas as pd 
import EventStudy_tools as es
# Import Excel
f = '/Users/Alen/Documents/0_Academic/0_University/2_Magistrski_Studij/3_Semester (2018)/Empirical Asset Pricing/2_Trigav Skladi/v03/Export.xlsx'
f2 = '/Users/Alen/Documents/0_Academic/0_University/2_Magistrski_Studij/3_Semester (2018)/Empirical Asset Pricing/2_Trigav Skladi/v03/3_miss3.xlsx'
data = es.Excel(f)



# Set benchmark and assets
benchmark = "r_LBUSTRUU"
assets = ["r_LU13TRUU","r_LU35TRUU",	"r_LU57TRUU",
          "r_LU71TRUU","r_LU10TRUU","r_LU3ATRUU"	,
          "r_LU2ATRUU","r_LU1ATRUU","r_LUBATRUU",
          "r_LUATTRUU","r_LUACTRUU","r_2_equal","r_2_minvar"]
n = 3





# Get estimation & event windows; delete last estimation window
event_win = es.EventWindow(data, n)
est_win = es.EstimationWindow(data, n)
if len(event_win) < len(est_win):
    del est_win[-1]
#Case1 CAPM alphas and betas
case1  = es.CAPM(est_win, benchmark, assets)
#Obtain ARs
abnormal_returns = es.AbnormalReturns(case1, event_win, assets, benchmark)
# Create dfs for each asset
for asset in range(len(assets)):
    name = assets[asset]
    exec('{} = pd.DataFrame(abnormal_returns[asset][0])'.format(name))





with pd.ExcelWriter(f2) as writer:
    r_LU13TRUU.to_excel(writer, "r_LU13TRUU")
    r_LU35TRUU.to_excel(writer, "r_LU35TRUU")
    r_LU57TRUU.to_excel(writer, "r_LU57TRUU")
    r_LU71TRUU.to_excel(writer, "r_LU71TRUU")
    r_LU10TRUU.to_excel(writer, "r_LU10TRUU")
    r_LU3ATRUU.to_excel(writer, "r_LU3ATRUU")
    r_LU2ATRUU.to_excel(writer, "r_LU2ATRUU")
    r_LU1ATRUU.to_excel(writer, "r_LU1ATRUU")
    r_LUBATRUU.to_excel(writer, "r_LUBATRUU")
    r_LUATTRUU.to_excel(writer, "r_LUATTRUU")
    r_LUACTRUU.to_excel(writer, "r_LUACTRUU")            
    r_2_equal.to_excel(writer, "r_2_equal")            
    r_2_minvar.to_excel(writer, "r_2_minvar")


            