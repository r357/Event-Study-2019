import pandas as pd
from pandas import DataFrame

#import data from Excel
ReadExcel = pd.read_excel (r'C:\Users\asus\Documents\Python-Vaje\ts-01.xlsx', '4beat')
df_beat = DataFrame(ReadExcel,columns=['Date','LU13TRUU_AR', 'LU35TRUU_AR', 'LU57TRUU_AR', 'LU71TRUU_AR', 'LU10TRUU_AR', 'LU3ATRUU_AR', 'LU2ATRUU_AR', 'LU1ATRUU_AR', 'LUBATRUU_AR', 'LUACTRUU_AR', 'LUATTRUU_AR', 'window_beat_CPUPXCHG'])
df_beat.dropna(inplace=True)
#print (df_beat)

ReadExcel = pd.read_excel (r'C:\Users\asus\Documents\Python-Vaje\ts-01.xlsx', '4miss')
df_miss = DataFrame(ReadExcel,columns=['Date','LU13TRUU_AR', 'LU35TRUU_AR', 'LU57TRUU_AR', 'LU71TRUU_AR', 'LU10TRUU_AR', 'LU3ATRUU_AR', 'LU2ATRUU_AR', 'LU1ATRUU_AR', 'LUBATRUU_AR', 'LUACTRUU_AR', 'LUATTRUU_AR', 'window_miss_CPUPXCHG'])
df_miss.dropna(inplace=True)
#print (df_miss)

#LU13TRUU CPUPXCHG beat
timeminus3_beat = df_beat[df_beat.window_beat_CPUPXCHG == -3]
listLU13TRUU_ARminus3_beat = timeminus3_beat['LU13TRUU_AR']
a = sum(listLU13TRUU_ARminus3_beat)
b = len(listLU13TRUU_ARminus3_beat)
c = a/b #AAR_beat(-3)
timeminus2_beat = df_beat[df_beat.window_beat_CPUPXCHG == -2]
listLU13TRUU_ARminus2_beat = timeminus2_beat['LU13TRUU_AR']
d = sum(listLU13TRUU_ARminus2_beat)
e = len(listLU13TRUU_ARminus2_beat)
f = d/e #AAR_beat(-2)
timeminus1_beat = df_beat[df_beat.window_beat_CPUPXCHG == -1]
listLU13TRUU_ARminus1_beat = timeminus1_beat['LU13TRUU_AR']
g = sum(listLU13TRUU_ARminus1_beat)
h = len(listLU13TRUU_ARminus1_beat)
i = g/h #AAR_beat(-1)
timezero_beat = df_beat[df_beat.window_beat_CPUPXCHG == 0]
listLU13TRUU_ARzero_beat = timezero_beat['LU13TRUU_AR']
j = sum(listLU13TRUU_ARzero_beat)
k = len(listLU13TRUU_ARzero_beat)
l = j/k #AAR_beat(0)
timeplus1_beat = df_beat[df_beat.window_beat_CPUPXCHG == 1]
listLU13TRUU_ARplus1_beat = timeplus1_beat['LU13TRUU_AR']
m = sum(listLU13TRUU_ARplus1_beat)
n = len(listLU13TRUU_ARplus1_beat)
o = m/n #AAR(1)
timeplus2_beat = df_beat[df_beat.window_beat_CPUPXCHG == 2]
listLU13TRUU_ARplus2_beat = timeplus2_beat['LU13TRUU_AR']
p = sum(listLU13TRUU_ARplus2_beat)
r = len(listLU13TRUU_ARplus2_beat)
s = p/r #AAR_beat(2)
timeplus3_beat = df_beat[df_beat.window_beat_CPUPXCHG == 3]
listLU13TRUU_ARplus3_beat = timeplus3_beat['LU13TRUU_AR']
t = sum(listLU13TRUU_ARplus3_beat)
u = len(listLU13TRUU_ARplus3_beat)
v = t/u #AAR(3)
CAARminus3_LU13TRUU_beat = c
CAARminus2_LU13TRUU_beat = c + f
CAARminus1_LU13TRUU_beat = c + f + i
CAARzero_LU13TRUU_beat = c + f + i + l
CAARplus1_LU13TRUU_beat = c + f + i + l + o
CAARplus2_LU13TRUU_beat = c + f + i + l + o + s
CAARplus3_LU13TRUU_beat = c + f + i + l + o + s + v
CAAR_LU13TRUU_beat = [CAARminus3_LU13TRUU_beat, CAARminus2_LU13TRUU_beat, CAARminus1_LU13TRUU_beat, CAARzero_LU13TRUU_beat, CAARplus1_LU13TRUU_beat, CAARplus2_LU13TRUU_beat, CAARplus3_LU13TRUU_beat]
time = [-3, -2, -1, 0, 1, 2, 3]

import matplotlib.pyplot as plt

fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(time,CAAR_LU13TRUU_beat,'k--',color='blue',label=r'$CAAR$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Time Horizon')
ax1.set_ylabel(r'CAAR LU13TRUU CPUPXCHG beat')

#LU13TRUU CPUPXCHG miss
timeminus3_miss = df_miss[df_miss.window_miss_CPUPXCHG == -3]
listLU13TRUU_ARminus3_miss = timeminus3_miss['LU13TRUU_AR']
aa = sum(listLU13TRUU_ARminus3_miss)
bb = len(listLU13TRUU_ARminus3_miss)
cc = aa/bb #AAR_miss(-3)
timeminus2_miss = df_miss[df_miss.window_miss_CPUPXCHG == -2]
listLU13TRUU_ARminus2_miss = timeminus2_miss['LU13TRUU_AR']
dd = sum(listLU13TRUU_ARminus2_miss)
ee = len(listLU13TRUU_ARminus2_miss)
ff = dd/ee #AAR_miss(-2)
timeminus1_miss = df_miss[df_miss.window_miss_CPUPXCHG == -1]
listLU13TRUU_ARminus1_miss = timeminus1_miss['LU13TRUU_AR']
gg = sum(listLU13TRUU_ARminus1_miss)
hh = len(listLU13TRUU_ARminus1_miss)
ii = gg/hh #AAR_miss(-1)
timezero_miss = df_miss[df_miss.window_miss_CPUPXCHG == 0]
listLU13TRUU_ARzero_miss = timezero_miss['LU13TRUU_AR']
jj = sum(listLU13TRUU_ARzero_miss)
kk = len(listLU13TRUU_ARzero_miss)
ll = jj/kk #AAR_miss(0)
timeplus1_miss = df_miss[df_miss.window_miss_CPUPXCHG == 1]
listLU13TRUU_ARplus1_miss = timeplus1_miss['LU13TRUU_AR']
mm = sum(listLU13TRUU_ARplus1_miss)
nn = len(listLU13TRUU_ARplus1_miss)
oo = mm/nn #AAR_miss(1)
timeplus2_miss = df_miss[df_miss.window_miss_CPUPXCHG == 2]
listLU13TRUU_ARplus2_miss = timeplus2_miss['LU13TRUU_AR']
pp = sum(listLU13TRUU_ARplus2_miss)
rr = len(listLU13TRUU_ARplus2_miss)
ss = pp/rr #AAR_miss(2)
timeplus3_miss = df_miss[df_miss.window_miss_CPUPXCHG == 3]
listLU13TRUU_ARplus3_miss = timeplus3_miss['LU13TRUU_AR']
tt = sum(listLU13TRUU_ARplus3_miss)
uu = len(listLU13TRUU_ARplus3_miss)
vv = tt/uu #AAR_miss(3)
CAARminus3_LU13TRUU_miss = cc
CAARminus2_LU13TRUU_miss = cc + ff
CAARminus1_LU13TRUU_miss = cc + ff + ii
CAARzero_LU13TRUU_miss = cc + ff + ii + ll
CAARplus1_LU13TRUU_miss = cc + ff + ii + ll + oo
CAARplus2_LU13TRUU_miss = cc + ff + ii + ll + oo + ss
CAARplus3_LU13TRUU_miss = cc + ff + ii + ll + oo + ss + vv
CAAR_LU13TRUU_miss = [CAARminus3_LU13TRUU_miss, CAARminus2_LU13TRUU_miss, CAARminus1_LU13TRUU_miss, CAARzero_LU13TRUU_miss, CAARplus1_LU13TRUU_miss, CAARplus2_LU13TRUU_miss, CAARplus3_LU13TRUU_miss]

fig2 = plt.figure(); ax2=fig2.add_subplot(1,1,1)
ax2.plot(time,CAAR_LU13TRUU_miss,'k--',color='blue',label=r'$CAAR$')
ax2.legend(loc='best')
ax2.set_xlabel(r'Time Horizon')
ax2.set_ylabel(r'CAAR LU13TRUU CPUPXCHG miss')

