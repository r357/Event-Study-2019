import pandas as pd
from pandas import DataFrame

#import data from Excel
ReadExcel = pd.read_excel (r'C:\Users\asus\Documents\Python-Vaje\ts-ib8a.xlsx')
df = DataFrame(ReadExcel,columns=['Date','event_horizon','IB8A_AR'])
df.dropna(inplace=True)

#event_horizon = -7
timeminus7 = df[df.event_horizon == -7]
#print (timeminus7) #gives serial no., Date, event_horizon, IB8A_AR for t = -7
listIB8A_ARminus7 = timeminus7['IB8A_AR']
#print (listIB8A_ARminus7) #gives serial no., IB8A_AR for t = -7
a = sum(listIB8A_ARminus7)
#print (a) #sum of IB8A_AR for t = -7
b = len(listIB8A_ARminus7)
#print (b) #no. of events for t = -7
c = a/b
#print (c) #AAR(-7)

#event_horizon = -6
timeminus6 = df[df.event_horizon == -6]
#print (timeminus6) #gives serial no., Date, event_horizon, IB8A_AR for t = -6
listIB8A_ARminus6 = timeminus6['IB8A_AR']
#print (listIB8A_ARminus6) #gives serial no., IB8A_AR for t = -6
d = sum(listIB8A_ARminus6)
#print (d) #sum of IB8A_AR for t = -6
e = len(listIB8A_ARminus6)
#print (e) #no. of events for t = -6
f = d/e
#print (f) #AAR(-6)

#event_horizon = -5
timeminus5 = df[df.event_horizon == -5]
#print (timeminus5) #gives serial no., Date, event_horizon, IB8A_AR for t = -5
listIB8A_ARminus5 = timeminus5['IB8A_AR']
#print (listIB8A_ARminus5) #gives serial no., IB8A_AR for t = -5
g = sum(listIB8A_ARminus5)
#print (g) #sum of IB8A_AR for t = -5
h = len(listIB8A_ARminus5)
#print (h) #no. of events for t = -5
i = g/h
#print (i) #AAR(-5)

#event_horizon = -4
timeminus4 = df[df.event_horizon == -4]
#print (timeminus4) #gives serial no., Date, event_horizon, IB8A_AR for t = -4
listIB8A_ARminus4 = timeminus4['IB8A_AR']
#print (listIB8A_ARminus4) #gives serial no., IB8A_AR for t = -4
j = sum(listIB8A_ARminus4)
#print (j) #sum of IB8A_AR for t = -4
k = len(listIB8A_ARminus4)
#print (k) #no. of events for t = -4
l = j/k
#print (l) #AAR(-4)

#event_horizon = -3
timeminus3 = df[df.event_horizon == -3]
#print (timeminus3) #gives serial no., Date, event_horizon, IB8A_AR for t = -3
listIB8A_ARminus3 = timeminus3['IB8A_AR']
#print (listIB8A_ARminus3) #gives serial no., IB8A_AR for t = -3
m = sum(listIB8A_ARminus3)
#print (m) #sum of IB8A_AR for t = -3
n = len(listIB8A_ARminus3)
#print (n) #no. of events for t = -3
o = m/n
#print (o) #AAR(-3)

#event_horizon = -2
timeminus2 = df[df.event_horizon == -2]
#print (timeminus2) #gives serial no., Date, event_horizon, IB8A_AR for t = -2
listIB8A_ARminus2 = timeminus2['IB8A_AR']
#print (listIB8A_ARminus2) #gives serial no., IB8A_AR for t = -2
p = sum(listIB8A_ARminus2)
#print (p) #sum of IB8A_AR for t = -2
r = len(listIB8A_ARminus2)
#print (r) #no. of events for t = -2
s = p/r
#print (s) #AAR(-2)

#event_horizon = -1
timeminus1 = df[df.event_horizon == -1]
#print (timeminus1) #gives serial no., Date, event_horizon, IB8A_AR for t = -1
listIB8A_ARminus1 = timeminus1['IB8A_AR']
#print (listIB8A_ARminus1) #gives serial no., IB8A_AR for t = -1
t = sum(listIB8A_ARminus1)
#print (t) #sum of IB8A_AR for t = -1
u = len(listIB8A_ARminus1)
#print (u) #no. of events for t = -1
v = t/u
#print (v) #AAR(-1)

