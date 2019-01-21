import pandas as pd 
import EventStudy_tools as es
# Import Excel
f = '/Users/Alen/Documents/0_Academic/0_University/2_Magistrski_Studij/3_Semester (2018)/Empirical Asset Pricing/2_Trigav Skladi/v03/Export.xlsx'
f2 = '/Users/Alen/Documents/0_Academic/0_University/2_Magistrski_Studij/3_Semester (2018)/Empirical Asset Pricing/2_Trigav Skladi/v03/2_miss1.xlsx'
data = es.Excel(f)



# Set benchmark and assets
benchmark = "r_LP06TREU"
assets = ["r_IB8A", "r_QW1A", "r_1_equal"]






# Get estimation & event windows; delete last estimation window
event_win = es.EventWindow(data, n=1)
est_win = es.EstimationWindow(data, n=1)
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
    r_IB8A.to_excel(writer, "IB8A")
    r_QW1A.to_excel(writer, "QW1A")
    r_1_equal.to_excel(writer, "r_1_equal")


            
            
            