#LU35TRUU CPUPXCHG beat
listLU35TRUU_ARminus3_beat = timeminus3_beat['LU35TRUU_AR']
a = sum(listLU35TRUU_ARminus3_beat)
b = len(listLU35TRUU_ARminus3_beat)
c = a/b #AAR_beat(-3)
listLU35TRUU_ARminus2_beat = timeminus2_beat['LU35TRUU_AR']
d = sum(listLU35TRUU_ARminus2_beat)
e = len(listLU35TRUU_ARminus2_beat)
f = d/e #AAR_beat(-2)
listLU35TRUU_ARminus1_beat = timeminus1_beat['LU35TRUU_AR']
g = sum(listLU35TRUU_ARminus1_beat)
h = len(listLU35TRUU_ARminus1_beat)
i = g/h #AAR_beat(-1)
listLU35TRUU_ARzero_beat = timezero_beat['LU35TRUU_AR']
j = sum(listLU35TRUU_ARzero_beat)
k = len(listLU35TRUU_ARzero_beat)
l = j/k #AAR_beat(0)
listLU35TRUU_ARplus1_beat = timeplus1_beat['LU35TRUU_AR']
m = sum(listLU35TRUU_ARplus1_beat)
n = len(listLU35TRUU_ARplus1_beat)
o = m/n #AAR(1)
listLU35TRUU_ARplus2_beat = timeplus2_beat['LU35TRUU_AR']
p = sum(listLU35TRUU_ARplus2_beat)
r = len(listLU35TRUU_ARplus2_beat)
s = p/r #AAR_beat(2)
listLU35TRUU_ARplus3_beat = timeplus3_beat['LU35TRUU_AR']
t = sum(listLU35TRUU_ARplus3_beat)
u = len(listLU35TRUU_ARplus3_beat)
v = t/u #AAR(3)
CAARminus3_LU35TRUU_beat = c
CAARminus2_LU35TRUU_beat = c + f
CAARminus1_LU35TRUU_beat = c + f + i
CAARzero_LU35TRUU_beat = c + f + i + l
CAARplus1_LU35TRUU_beat = c + f + i + l + o
CAARplus2_LU35TRUU_beat = c + f + i + l + o + s
CAARplus3_LU35TRUU_beat = c + f + i + l + o + s + v
CAAR_LU35TRUU_beat = [CAARminus3_LU35TRUU_beat, CAARminus2_LU35TRUU_beat, CAARminus1_LU35TRUU_beat, CAARzero_LU35TRUU_beat, CAARplus1_LU35TRUU_beat, CAARplus2_LU35TRUU_beat, CAARplus3_LU35TRUU_beat]

fig3 = plt.figure(); ax3=fig3.add_subplot(1,1,1)
ax3.plot(time,CAAR_LU35TRUU_beat,'k--',color='blue',label=r'$CAAR$')
ax3.legend(loc='best')
ax3.set_xlabel(r'Time Horizon')
ax3.set_ylabel(r'CAAR LU35TRUU CPUPXCHG beat')

#LU35TRUU CPUPXCHG miss
listLU35TRUU_ARminus3_miss = timeminus3_miss['LU35TRUU_AR']
aa = sum(listLU35TRUU_ARminus3_miss)
bb = len(listLU35TRUU_ARminus3_miss)
cc = aa/bb #AAR_miss(-3)
listLU35TRUU_ARminus2_miss = timeminus2_miss['LU35TRUU_AR']
dd = sum(listLU35TRUU_ARminus2_miss)
ee = len(listLU35TRUU_ARminus2_miss)
ff = dd/ee #AAR_miss(-2)
listLU35TRUU_ARminus1_miss = timeminus1_miss['LU35TRUU_AR']
gg = sum(listLU35TRUU_ARminus1_miss)
hh = len(listLU35TRUU_ARminus1_miss)
ii = gg/hh #AAR_miss(-1)
listLU35TRUU_ARzero_miss = timezero_miss['LU35TRUU_AR']
jj = sum(listLU35TRUU_ARzero_miss)
kk = len(listLU35TRUU_ARzero_miss)
ll = jj/kk #AAR_miss(0)
listLU35TRUU_ARplus1_miss = timeplus1_miss['LU35TRUU_AR']
mm = sum(listLU35TRUU_ARplus1_miss)
nn = len(listLU35TRUU_ARplus1_miss)
oo = mm/nn #AAR_miss(1)
listLU35TRUU_ARplus2_miss = timeplus2_miss['LU35TRUU_AR']
pp = sum(listLU35TRUU_ARplus2_miss)
rr = len(listLU35TRUU_ARplus2_miss)
ss = pp/rr #AAR_miss(2)
listLU35TRUU_ARplus3_miss = timeplus3_miss['LU35TRUU_AR']
tt = sum(listLU35TRUU_ARplus3_miss)
uu = len(listLU35TRUU_ARplus3_miss)
vv = tt/uu #AAR_miss(3)
CAARminus3_LU35TRUU_miss = cc
CAARminus2_LU35TRUU_miss = cc + ff
CAARminus1_LU35TRUU_miss = cc + ff + ii
CAARzero_LU35TRUU_miss = cc + ff + ii + ll
CAARplus1_LU35TRUU_miss = cc + ff + ii + ll + oo
CAARplus2_LU35TRUU_miss = cc + ff + ii + ll + oo + ss
CAARplus3_LU35TRUU_miss = cc + ff + ii + ll + oo + ss + vv
CAAR_LU35TRUU_miss = [CAARminus3_LU35TRUU_miss, CAARminus2_LU35TRUU_miss, CAARminus1_LU35TRUU_miss, CAARzero_LU35TRUU_miss, CAARplus1_LU35TRUU_miss, CAARplus2_LU35TRUU_miss, CAARplus3_LU35TRUU_miss]

fig4 = plt.figure(); ax4=fig4.add_subplot(1,1,1)
ax4.plot(time,CAAR_LU35TRUU_miss,'k--',color='blue',label=r'$CAAR$')
ax4.legend(loc='best')
ax4.set_xlabel(r'Time Horizon')
ax4.set_ylabel(r'CAAR LU35TRUU CPUPXCHG miss')

#LU57TRUU CPUPXCHG beat
listLU57TRUU_ARminus3_beat = timeminus3_beat['LU57TRUU_AR']
a = sum(listLU57TRUU_ARminus3_beat)
b = len(listLU57TRUU_ARminus3_beat)
c = a/b #AAR_beat(-3)
listLU57TRUU_ARminus2_beat = timeminus2_beat['LU57TRUU_AR']
d = sum(listLU57TRUU_ARminus2_beat)
e = len(listLU57TRUU_ARminus2_beat)
f = d/e #AAR_beat(-2)
listLU57TRUU_ARminus1_beat = timeminus1_beat['LU57TRUU_AR']
g = sum(listLU57TRUU_ARminus1_beat)
h = len(listLU57TRUU_ARminus1_beat)
i = g/h #AAR_beat(-1)
listLU57TRUU_ARzero_beat = timezero_beat['LU57TRUU_AR']
j = sum(listLU57TRUU_ARzero_beat)
k = len(listLU57TRUU_ARzero_beat)
l = j/k #AAR_beat(0)
listLU57TRUU_ARplus1_beat = timeplus1_beat['LU57TRUU_AR']
m = sum(listLU57TRUU_ARplus1_beat)
n = len(listLU57TRUU_ARplus1_beat)
o = m/n #AAR(1)
listLU57TRUU_ARplus2_beat = timeplus2_beat['LU57TRUU_AR']
p = sum(listLU57TRUU_ARplus2_beat)
r = len(listLU57TRUU_ARplus2_beat)
s = p/r #AAR_beat(2)
listLU57TRUU_ARplus3_beat = timeplus3_beat['LU57TRUU_AR']
t = sum(listLU57TRUU_ARplus3_beat)
u = len(listLU57TRUU_ARplus3_beat)
v = t/u #AAR(3)
CAARminus3_LU57TRUU_beat = c
CAARminus2_LU57TRUU_beat = c + f
CAARminus1_LU57TRUU_beat = c + f + i
CAARzero_LU57TRUU_beat = c + f + i + l
CAARplus1_LU57TRUU_beat = c + f + i + l + o
CAARplus2_LU57TRUU_beat = c + f + i + l + o + s
CAARplus3_LU57TRUU_beat = c + f + i + l + o + s + v
CAAR_LU57TRUU_beat = [CAARminus3_LU57TRUU_beat, CAARminus2_LU57TRUU_beat, CAARminus1_LU57TRUU_beat, CAARzero_LU57TRUU_beat, CAARplus1_LU57TRUU_beat, CAARplus2_LU57TRUU_beat, CAARplus3_LU57TRUU_beat]