#event_horizon = 0
timezero = df[df.event_horizon == 0]
#print (timezero) #gives serial no., Date, event_horizon, IB8A_AR for t = 0
listIB8A_ARzero = timezero['IB8A_AR']
#print (listIB8A_ARzero) #gives serial no., IB8A_AR for t = 0
z = sum(listIB8A_ARzero)
#print (z) #sum of IB8A_AR for t = 0
y = len(listIB8A_ARzero)
#print (y) #no. of events for t = 0
x = z/y
#print (x) #AAR(0)

#event_horizon = 1
timeplus1 = df[df.event_horizon == 1]
#print (timeplus1) #gives serial no., Date, event_horizon, IB8A_AR for t = 1
listIB8A_ARplus1 = timeplus1['IB8A_AR']
#print (listIB8A_ARplus1) #gives serial no., IB8A_AR for t = 1
aa = sum(listIB8A_ARplus1)
#print (aa) #sum of IB8A_AR for t = 1
bb = len(listIB8A_ARplus1)
#print (bb) #no. of events for t = 1
cc = aa/bb
#print (cc) #AAR(1)

#event_horizon = 2
timeplus2 = df[df.event_horizon == 2]
#print (timeplus2) #gives serial no., Date, event_horizon, IB8A_AR for t = 2
listIB8A_ARplus2 = timeplus2['IB8A_AR']
#print (listIB8A_ARplus2) #gives serial no., IB8A_AR for t = 2
dd = sum(listIB8A_ARplus2)
#print (dd) #sum of IB8A_AR for t = 2
ee = len(listIB8A_ARplus2)
#print (ee) #no. of events for t = 2
ff = dd/ee
#print (ff) #AAR(2)

#event_horizon = 3
timeplus3 = df[df.event_horizon == 3]
#print (timeplus3) #gives serial no., Date, event_horizon, IB8A_AR for t = 3
listIB8A_ARplus3 = timeplus3['IB8A_AR']
#print (listIB8A_ARplus3) #gives serial no., IB8A_AR for t = 3
gg = sum(listIB8A_ARplus3)
#print (gg) #sum of IB8A_AR for t = 3
hh = len(listIB8A_ARplus3)
#print (hh) #no. of events for t = 3
ii = gg/hh
#print (ii) #AAR(3)

#event_horizon = 4
timeplus4 = df[df.event_horizon == 4]
#print (timeplus4) #gives serial no., Date, event_horizon, IB8A_AR for t = 4
listIB8A_ARplus4 = timeplus4['IB8A_AR']
#print (listIB8A_ARplus4) #gives serial no., IB8A_AR for t = 4
jj = sum(listIB8A_ARplus4)
#print (jj) #sum of IB8A_AR for t = 4
kk = len(listIB8A_ARplus4)
#print (kk) #no. of events for t = 4
ll = jj/kk
#print (ll) #AAR(4)

#event_horizon = 5
timeplus5 = df[df.event_horizon == 5]
#print (timeplus5) #gives serial no., Date, event_horizon, IB8A_AR for t = 5
listIB8A_ARplus5 = timeplus5['IB8A_AR']
#print (listIB8A_ARplus5) #gives serial no., IB8A_AR for t = 5
mm = sum(listIB8A_ARplus5)
#print (mm) #sum of IB8A_AR for t = 5
nn = len(listIB8A_ARplus5)
#print (nn) #no. of events for t = 5
oo = mm/nn
#print (oo) #AAR(5)

#event_horizon = 6
timeplus6 = df[df.event_horizon == 6]
#print (timeplus6) #gives serial no., Date, event_horizon, IB8A_AR for t = 6
listIB8A_ARplus6 = timeplus6['IB8A_AR']
#print (listIB8A_ARplus6) #gives serial no., IB8A_AR for t = 6
pp = sum(listIB8A_ARplus6)
#print (pp) #sum of IB8A_AR for t = 6
rr = len(listIB8A_ARplus6)
#print (rr) #no. of events for t = 6
ss = pp/rr
#print (ss) #AAR(6)

#event_horizon = 7
timeplus7 = df[df.event_horizon == 7]
#print (timeplus7) #gives serial no., Date, event_horizon, IB8A_AR for t = 7
listIB8A_ARplus7 = timeplus7['IB8A_AR']
#print (listIB8A_ARplus7) #gives serial no., IB8A_AR for t = 7
tt = sum(listIB8A_ARplus7)
#print (tt) #sum of IB8A_AR for t = 7
uu = len(listIB8A_ARplus7)
#print (uu) #no. of events for t = 7
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
ax1.plot(time,CAAR,'k--',color='blue',label=r'$CAAR$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Time Horizon')
ax1.set_ylabel(r'CAAR')

















