import pandas as pd
from pandas import DataFrame

#import data from Excel
ReadExcel = pd.read_excel (r'C:\Users\asus\Documents\Python-Vaje\ts-lu1atruu.xlsx')
df = DataFrame(ReadExcel,columns=['Date','event_horizon','LU1ATRUU_AR'])
df.dropna(inplace=True)

#event_horizon = -7
timeminus7 = df[df.event_horizon == -7]
#print (timeminus7)
listLU1ATRUU_ARminus7 = timeminus7['LU1ATRUU_AR']
#print (listLU1ATRUU_ARminus7)
a = sum(listLU1ATRUU_ARminus7)
#print (a)
b = len(listLU1ATRUU_ARminus7)
#print (b)
c = a/b
#print (c) #AAR(-7)

#event_horizon = -6
timeminus6 = df[df.event_horizon == -6]
#print (timeminus6)
listLU1ATRUU_ARminus6 = timeminus6['LU1ATRUU_AR']
#print (listLU1ATRUU_ARminus6)
d = sum(listLU1ATRUU_ARminus6)
#print (d)
e = len(listLU1ATRUU_ARminus6)
#print (e)
f = d/e
#print (f) #AAR(-6)

#event_horizon = -5
timeminus5 = df[df.event_horizon == -5]
#print (timeminus5)
listLU1ATRUU_ARminus5 = timeminus5['LU1ATRUU_AR']
#print (listLU1ATRUU_ARminus5)
g = sum(listLU1ATRUU_ARminus5)
#print (g)
h = len(listLU1ATRUU_ARminus5)
#print (h)
i = g/h
#print (i) #AAR(-5)

#event_horizon = -4
timeminus4 = df[df.event_horizon == -4]
#print (timeminus4)
listLU1ATRUU_ARminus4 = timeminus4['LU1ATRUU_AR']
#print (listLU1ATRUU_ARminus4)
j = sum(listLU1ATRUU_ARminus4)
#print (j)
k = len(listLU1ATRUU_ARminus4)
#print (k)
l = j/k
#print (l) #AAR(-4)

#event_horizon = -3
timeminus3 = df[df.event_horizon == -3]
#print (timeminus3)
listLU1ATRUU_ARminus3 = timeminus3['LU1ATRUU_AR']
#print (listLU1ATRUU_ARminus3)
m = sum(listLU1ATRUU_ARminus3)
#print (m)
n = len(listLU1ATRUU_ARminus3)
#print (n)
o = m/n
#print (o) #AAR(-3)

#event_horizon = -2
timeminus2 = df[df.event_horizon == -2]
#print (timeminus2)
listLU1ATRUU_ARminus2 = timeminus2['LU1ATRUU_AR']
#print (listLU1ATRUU_ARminus2)
p = sum(listLU1ATRUU_ARminus2)
#print (p)
r = len(listLU1ATRUU_ARminus2)
#print (r)
s = p/r
#print (s) #AAR(-2)

#event_horizon = -1
timeminus1 = df[df.event_horizon == -1]
#print (timeminus1)
listLU1ATRUU_ARminus1 = timeminus1['LU1ATRUU_AR']
#print (listLU1ATRUU_ARminus1)
t = sum(listLU1ATRUU_ARminus1)
#print (t)
u = len(listLU1ATRUU_ARminus1)
#print (u)
v = t/u
#print (v) #AAR(-1)

#event_horizon = 0
timezero = df[df.event_horizon == 0]
#print (timezero)
listLU1ATRUU_ARzero = timezero['LU1ATRUU_AR']
#print (listLU1ATRUU_ARzero)
z = sum(listLU1ATRUU_ARzero)
#print (z)
y = len(listLU1ATRUU_ARzero)
#print (y)
x = z/y
#print (x) #AAR(0)

#event_horizon = 1
timeplus1 = df[df.event_horizon == 1]
#print (timeplus1)
listLU1ATRUU_ARplus1 = timeplus1['LU1ATRUU_AR']
#print (listLU1ATRUU_ARplus1)
aa = sum(listLU1ATRUU_ARplus1)
#print (aa)
bb = len(listLU1ATRUU_ARplus1)
#print (bb)
cc = aa/bb
#print (cc) #AAR(1)

#event_horizon = 2
timeplus2 = df[df.event_horizon == 2]
#print (timeplus2)
listLU1ATRUU_ARplus2 = timeplus2['LU1ATRUU_AR']
#print (listLU1ATRUU_ARplus2)
dd = sum(listLU1ATRUU_ARplus2)
#print (dd)
ee = len(listLU1ATRUU_ARplus2)
#print (ee)
ff = dd/ee
#print (ff) #AAR(2)