fig5 = plt.figure(); ax5=fig5.add_subplot(1,1,1)
ax5.plot(time,CAAR_LU57TRUU_beat,'k--',color='blue',label=r'$CAAR$')
ax5.legend(loc='best')
ax5.set_xlabel(r'Time Horizon')
ax5.set_ylabel(r'CAAR LU57TRUU CPUPXCHG beat')

#LU57TRUU CPUPXCHG miss
listLU57TRUU_ARminus3_miss = timeminus3_miss['LU57TRUU_AR']
aa = sum(listLU57TRUU_ARminus3_miss)
bb = len(listLU57TRUU_ARminus3_miss)
cc = aa/bb #AAR_miss(-3)
listLU57TRUU_ARminus2_miss = timeminus2_miss['LU57TRUU_AR']
dd = sum(listLU57TRUU_ARminus2_miss)
ee = len(listLU57TRUU_ARminus2_miss)
ff = dd/ee #AAR_miss(-2)
listLU57TRUU_ARminus1_miss = timeminus1_miss['LU57TRUU_AR']
gg = sum(listLU57TRUU_ARminus1_miss)
hh = len(listLU57TRUU_ARminus1_miss)
ii = gg/hh #AAR_miss(-1)
listLU57TRUU_ARzero_miss = timezero_miss['LU57TRUU_AR']
jj = sum(listLU57TRUU_ARzero_miss)
kk = len(listLU57TRUU_ARzero_miss)
ll = jj/kk #AAR_miss(0)
listLU57TRUU_ARplus1_miss = timeplus1_miss['LU57TRUU_AR']
mm = sum(listLU57TRUU_ARplus1_miss)
nn = len(listLU57TRUU_ARplus1_miss)
oo = mm/nn #AAR_miss(1)
listLU57TRUU_ARplus2_miss = timeplus2_miss['LU57TRUU_AR']
pp = sum(listLU57TRUU_ARplus2_miss)
rr = len(listLU57TRUU_ARplus2_miss)
ss = pp/rr #AAR_miss(2)
listLU57TRUU_ARplus3_miss = timeplus3_miss['LU57TRUU_AR']
tt = sum(listLU57TRUU_ARplus3_miss)
uu = len(listLU57TRUU_ARplus3_miss)
vv = tt/uu #AAR_miss(3)
CAARminus3_LU57TRUU_miss = cc
CAARminus2_LU57TRUU_miss = cc + ff
CAARminus1_LU57TRUU_miss = cc + ff + ii
CAARzero_LU57TRUU_miss = cc + ff + ii + ll
CAARplus1_LU57TRUU_miss = cc + ff + ii + ll + oo
CAARplus2_LU57TRUU_miss = cc + ff + ii + ll + oo + ss
CAARplus3_LU57TRUU_miss = cc + ff + ii + ll + oo + ss + vv
CAAR_LU57TRUU_miss = [CAARminus3_LU57TRUU_miss, CAARminus2_LU57TRUU_miss, CAARminus1_LU57TRUU_miss, CAARzero_LU57TRUU_miss, CAARplus1_LU57TRUU_miss, CAARplus2_LU57TRUU_miss, CAARplus3_LU57TRUU_miss]

fig6 = plt.figure(); ax6=fig6.add_subplot(1,1,1)
ax6.plot(time,CAAR_LU57TRUU_miss,'k--',color='blue',label=r'$CAAR$')
ax6.legend(loc='best')
ax6.set_xlabel(r'Time Horizon')
ax6.set_ylabel(r'CAAR LU57TRUU CPUPXCHG miss')

#LU71TRUU CPUPXCHG beat
listLU71TRUU_ARminus3_beat = timeminus3_beat['LU71TRUU_AR']
a = sum(listLU71TRUU_ARminus3_beat)
b = len(listLU71TRUU_ARminus3_beat)
c = a/b #AAR_beat(-3)
listLU71TRUU_ARminus2_beat = timeminus2_beat['LU71TRUU_AR']
d = sum(listLU71TRUU_ARminus2_beat)
e = len(listLU71TRUU_ARminus2_beat)
f = d/e #AAR_beat(-2)
listLU71TRUU_ARminus1_beat = timeminus1_beat['LU71TRUU_AR']
g = sum(listLU71TRUU_ARminus1_beat)
h = len(listLU71TRUU_ARminus1_beat)
i = g/h #AAR_beat(-1)
listLU71TRUU_ARzero_beat = timezero_beat['LU71TRUU_AR']
j = sum(listLU71TRUU_ARzero_beat)
k = len(listLU71TRUU_ARzero_beat)
l = j/k #AAR_beat(0)
listLU71TRUU_ARplus1_beat = timeplus1_beat['LU71TRUU_AR']
m = sum(listLU71TRUU_ARplus1_beat)
n = len(listLU71TRUU_ARplus1_beat)
o = m/n #AAR(1)
listLU71TRUU_ARplus2_beat = timeplus2_beat['LU71TRUU_AR']
p = sum(listLU71TRUU_ARplus2_beat)
r = len(listLU71TRUU_ARplus2_beat)
s = p/r #AAR_beat(2)
listLU71TRUU_ARplus3_beat = timeplus3_beat['LU71TRUU_AR']
t = sum(listLU71TRUU_ARplus3_beat)
u = len(listLU71TRUU_ARplus3_beat)
v = t/u #AAR(3)
CAARminus3_LU71TRUU_beat = c
CAARminus2_LU71TRUU_beat = c + f
CAARminus1_LU71TRUU_beat = c + f + i
CAARzero_LU71TRUU_beat = c + f + i + l
CAARplus1_LU71TRUU_beat = c + f + i + l + o
CAARplus2_LU71TRUU_beat = c + f + i + l + o + s
CAARplus3_LU71TRUU_beat = c + f + i + l + o + s + v
CAAR_LU71TRUU_beat = [CAARminus3_LU71TRUU_beat, CAARminus2_LU71TRUU_beat, CAARminus1_LU71TRUU_beat, CAARzero_LU71TRUU_beat, CAARplus1_LU71TRUU_beat, CAARplus2_LU71TRUU_beat, CAARplus3_LU71TRUU_beat]

fig7 = plt.figure(); ax7=fig7.add_subplot(1,1,1)
ax7.plot(time,CAAR_LU71TRUU_beat,'k--',color='blue',label=r'$CAAR$')
ax7.legend(loc='best')
ax7.set_xlabel(r'Time Horizon')
ax7.set_ylabel(r'CAAR LU71TRUU CPUPXCHG beat')

#LU71TRUU CPUPXCHG miss
listLU71TRUU_ARminus3_miss = timeminus3_miss['LU71TRUU_AR']
aa = sum(listLU71TRUU_ARminus3_miss)
bb = len(listLU71TRUU_ARminus3_miss)
cc = aa/bb #AAR_miss(-3)
listLU71TRUU_ARminus2_miss = timeminus2_miss['LU71TRUU_AR']
dd = sum(listLU71TRUU_ARminus2_miss)
ee = len(listLU71TRUU_ARminus2_miss)
ff = dd/ee #AAR_miss(-2)
listLU71TRUU_ARminus1_miss = timeminus1_miss['LU71TRUU_AR']
gg = sum(listLU71TRUU_ARminus1_miss)
hh = len(listLU71TRUU_ARminus1_miss)
ii = gg/hh #AAR_miss(-1)
listLU71TRUU_ARzero_miss = timezero_miss['LU71TRUU_AR']
jj = sum(listLU71TRUU_ARzero_miss)
kk = len(listLU71TRUU_ARzero_miss)
ll = jj/kk #AAR_miss(0)
listLU71TRUU_ARplus1_miss = timeplus1_miss['LU71TRUU_AR']
mm = sum(listLU71TRUU_ARplus1_miss)
nn = len(listLU71TRUU_ARplus1_miss)
oo = mm/nn #AAR_miss(1)
listLU71TRUU_ARplus2_miss = timeplus2_miss['LU71TRUU_AR']
pp = sum(listLU71TRUU_ARplus2_miss)
rr = len(listLU71TRUU_ARplus2_miss)
ss = pp/rr #AAR_miss(2)
listLU71TRUU_ARplus3_miss = timeplus3_miss['LU71TRUU_AR']
tt = sum(listLU71TRUU_ARplus3_miss)
uu = len(listLU71TRUU_ARplus3_miss)
vv = tt/uu #AAR_miss(3)
CAARminus3_LU71TRUU_miss = cc
CAARminus2_LU71TRUU_miss = cc + ff
CAARminus1_LU71TRUU_miss = cc + ff + ii
CAARzero_LU71TRUU_miss = cc + ff + ii + ll
CAARplus1_LU71TRUU_miss = cc + ff + ii + ll + oo
CAARplus2_LU71TRUU_miss = cc + ff + ii + ll + oo + ss
CAARplus3_LU71TRUU_miss = cc + ff + ii + ll + oo + ss + vv
CAAR_LU71TRUU_miss = [CAARminus3_LU71TRUU_miss, CAARminus2_LU71TRUU_miss, CAARminus1_LU71TRUU_miss, CAARzero_LU71TRUU_miss, CAARplus1_LU71TRUU_miss, CAARplus2_LU71TRUU_miss, CAARplus3_LU71TRUU_miss]

