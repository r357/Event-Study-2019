import pyfolio as pf
import pandas as pd
data = pd.read_csv("/Users/Alen/Documents/0_Academic/0_University/2_Magistrski_Studij/3_Semester (2018)/Empirical Asset Pricing/2_Trigav Skladi/v02/trigskl8csv_rets.csv", sep=";")
data = data.dropna()

print(data.head())
p1 = data[["IB8A", "QW1A"]]
p2 = data[["LU35TRUU",
            "LU13TRUU",
            "LU57TRUU",
            "LU71TRUU",
            "LU10TRUU",
            "LU3ATRUU",
            "LU2ATRUU",
            "LU1ATRUU",
            "LUBATRUU",
            "LUATTRUU",
            "LUACTRUU"]]

w1 = pf.Wrapper_Markowitz(p1, len(p1.columns), short=False)
w2 = pf.Wrapper_Markowitz(p2, len(p2.columns), short=False)  