#event_horizon = 3
timeplus3 = df[df.event_horizon == 3]
#print (timeplus3)
listLU1ATRUU_ARplus3 = timeplus3['LU1ATRUU_AR']
#print (listLU1ATRUU_ARplus3)
gg = sum(listLU1ATRUU_ARplus3)
#print (gg)
hh = len(listLU1ATRUU_ARplus3)
#print (hh)
ii = gg/hh
#print (ii) #AAR(3)

#event_horizon = 4
timeplus4 = df[df.event_horizon == 4]
#print (timeplus4)
listLU1ATRUU_ARplus4 = timeplus4['LU1ATRUU_AR']
#print (listLU1ATRUU_ARplus4)
jj = sum(listLU1ATRUU_ARplus4)
#print (jj)
kk = len(listLU1ATRUU_ARplus4)
#print (kk)
ll = jj/kk
#print (ll) #AAR(4)

#event_horizon = 5
timeplus5 = df[df.event_horizon == 5]
#print (timeplus5)
listLU1ATRUU_ARplus5 = timeplus5['LU1ATRUU_AR']
#print (listLU1ATRUU_ARplus5)
mm = sum(listLU1ATRUU_ARplus5)
#print (mm)
nn = len(listLU1ATRUU_ARplus5)
#print (nn)
oo = mm/nn
#print (oo) #AAR(5)

#event_horizon = 6
timeplus6 = df[df.event_horizon == 6]
#print (timeplus6)
listLU1ATRUU_ARplus6 = timeplus6['LU1ATRUU_AR']
#print (listLU1ATRUU_ARplus6)
pp = sum(listLU1ATRUU_ARplus6)
#print (pp)
rr = len(listLU1ATRUU_ARplus6)
#print (rr)
ss = pp/rr
#print (ss) #AAR(6)

#event_horizon = 7
timeplus7 = df[df.event_horizon == 7]
#print (timeplus7)
listLU1ATRUU_ARplus7 = timeplus7['LU1ATRUU_AR']
#print (listLU1ATRUU_ARplus7)
tt = sum(listLU1ATRUU_ARplus7)
#print (tt)
uu = len(listLU1ATRUU_ARplus7)
#print (uu)
vv = tt/uu
#print (vv) #AAR(7)

CAARminus7 = c #CAAR(-7)
#print (CAARminus7)
CAARminus6 = c + f #CAAR(-6)
#print (CAARminus6)
CAARminus5 = c + f + i #CAAR(-5)
#print (CAARminus5)
CAARminus4 = c + f + i + l #CAAR(-4)
#print (CAARminus4)
CAARminus3 = c + f + i + l + o #CAAR(-3)
#print (CAARminus3)
CAARminus2 = c + f + i + l + o + s #CAAR(-2)
#print (CAARminus2)
CAARminus1 = c + f + i + l + o + s + v #CAAR(-1)
#print (CAARminus1)
CAARzero = c + f + i + l + o + s + v + x #CAAR(0)
#print (CAARzero)
CAARplus1 = c + f + i + l + o + s + v + x + cc #CAAR(1)
#print (CAARplus1)
CAARplus2 = c + f + i + l + o + s + v + x + cc +ff #CAAR(2)
#print (CAARplus2)
CAARplus3 = c + f + i + l + o + s + v + x + cc + ff + ii #CAAR(3)
#print (CAARplus3)
CAARplus4 = c + f + i + l + o + s + v + x + cc + ff + ii + ll #CAAR(4)
#print (CAARplus4)
CAARplus5 = c + f + i + l + o + s + v + x + cc + ff + ii + ll + oo #CAAR(5)
#print (CAARplus5)
CAARplus6 = c + f + i + l + o + s + v + x + cc + ff + ii + ll + oo + ss #CAAR(6)
#print (CAARplus6)
CAARplus7 = c + f + i + l + o + s + v + x + cc + ff + ii + ll + oo + ss + vv #CAAR(7)
#print (CAARplus7)

CAAR = [CAARminus7, CAARminus6, CAARminus5, CAARminus4, CAARminus3, CAARminus2, CAARminus1, CAARzero, CAARplus1, CAARplus2, CAARplus3, CAARplus4, CAARplus5, CAARplus6, CAARplus7]
time = [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7]

import matplotlib.pyplot as plt

fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(time,CAAR,'k--',color='orange',label=r'$CAAR$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Time Horizon')
ax1.set_ylabel(r'CAAR')