fig8 = plt.figure(); ax8=fig8.add_subplot(1,1,1)
ax8.plot(time,CAAR_LU71TRUU_miss,'k--',color='blue',label=r'$CAAR$')
ax8.legend(loc='best')
ax8.set_xlabel(r'Time Horizon')
ax8.set_ylabel(r'CAAR LU71TRUU CPUPXCHG miss')

#LU10TRUU CPUPXCHG beat
listLU10TRUU_ARminus3_beat = timeminus3_beat['LU10TRUU_AR']
a = sum(listLU10TRUU_ARminus3_beat)
b = len(listLU10TRUU_ARminus3_beat)
c = a/b #AAR_beat(-3)
listLU10TRUU_ARminus2_beat = timeminus2_beat['LU10TRUU_AR']
d = sum(listLU10TRUU_ARminus2_beat)
e = len(listLU10TRUU_ARminus2_beat)
f = d/e #AAR_beat(-2)
listLU10TRUU_ARminus1_beat = timeminus1_beat['LU10TRUU_AR']
g = sum(listLU10TRUU_ARminus1_beat)
h = len(listLU10TRUU_ARminus1_beat)
i = g/h #AAR_beat(-1)
listLU10TRUU_ARzero_beat = timezero_beat['LU10TRUU_AR']
j = sum(listLU10TRUU_ARzero_beat)
k = len(listLU10TRUU_ARzero_beat)
l = j/k #AAR_beat(0)
listLU10TRUU_ARplus1_beat = timeplus1_beat['LU10TRUU_AR']
m = sum(listLU10TRUU_ARplus1_beat)
n = len(listLU10TRUU_ARplus1_beat)
o = m/n #AAR(1)
listLU10TRUU_ARplus2_beat = timeplus2_beat['LU10TRUU_AR']
p = sum(listLU10TRUU_ARplus2_beat)
r = len(listLU10TRUU_ARplus2_beat)
s = p/r #AAR_beat(2)
listLU10TRUU_ARplus3_beat = timeplus3_beat['LU10TRUU_AR']
t = sum(listLU10TRUU_ARplus3_beat)
u = len(listLU10TRUU_ARplus3_beat)
v = t/u #AAR(3)
CAARminus3_LU10TRUU_beat = c
CAARminus2_LU10TRUU_beat = c + f
CAARminus1_LU10TRUU_beat = c + f + i
CAARzero_LU10TRUU_beat = c + f + i + l
CAARplus1_LU10TRUU_beat = c + f + i + l + o
CAARplus2_LU10TRUU_beat = c + f + i + l + o + s
CAARplus3_LU10TRUU_beat = c + f + i + l + o + s + v
CAAR_LU10TRUU_beat = [CAARminus3_LU10TRUU_beat, CAARminus2_LU10TRUU_beat, CAARminus1_LU10TRUU_beat, CAARzero_LU10TRUU_beat, CAARplus1_LU10TRUU_beat, CAARplus2_LU10TRUU_beat, CAARplus3_LU10TRUU_beat]

fig9 = plt.figure(); ax9=fig9.add_subplot(1,1,1)
ax9.plot(time,CAAR_LU10TRUU_beat,'k--',color='blue',label=r'$CAAR$')
ax9.legend(loc='best')
ax9.set_xlabel(r'Time Horizon')
ax9.set_ylabel(r'CAAR LU10TRUU CPUPXCHG beat')

#LU10TRUU CPUPXCHG miss
listLU10TRUU_ARminus3_miss = timeminus3_miss['LU10TRUU_AR']
aa = sum(listLU10TRUU_ARminus3_miss)
bb = len(listLU10TRUU_ARminus3_miss)
cc = aa/bb #AAR_miss(-3)
listLU10TRUU_ARminus2_miss = timeminus2_miss['LU10TRUU_AR']
dd = sum(listLU10TRUU_ARminus2_miss)
ee = len(listLU10TRUU_ARminus2_miss)
ff = dd/ee #AAR_miss(-2)
listLU10TRUU_ARminus1_miss = timeminus1_miss['LU10TRUU_AR']
gg = sum(listLU10TRUU_ARminus1_miss)
hh = len(listLU10TRUU_ARminus1_miss)
ii = gg/hh #AAR_miss(-1)
listLU10TRUU_ARzero_miss = timezero_miss['LU10TRUU_AR']
jj = sum(listLU10TRUU_ARzero_miss)
kk = len(listLU10TRUU_ARzero_miss)
ll = jj/kk #AAR_miss(0)
listLU10TRUU_ARplus1_miss = timeplus1_miss['LU10TRUU_AR']
mm = sum(listLU10TRUU_ARplus1_miss)
nn = len(listLU10TRUU_ARplus1_miss)
oo = mm/nn #AAR_miss(1)
listLU10TRUU_ARplus2_miss = timeplus2_miss['LU10TRUU_AR']
pp = sum(listLU10TRUU_ARplus2_miss)
rr = len(listLU10TRUU_ARplus2_miss)
ss = pp/rr #AAR_miss(2)
listLU10TRUU_ARplus3_miss = timeplus3_miss['LU10TRUU_AR']
tt = sum(listLU10TRUU_ARplus3_miss)
uu = len(listLU10TRUU_ARplus3_miss)
vv = tt/uu #AAR_miss(3)
CAARminus3_LU10TRUU_miss = cc
CAARminus2_LU10TRUU_miss = cc + ff
CAARminus1_LU10TRUU_miss = cc + ff + ii
CAARzero_LU10TRUU_miss = cc + ff + ii + ll
CAARplus1_LU10TRUU_miss = cc + ff + ii + ll + oo
CAARplus2_LU10TRUU_miss = cc + ff + ii + ll + oo + ss
CAARplus3_LU10TRUU_miss = cc + ff + ii + ll + oo + ss + vv
CAAR_LU10TRUU_miss = [CAARminus3_LU10TRUU_miss, CAARminus2_LU10TRUU_miss, CAARminus1_LU10TRUU_miss, CAARzero_LU10TRUU_miss, CAARplus1_LU10TRUU_miss, CAARplus2_LU10TRUU_miss, CAARplus3_LU10TRUU_miss]

fig10 = plt.figure(); ax10=fig10.add_subplot(1,1,1)
ax10.plot(time,CAAR_LU10TRUU_miss,'k--',color='blue',label=r'$CAAR$')
ax10.legend(loc='best')
ax10.set_xlabel(r'Time Horizon')
ax10.set_ylabel(r'CAAR LU10TRUU CPUPXCHG miss')

#LU3ATRUU CPUPXCHG beat
listLU3ATRUU_ARminus3_beat = timeminus3_beat['LU3ATRUU_AR']
a = sum(listLU3ATRUU_ARminus3_beat)
b = len(listLU3ATRUU_ARminus3_beat)
c = a/b #AAR_beat(-3)
listLU3ATRUU_ARminus2_beat = timeminus2_beat['LU3ATRUU_AR']
d = sum(listLU3ATRUU_ARminus2_beat)
e = len(listLU3ATRUU_ARminus2_beat)
f = d/e #AAR_beat(-2)
listLU3ATRUU_ARminus1_beat = timeminus1_beat['LU3ATRUU_AR']
g = sum(listLU3ATRUU_ARminus1_beat)
h = len(listLU3ATRUU_ARminus1_beat)
i = g/h #AAR_beat(-1)
listLU3ATRUU_ARzero_beat = timezero_beat['LU3ATRUU_AR']
j = sum(listLU3ATRUU_ARzero_beat)
k = len(listLU3ATRUU_ARzero_beat)
l = j/k #AAR_beat(0)
listLU3ATRUU_ARplus1_beat = timeplus1_beat['LU3ATRUU_AR']
m = sum(listLU3ATRUU_ARplus1_beat)
n = len(listLU3ATRUU_ARplus1_beat)
o = m/n #AAR(1)
listLU3ATRUU_ARplus2_beat = timeplus2_beat['LU3ATRUU_AR']
p = sum(listLU3ATRUU_ARplus2_beat)
r = len(listLU3ATRUU_ARplus2_beat)
s = p/r #AAR_beat(2)
listLU3ATRUU_ARplus3_beat = timeplus3_beat['LU3ATRUU_AR']
t = sum(listLU3ATRUU_ARplus3_beat)
u = len(listLU3ATRUU_ARplus3_beat)
v = t/u #AAR(3)
CAARminus3_LU3ATRUU_beat = c
CAARminus2_LU3ATRUU_beat = c + f
CAARminus1_LU3ATRUU_beat = c + f + i
CAARzero_LU3ATRUU_beat = c + f + i + l
CAARplus1_LU3ATRUU_beat = c + f + i + l + o
CAARplus2_LU3ATRUU_beat = c + f + i + l + o + s
CAARplus3_LU3ATRUU_beat = c + f + i + l + o + s + v
CAAR_LU3ATRUU_beat = [CAARminus3_LU3ATRUU_beat, CAARminus2_LU3ATRUU_beat, CAARminus1_LU3ATRUU_beat, CAARzero_LU3ATRUU_beat, CAARplus1_LU3ATRUU_beat, CAARplus2_LU3ATRUU_beat, CAARplus3_LU3ATRUU_beat]

fig11 = plt.figure(); ax11=fig11.add_subplot(1,1,1)
ax11.plot(time,CAAR_LU3ATRUU_beat,'k--',color='blue',label=r'$CAAR$')
ax11.legend(loc='best')
ax11.set_xlabel(r'Time Horizon')
ax11.set_ylabel(r'CAAR LU3ATRUU CPUPXCHG beat')

#LU3ATRUU CPUPXCHG miss
listLU3ATRUU_ARminus3_miss = timeminus3_miss['LU3ATRUU_AR']
aa = sum(listLU3ATRUU_ARminus3_miss)
bb = len(listLU3ATRUU_ARminus3_miss)
cc = aa/bb #AAR_miss(-3)
listLU3ATRUU_ARminus2_miss = timeminus2_miss['LU3ATRUU_AR']
dd = sum(listLU3ATRUU_ARminus2_miss)
ee = len(listLU3ATRUU_ARminus2_miss)
ff = dd/ee #AAR_miss(-2)
listLU3ATRUU_ARminus1_miss = timeminus1_miss['LU3ATRUU_AR']
gg = sum(listLU3ATRUU_ARminus1_miss)
hh = len(listLU3ATRUU_ARminus1_miss)
ii = gg/hh #AAR_miss(-1)
listLU3ATRUU_ARzero_miss = timezero_miss['LU3ATRUU_AR']
jj = sum(listLU3ATRUU_ARzero_miss)
kk = len(listLU3ATRUU_ARzero_miss)
ll = jj/kk #AAR_miss(0)
listLU3ATRUU_ARplus1_miss = timeplus1_miss['LU3ATRUU_AR']
mm = sum(listLU3ATRUU_ARplus1_miss)
nn = len(listLU3ATRUU_ARplus1_miss)
oo = mm/nn #AAR_miss(1)
listLU3ATRUU_ARplus2_miss = timeplus2_miss['LU3ATRUU_AR']
pp = sum(listLU3ATRUU_ARplus2_miss)
rr = len(listLU3ATRUU_ARplus2_miss)
ss = pp/rr #AAR_miss(2)
listLU3ATRUU_ARplus3_miss = timeplus3_miss['LU3ATRUU_AR']
tt = sum(listLU3ATRUU_ARplus3_miss)
uu = len(listLU3ATRUU_ARplus3_miss)
vv = tt/uu #AAR_miss(3)
CAARminus3_LU3ATRUU_miss = cc
CAARminus2_LU3ATRUU_miss = cc + ff
CAARminus1_LU3ATRUU_miss = cc + ff + ii
CAARzero_LU3ATRUU_miss = cc + ff + ii + ll
CAARplus1_LU3ATRUU_miss = cc + ff + ii + ll + oo
CAARplus2_LU3ATRUU_miss = cc + ff + ii + ll + oo + ss
CAARplus3_LU3ATRUU_miss = cc + ff + ii + ll + oo + ss + vv
CAAR_LU3ATRUU_miss = [CAARminus3_LU3ATRUU_miss, CAARminus2_LU3ATRUU_miss, CAARminus1_LU3ATRUU_miss, CAARzero_LU3ATRUU_miss, CAARplus1_LU3ATRUU_miss, CAARplus2_LU3ATRUU_miss, CAARplus3_LU3ATRUU_miss]

fig12 = plt.figure(); ax12=fig12.add_subplot(1,1,1)
ax12.plot(time,CAAR_LU3ATRUU_miss,'k--',color='blue',label=r'$CAAR$')
ax12.legend(loc='best')
ax12.set_xlabel(r'Time Horizon')
ax12.set_ylabel(r'CAAR LU3ATRUU CPUPXCHG miss')

#LU2ATRUU CPUPXCHG beat
listLU2ATRUU_ARminus3_beat = timeminus3_beat['LU2ATRUU_AR']
a = sum(listLU2ATRUU_ARminus3_beat)
b = len(listLU2ATRUU_ARminus3_beat)
c = a/b #AAR_beat(-3)
listLU2ATRUU_ARminus2_beat = timeminus2_beat['LU2ATRUU_AR']
d = sum(listLU2ATRUU_ARminus2_beat)
e = len(listLU2ATRUU_ARminus2_beat)
f = d/e #AAR_beat(-2)
listLU2ATRUU_ARminus1_beat = timeminus1_beat['LU2ATRUU_AR']
g = sum(listLU2ATRUU_ARminus1_beat)
h = len(listLU2ATRUU_ARminus1_beat)
i = g/h #AAR_beat(-1)
listLU2ATRUU_ARzero_beat = timezero_beat['LU2ATRUU_AR']
j = sum(listLU2ATRUU_ARzero_beat)
k = len(listLU2ATRUU_ARzero_beat)
l = j/k #AAR_beat(0)
listLU2ATRUU_ARplus1_beat = timeplus1_beat['LU2ATRUU_AR']
m = sum(listLU2ATRUU_ARplus1_beat)
n = len(listLU2ATRUU_ARplus1_beat)
o = m/n #AAR(1)
listLU2ATRUU_ARplus2_beat = timeplus2_beat['LU2ATRUU_AR']
p = sum(listLU2ATRUU_ARplus2_beat)
r = len(listLU2ATRUU_ARplus2_beat)
s = p/r #AAR_beat(2)
listLU2ATRUU_ARplus3_beat = timeplus3_beat['LU2ATRUU_AR']
t = sum(listLU2ATRUU_ARplus3_beat)
u = len(listLU2ATRUU_ARplus3_beat)
v = t/u #AAR(3)
CAARminus3_LU2ATRUU_beat = c
CAARminus2_LU2ATRUU_beat = c + f
CAARminus1_LU2ATRUU_beat = c + f + i
CAARzero_LU2ATRUU_beat = c + f + i + l
CAARplus1_LU2ATRUU_beat = c + f + i + l + o
CAARplus2_LU2ATRUU_beat = c + f + i + l + o + s
CAARplus3_LU2ATRUU_beat = c + f + i + l + o + s + v
CAAR_LU2ATRUU_beat = [CAARminus3_LU2ATRUU_beat, CAARminus2_LU2ATRUU_beat, CAARminus1_LU2ATRUU_beat, CAARzero_LU2ATRUU_beat, CAARplus1_LU2ATRUU_beat, CAARplus2_LU2ATRUU_beat, CAARplus3_LU2ATRUU_beat]

fig13 = plt.figure(); ax13=fig13.add_subplot(1,1,1)
ax13.plot(time,CAAR_LU2ATRUU_beat,'k--',color='blue',label=r'$CAAR$')
ax13.legend(loc='best')
ax13.set_xlabel(r'Time Horizon')
ax13.set_ylabel(r'CAAR LU2ATRUU CPUPXCHG beat')

#LU2ATRUU CPUPXCHG miss
listLU2ATRUU_ARminus3_miss = timeminus3_miss['LU2ATRUU_AR']
aa = sum(listLU2ATRUU_ARminus3_miss)
bb = len(listLU2ATRUU_ARminus3_miss)
cc = aa/bb #AAR_miss(-3)
listLU2ATRUU_ARminus2_miss = timeminus2_miss['LU2ATRUU_AR']
dd = sum(listLU2ATRUU_ARminus2_miss)
ee = len(listLU2ATRUU_ARminus2_miss)
ff = dd/ee #AAR_miss(-2)
listLU2ATRUU_ARminus1_miss = timeminus1_miss['LU2ATRUU_AR']
gg = sum(listLU2ATRUU_ARminus1_miss)
hh = len(listLU2ATRUU_ARminus1_miss)
ii = gg/hh #AAR_miss(-1)
listLU2ATRUU_ARzero_miss = timezero_miss['LU2ATRUU_AR']
jj = sum(listLU2ATRUU_ARzero_miss)
kk = len(listLU2ATRUU_ARzero_miss)
ll = jj/kk #AAR_miss(0)
listLU2ATRUU_ARplus1_miss = timeplus1_miss['LU2ATRUU_AR']
mm = sum(listLU2ATRUU_ARplus1_miss)
nn = len(listLU2ATRUU_ARplus1_miss)
oo = mm/nn #AAR_miss(1)
listLU2ATRUU_ARplus2_miss = timeplus2_miss['LU2ATRUU_AR']
pp = sum(listLU2ATRUU_ARplus2_miss)
rr = len(listLU2ATRUU_ARplus2_miss)
ss = pp/rr #AAR_miss(2)
listLU2ATRUU_ARplus3_miss = timeplus3_miss['LU2ATRUU_AR']
tt = sum(listLU2ATRUU_ARplus3_miss)
uu = len(listLU2ATRUU_ARplus3_miss)
vv = tt/uu #AAR_miss(3)
CAARminus3_LU2ATRUU_miss = cc
CAARminus2_LU2ATRUU_miss = cc + ff
CAARminus1_LU2ATRUU_miss = cc + ff + ii
CAARzero_LU2ATRUU_miss = cc + ff + ii + ll
CAARplus1_LU2ATRUU_miss = cc + ff + ii + ll + oo
CAARplus2_LU2ATRUU_miss = cc + ff + ii + ll + oo + ss
CAARplus3_LU2ATRUU_miss = cc + ff + ii + ll + oo + ss + vv
CAAR_LU2ATRUU_miss = [CAARminus3_LU2ATRUU_miss, CAARminus2_LU2ATRUU_miss, CAARminus1_LU2ATRUU_miss, CAARzero_LU2ATRUU_miss, CAARplus1_LU2ATRUU_miss, CAARplus2_LU2ATRUU_miss, CAARplus3_LU2ATRUU_miss]

fig14 = plt.figure(); ax14=fig14.add_subplot(1,1,1)
ax14.plot(time,CAAR_LU2ATRUU_miss,'k--',color='blue',label=r'$CAAR$')
ax14.legend(loc='best')
ax14.set_xlabel(r'Time Horizon')
ax14.set_ylabel(r'CAAR LU2ATRUU CPUPXCHG miss')

#LU1ATRUU CPUPXCHG beat
listLU1ATRUU_ARminus3_beat = timeminus3_beat['LU1ATRUU_AR']
a = sum(listLU1ATRUU_ARminus3_beat)
b = len(listLU1ATRUU_ARminus3_beat)
c = a/b #AAR_beat(-3)
listLU1ATRUU_ARminus2_beat = timeminus2_beat['LU1ATRUU_AR']
d = sum(listLU1ATRUU_ARminus2_beat)
e = len(listLU1ATRUU_ARminus2_beat)
f = d/e #AAR_beat(-2)
listLU1ATRUU_ARminus1_beat = timeminus1_beat['LU1ATRUU_AR']
g = sum(listLU1ATRUU_ARminus1_beat)
h = len(listLU1ATRUU_ARminus1_beat)
i = g/h #AAR_beat(-1)
listLU1ATRUU_ARzero_beat = timezero_beat['LU1ATRUU_AR']
j = sum(listLU1ATRUU_ARzero_beat)
k = len(listLU1ATRUU_ARzero_beat)
l = j/k #AAR_beat(0)
listLU1ATRUU_ARplus1_beat = timeplus1_beat['LU1ATRUU_AR']
m = sum(listLU1ATRUU_ARplus1_beat)
n = len(listLU1ATRUU_ARplus1_beat)
o = m/n #AAR(1)
listLU1ATRUU_ARplus2_beat = timeplus2_beat['LU1ATRUU_AR']
p = sum(listLU1ATRUU_ARplus2_beat)
r = len(listLU1ATRUU_ARplus2_beat)
s = p/r #AAR_beat(2)
listLU1ATRUU_ARplus3_beat = timeplus3_beat['LU1ATRUU_AR']
t = sum(listLU1ATRUU_ARplus3_beat)
u = len(listLU1ATRUU_ARplus3_beat)
v = t/u #AAR(3)
CAARminus3_LU1ATRUU_beat = c
CAARminus2_LU1ATRUU_beat = c + f
CAARminus1_LU1ATRUU_beat = c + f + i
CAARzero_LU1ATRUU_beat = c + f + i + l
CAARplus1_LU1ATRUU_beat = c + f + i + l + o
CAARplus2_LU1ATRUU_beat = c + f + i + l + o + s
CAARplus3_LU1ATRUU_beat = c + f + i + l + o + s + v
CAAR_LU1ATRUU_beat = [CAARminus3_LU1ATRUU_beat, CAARminus2_LU1ATRUU_beat, CAARminus1_LU1ATRUU_beat, CAARzero_LU1ATRUU_beat, CAARplus1_LU1ATRUU_beat, CAARplus2_LU1ATRUU_beat, CAARplus3_LU1ATRUU_beat]

fig15 = plt.figure(); ax15=fig15.add_subplot(1,1,1)
ax15.plot(time,CAAR_LU1ATRUU_beat,'k--',color='blue',label=r'$CAAR$')
ax15.legend(loc='best')
ax15.set_xlabel(r'Time Horizon')
ax15.set_ylabel(r'CAAR LU1ATRUU CPUPXCHG beat')

#LU1ATRUU CPUPXCHG miss
listLU1ATRUU_ARminus3_miss = timeminus3_miss['LU1ATRUU_AR']
aa = sum(listLU1ATRUU_ARminus3_miss)
bb = len(listLU1ATRUU_ARminus3_miss)
cc = aa/bb #AAR_miss(-3)
listLU1ATRUU_ARminus2_miss = timeminus2_miss['LU1ATRUU_AR']
dd = sum(listLU1ATRUU_ARminus2_miss)
ee = len(listLU1ATRUU_ARminus2_miss)
ff = dd/ee #AAR_miss(-2)
listLU1ATRUU_ARminus1_miss = timeminus1_miss['LU1ATRUU_AR']
gg = sum(listLU1ATRUU_ARminus1_miss)
hh = len(listLU1ATRUU_ARminus1_miss)
ii = gg/hh #AAR_miss(-1)
listLU1ATRUU_ARzero_miss = timezero_miss['LU1ATRUU_AR']
jj = sum(listLU1ATRUU_ARzero_miss)
kk = len(listLU1ATRUU_ARzero_miss)
ll = jj/kk #AAR_miss(0)
listLU1ATRUU_ARplus1_miss = timeplus1_miss['LU1ATRUU_AR']
mm = sum(listLU1ATRUU_ARplus1_miss)
nn = len(listLU1ATRUU_ARplus1_miss)
oo = mm/nn #AAR_miss(1)
listLU1ATRUU_ARplus2_miss = timeplus2_miss['LU1ATRUU_AR']
pp = sum(listLU1ATRUU_ARplus2_miss)
rr = len(listLU1ATRUU_ARplus2_miss)
ss = pp/rr #AAR_miss(2)
listLU1ATRUU_ARplus3_miss = timeplus3_miss['LU1ATRUU_AR']
tt = sum(listLU1ATRUU_ARplus3_miss)
uu = len(listLU1ATRUU_ARplus3_miss)
vv = tt/uu #AAR_miss(3)
CAARminus3_LU1ATRUU_miss = cc
CAARminus2_LU1ATRUU_miss = cc + ff
CAARminus1_LU1ATRUU_miss = cc + ff + ii
CAARzero_LU1ATRUU_miss = cc + ff + ii + ll
CAARplus1_LU1ATRUU_miss = cc + ff + ii + ll + oo
CAARplus2_LU1ATRUU_miss = cc + ff + ii + ll + oo + ss
CAARplus3_LU1ATRUU_miss = cc + ff + ii + ll + oo + ss + vv
CAAR_LU1ATRUU_miss = [CAARminus3_LU1ATRUU_miss, CAARminus2_LU1ATRUU_miss, CAARminus1_LU1ATRUU_miss, CAARzero_LU1ATRUU_miss, CAARplus1_LU1ATRUU_miss, CAARplus2_LU1ATRUU_miss, CAARplus3_LU1ATRUU_miss]

fig16 = plt.figure(); ax16=fig16.add_subplot(1,1,1)
ax16.plot(time,CAAR_LU1ATRUU_miss,'k--',color='blue',label=r'$CAAR$')
ax16.legend(loc='best')
ax16.set_xlabel(r'Time Horizon')
ax16.set_ylabel(r'CAAR LU1ATRUU CPUPXCHG miss')

#LUBATRUU CPUPXCHG beat
listLUBATRUU_ARminus3_beat = timeminus3_beat['LUBATRUU_AR']
a = sum(listLUBATRUU_ARminus3_beat)
b = len(listLUBATRUU_ARminus3_beat)
c = a/b #AAR_beat(-3)
listLUBATRUU_ARminus2_beat = timeminus2_beat['LUBATRUU_AR']
d = sum(listLUBATRUU_ARminus2_beat)
e = len(listLUBATRUU_ARminus2_beat)
f = d/e #AAR_beat(-2)
listLUBATRUU_ARminus1_beat = timeminus1_beat['LUBATRUU_AR']
g = sum(listLUBATRUU_ARminus1_beat)
h = len(listLUBATRUU_ARminus1_beat)
i = g/h #AAR_beat(-1)
listLUBATRUU_ARzero_beat = timezero_beat['LUBATRUU_AR']
j = sum(listLUBATRUU_ARzero_beat)
k = len(listLUBATRUU_ARzero_beat)
l = j/k #AAR_beat(0)
listLUBATRUU_ARplus1_beat = timeplus1_beat['LUBATRUU_AR']
m = sum(listLUBATRUU_ARplus1_beat)
n = len(listLUBATRUU_ARplus1_beat)
o = m/n #AAR(1)
listLUBATRUU_ARplus2_beat = timeplus2_beat['LUBATRUU_AR']
p = sum(listLUBATRUU_ARplus2_beat)
r = len(listLUBATRUU_ARplus2_beat)
s = p/r #AAR_beat(2)
listLUBATRUU_ARplus3_beat = timeplus3_beat['LUBATRUU_AR']
t = sum(listLUBATRUU_ARplus3_beat)
u = len(listLUBATRUU_ARplus3_beat)
v = t/u #AAR(3)
CAARminus3_LUBATRUU_beat = c
CAARminus2_LUBATRUU_beat = c + f
CAARminus1_LUBATRUU_beat = c + f + i
CAARzero_LUBATRUU_beat = c + f + i + l
CAARplus1_LUBATRUU_beat = c + f + i + l + o
CAARplus2_LUBATRUU_beat = c + f + i + l + o + s
CAARplus3_LUBATRUU_beat = c + f + i + l + o + s + v
CAAR_LUBATRUU_beat = [CAARminus3_LUBATRUU_beat, CAARminus2_LUBATRUU_beat, CAARminus1_LUBATRUU_beat, CAARzero_LUBATRUU_beat, CAARplus1_LUBATRUU_beat, CAARplus2_LUBATRUU_beat, CAARplus3_LUBATRUU_beat]

fig17 = plt.figure(); ax17=fig17.add_subplot(1,1,1)
ax17.plot(time,CAAR_LUBATRUU_beat,'k--',color='blue',label=r'$CAAR$')
ax17.legend(loc='best')
ax17.set_xlabel(r'Time Horizon')
ax17.set_ylabel(r'CAAR LUBATRUU CPUPXCHG beat')

#LUBATRUU CPUPXCHG miss
listLUBATRUU_ARminus3_miss = timeminus3_miss['LUBATRUU_AR']
aa = sum(listLUBATRUU_ARminus3_miss)
bb = len(listLUBATRUU_ARminus3_miss)
cc = aa/bb #AAR_miss(-3)
listLUBATRUU_ARminus2_miss = timeminus2_miss['LUBATRUU_AR']
dd = sum(listLUBATRUU_ARminus2_miss)
ee = len(listLUBATRUU_ARminus2_miss)
ff = dd/ee #AAR_miss(-2)
listLUBATRUU_ARminus1_miss = timeminus1_miss['LUBATRUU_AR']
gg = sum(listLUBATRUU_ARminus1_miss)
hh = len(listLUBATRUU_ARminus1_miss)
ii = gg/hh #AAR_miss(-1)
listLUBATRUU_ARzero_miss = timezero_miss['LUBATRUU_AR']
jj = sum(listLUBATRUU_ARzero_miss)
kk = len(listLUBATRUU_ARzero_miss)
ll = jj/kk #AAR_miss(0)
listLUBATRUU_ARplus1_miss = timeplus1_miss['LUBATRUU_AR']
mm = sum(listLUBATRUU_ARplus1_miss)
nn = len(listLUBATRUU_ARplus1_miss)
oo = mm/nn #AAR_miss(1)
listLUBATRUU_ARplus2_miss = timeplus2_miss['LUBATRUU_AR']
pp = sum(listLUBATRUU_ARplus2_miss)
rr = len(listLUBATRUU_ARplus2_miss)
ss = pp/rr #AAR_miss(2)
listLUBATRUU_ARplus3_miss = timeplus3_miss['LUBATRUU_AR']
tt = sum(listLUBATRUU_ARplus3_miss)
uu = len(listLUBATRUU_ARplus3_miss)
vv = tt/uu #AAR_miss(3)
CAARminus3_LUBATRUU_miss = cc
CAARminus2_LUBATRUU_miss = cc + ff
CAARminus1_LUBATRUU_miss = cc + ff + ii
CAARzero_LUBATRUU_miss = cc + ff + ii + ll
CAARplus1_LUBATRUU_miss = cc + ff + ii + ll + oo
CAARplus2_LUBATRUU_miss = cc + ff + ii + ll + oo + ss
CAARplus3_LUBATRUU_miss = cc + ff + ii + ll + oo + ss + vv
CAAR_LUBATRUU_miss = [CAARminus3_LUBATRUU_miss, CAARminus2_LUBATRUU_miss, CAARminus1_LUBATRUU_miss, CAARzero_LUBATRUU_miss, CAARplus1_LUBATRUU_miss, CAARplus2_LUBATRUU_miss, CAARplus3_LUBATRUU_miss]

fig18 = plt.figure(); ax18=fig18.add_subplot(1,1,1)
ax18.plot(time,CAAR_LUBATRUU_miss,'k--',color='blue',label=r'$CAAR$')
ax18.legend(loc='best')
ax18.set_xlabel(r'Time Horizon')
ax18.set_ylabel(r'CAAR LUBATRUU CPUPXCHG miss')

#LUATTRUU CPUPXCHG beat
listLUATTRUU_ARminus3_beat = timeminus3_beat['LUATTRUU_AR']
a = sum(listLUATTRUU_ARminus3_beat)
b = len(listLUATTRUU_ARminus3_beat)
c = a/b #AAR_beat(-3)
listLUATTRUU_ARminus2_beat = timeminus2_beat['LUATTRUU_AR']
d = sum(listLUATTRUU_ARminus2_beat)
e = len(listLUATTRUU_ARminus2_beat)
f = d/e #AAR_beat(-2)
listLUATTRUU_ARminus1_beat = timeminus1_beat['LUATTRUU_AR']
g = sum(listLUATTRUU_ARminus1_beat)
h = len(listLUATTRUU_ARminus1_beat)
i = g/h #AAR_beat(-1)
listLUATTRUU_ARzero_beat = timezero_beat['LUATTRUU_AR']
j = sum(listLUATTRUU_ARzero_beat)
k = len(listLUATTRUU_ARzero_beat)
l = j/k #AAR_beat(0)
listLUATTRUU_ARplus1_beat = timeplus1_beat['LUATTRUU_AR']
m = sum(listLUATTRUU_ARplus1_beat)
n = len(listLUATTRUU_ARplus1_beat)
o = m/n #AAR(1)
listLUATTRUU_ARplus2_beat = timeplus2_beat['LUATTRUU_AR']
p = sum(listLUATTRUU_ARplus2_beat)
r = len(listLUATTRUU_ARplus2_beat)
s = p/r #AAR_beat(2)
listLUATTRUU_ARplus3_beat = timeplus3_beat['LUATTRUU_AR']
t = sum(listLUATTRUU_ARplus3_beat)
u = len(listLUATTRUU_ARplus3_beat)
v = t/u #AAR(3)
CAARminus3_LUATTRUU_beat = c
CAARminus2_LUATTRUU_beat = c + f
CAARminus1_LUATTRUU_beat = c + f + i
CAARzero_LUATTRUU_beat = c + f + i + l
CAARplus1_LUATTRUU_beat = c + f + i + l + o
CAARplus2_LUATTRUU_beat = c + f + i + l + o + s
CAARplus3_LUATTRUU_beat = c + f + i + l + o + s + v
CAAR_LUATTRUU_beat = [CAARminus3_LUATTRUU_beat, CAARminus2_LUATTRUU_beat, CAARminus1_LUATTRUU_beat, CAARzero_LUATTRUU_beat, CAARplus1_LUATTRUU_beat, CAARplus2_LUATTRUU_beat, CAARplus3_LUATTRUU_beat]

fig19 = plt.figure(); ax19=fig19.add_subplot(1,1,1)
ax19.plot(time,CAAR_LUATTRUU_beat,'k--',color='blue',label=r'$CAAR$')
ax19.legend(loc='best')
ax19.set_xlabel(r'Time Horizon')
ax19.set_ylabel(r'CAAR LUATTRUU CPUPXCHG beat')

#LUATTRUU CPUPXCHG miss
listLUATTRUU_ARminus3_miss = timeminus3_miss['LUATTRUU_AR']
aa = sum(listLUATTRUU_ARminus3_miss)
bb = len(listLUATTRUU_ARminus3_miss)
cc = aa/bb #AAR_miss(-3)
listLUATTRUU_ARminus2_miss = timeminus2_miss['LUATTRUU_AR']
dd = sum(listLUATTRUU_ARminus2_miss)
ee = len(listLUATTRUU_ARminus2_miss)
ff = dd/ee #AAR_miss(-2)
listLUATTRUU_ARminus1_miss = timeminus1_miss['LUATTRUU_AR']
gg = sum(listLUATTRUU_ARminus1_miss)
hh = len(listLUATTRUU_ARminus1_miss)
ii = gg/hh #AAR_miss(-1)
listLUATTRUU_ARzero_miss = timezero_miss['LUATTRUU_AR']
jj = sum(listLUATTRUU_ARzero_miss)
kk = len(listLUATTRUU_ARzero_miss)
ll = jj/kk #AAR_miss(0)
listLUATTRUU_ARplus1_miss = timeplus1_miss['LUATTRUU_AR']
mm = sum(listLUATTRUU_ARplus1_miss)
nn = len(listLUATTRUU_ARplus1_miss)
oo = mm/nn #AAR_miss(1)
listLUATTRUU_ARplus2_miss = timeplus2_miss['LUATTRUU_AR']
pp = sum(listLUATTRUU_ARplus2_miss)
rr = len(listLUATTRUU_ARplus2_miss)
ss = pp/rr #AAR_miss(2)
listLUATTRUU_ARplus3_miss = timeplus3_miss['LUATTRUU_AR']
tt = sum(listLUATTRUU_ARplus3_miss)
uu = len(listLUATTRUU_ARplus3_miss)
vv = tt/uu #AAR_miss(3)
CAARminus3_LUATTRUU_miss = cc
CAARminus2_LUATTRUU_miss = cc + ff
CAARminus1_LUATTRUU_miss = cc + ff + ii
CAARzero_LUATTRUU_miss = cc + ff + ii + ll
CAARplus1_LUATTRUU_miss = cc + ff + ii + ll + oo
CAARplus2_LUATTRUU_miss = cc + ff + ii + ll + oo + ss
CAARplus3_LUATTRUU_miss = cc + ff + ii + ll + oo + ss + vv
CAAR_LUATTRUU_miss = [CAARminus3_LUATTRUU_miss, CAARminus2_LUATTRUU_miss, CAARminus1_LUATTRUU_miss, CAARzero_LUATTRUU_miss, CAARplus1_LUATTRUU_miss, CAARplus2_LUATTRUU_miss, CAARplus3_LUATTRUU_miss]

fig20 = plt.figure(); ax20=fig20.add_subplot(1,1,1)
ax20.plot(time,CAAR_LUATTRUU_miss,'k--',color='blue',label=r'$CAAR$')
ax20.legend(loc='best')
ax20.set_xlabel(r'Time Horizon')
ax20.set_ylabel(r'CAAR LUATTRUU CPUPXCHG miss')

#LUACTRUU CPUPXCHG beat
listLUACTRUU_ARminus3_beat = timeminus3_beat['LUACTRUU_AR']
a = sum(listLUACTRUU_ARminus3_beat)
b = len(listLUACTRUU_ARminus3_beat)
c = a/b #AAR_beat(-3)
listLUACTRUU_ARminus2_beat = timeminus2_beat['LUACTRUU_AR']
d = sum(listLUACTRUU_ARminus2_beat)
e = len(listLUACTRUU_ARminus2_beat)
f = d/e #AAR_beat(-2)
listLUACTRUU_ARminus1_beat = timeminus1_beat['LUACTRUU_AR']
g = sum(listLUACTRUU_ARminus1_beat)
h = len(listLUACTRUU_ARminus1_beat)
i = g/h #AAR_beat(-1)
listLUACTRUU_ARzero_beat = timezero_beat['LUACTRUU_AR']
j = sum(listLUACTRUU_ARzero_beat)
k = len(listLUACTRUU_ARzero_beat)
l = j/k #AAR_beat(0)
listLUACTRUU_ARplus1_beat = timeplus1_beat['LUACTRUU_AR']
m = sum(listLUACTRUU_ARplus1_beat)
n = len(listLUACTRUU_ARplus1_beat)
o = m/n #AAR(1)
listLUACTRUU_ARplus2_beat = timeplus2_beat['LUACTRUU_AR']
p = sum(listLUACTRUU_ARplus2_beat)
r = len(listLUACTRUU_ARplus2_beat)
s = p/r #AAR_beat(2)
listLUACTRUU_ARplus3_beat = timeplus3_beat['LUACTRUU_AR']
t = sum(listLUACTRUU_ARplus3_beat)
u = len(listLUACTRUU_ARplus3_beat)
v = t/u #AAR(3)
CAARminus3_LUACTRUU_beat = c
CAARminus2_LUACTRUU_beat = c + f
CAARminus1_LUACTRUU_beat = c + f + i
CAARzero_LUACTRUU_beat = c + f + i + l
CAARplus1_LUACTRUU_beat = c + f + i + l + o
CAARplus2_LUACTRUU_beat = c + f + i + l + o + s
CAARplus3_LUACTRUU_beat = c + f + i + l + o + s + v
CAAR_LUACTRUU_beat = [CAARminus3_LUACTRUU_beat, CAARminus2_LUACTRUU_beat, CAARminus1_LUACTRUU_beat, CAARzero_LUACTRUU_beat, CAARplus1_LUACTRUU_beat, CAARplus2_LUACTRUU_beat, CAARplus3_LUACTRUU_beat]

fig21 = plt.figure(); ax21=fig21.add_subplot(1,1,1)
ax21.plot(time,CAAR_LUACTRUU_beat,'k--',color='blue',label=r'$CAAR$')
ax21.legend(loc='best')
ax21.set_xlabel(r'Time Horizon')
ax21.set_ylabel(r'CAAR LUACTRUU CPUPXCHG beat')

#LUACTRUU CPUPXCHG miss
listLUACTRUU_ARminus3_miss = timeminus3_miss['LUACTRUU_AR']
aa = sum(listLUACTRUU_ARminus3_miss)
bb = len(listLUACTRUU_ARminus3_miss)
cc = aa/bb #AAR_miss(-3)
listLUACTRUU_ARminus2_miss = timeminus2_miss['LUACTRUU_AR']
dd = sum(listLUACTRUU_ARminus2_miss)
ee = len(listLUACTRUU_ARminus2_miss)
ff = dd/ee #AAR_miss(-2)
listLUACTRUU_ARminus1_miss = timeminus1_miss['LUACTRUU_AR']
gg = sum(listLUACTRUU_ARminus1_miss)
hh = len(listLUACTRUU_ARminus1_miss)
ii = gg/hh #AAR_miss(-1)
listLUACTRUU_ARzero_miss = timezero_miss['LUACTRUU_AR']
jj = sum(listLUACTRUU_ARzero_miss)
kk = len(listLUACTRUU_ARzero_miss)
ll = jj/kk #AAR_miss(0)
listLUACTRUU_ARplus1_miss = timeplus1_miss['LUACTRUU_AR']
mm = sum(listLUACTRUU_ARplus1_miss)
nn = len(listLUACTRUU_ARplus1_miss)
oo = mm/nn #AAR_miss(1)
listLUACTRUU_ARplus2_miss = timeplus2_miss['LUACTRUU_AR']
pp = sum(listLUACTRUU_ARplus2_miss)
rr = len(listLUACTRUU_ARplus2_miss)
ss = pp/rr #AAR_miss(2)
listLUACTRUU_ARplus3_miss = timeplus3_miss['LUACTRUU_AR']
tt = sum(listLUACTRUU_ARplus3_miss)
uu = len(listLUACTRUU_ARplus3_miss)
vv = tt/uu #AAR_miss(3)
CAARminus3_LUACTRUU_miss = cc
CAARminus2_LUACTRUU_miss = cc + ff
CAARminus1_LUACTRUU_miss = cc + ff + ii
CAARzero_LUACTRUU_miss = cc + ff + ii + ll
CAARplus1_LUACTRUU_miss = cc + ff + ii + ll + oo
CAARplus2_LUACTRUU_miss = cc + ff + ii + ll + oo + ss
CAARplus3_LUACTRUU_miss = cc + ff + ii + ll + oo + ss + vv
CAAR_LUACTRUU_miss = [CAARminus3_LUACTRUU_miss, CAARminus2_LUACTRUU_miss, CAARminus1_LUACTRUU_miss, CAARzero_LUACTRUU_miss, CAARplus1_LUACTRUU_miss, CAARplus2_LUACTRUU_miss, CAARplus3_LUACTRUU_miss]

fig22 = plt.figure(); ax22=fig22.add_subplot(1,1,1)
ax22.plot(time,CAAR_LUACTRUU_miss,'k--',color='blue',label=r'$CAAR$')
ax22.legend(loc='best')
ax22.set_xlabel(r'Time Horizon')
ax22.set_ylabel(r'CAAR LUACTRUU CPUPXCHG miss')