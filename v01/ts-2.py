import pandas as pd
from pandas import DataFrame

#import data from Excel
ReadExcel = pd.read_excel (r'C:\Users\asus\Documents\Python-Vaje\ts-01.xlsx', '2beat')
df_beat = DataFrame(ReadExcel,columns=['Date','IB8A_AR', 'QW1A_AR', 'window_beat_ECCPEMUY'])
df_beat.dropna(inplace=True)
#print (df_beat)

ReadExcel = pd.read_excel (r'C:\Users\asus\Documents\Python-Vaje\ts-01.xlsx', '2miss')
df_miss = DataFrame(ReadExcel,columns=['Date','IB8A_AR', 'QW1A_AR', 'window_miss_ECCPEMUY'])
df_miss.dropna(inplace=True)
#print (df_miss)

#IB8A ECCPEMUY beat
timeminus3_beat = df_beat[df_beat.window_beat_ECCPEMUY == -3]
listIB8A_ARminus3_beat = timeminus3_beat['IB8A_AR']
a = sum(listIB8A_ARminus3_beat)
b = len(listIB8A_ARminus3_beat)
c = a/b #AAR_beat(-3)
timeminus2_beat = df_beat[df_beat.window_beat_ECCPEMUY == -2]
listIB8A_ARminus2_beat = timeminus2_beat['IB8A_AR']
d = sum(listIB8A_ARminus2_beat)
e = len(listIB8A_ARminus2_beat)
f = d/e #AAR_beat(-2)
timeminus1_beat = df_beat[df_beat.window_beat_ECCPEMUY == -1]
listIB8A_ARminus1_beat = timeminus1_beat['IB8A_AR']
g = sum(listIB8A_ARminus1_beat)
h = len(listIB8A_ARminus1_beat)
i = g/h #AAR_beat(-1)
timezero_beat = df_beat[df_beat.window_beat_ECCPEMUY == 0]
listIB8A_ARzero_beat = timezero_beat['IB8A_AR']
j = sum(listIB8A_ARzero_beat)
k = len(listIB8A_ARzero_beat)
l = j/k #AAR_beat(0)
timeplus1_beat = df_beat[df_beat.window_beat_ECCPEMUY == 1]
listIB8A_ARplus1_beat = timeplus1_beat['IB8A_AR']
m = sum(listIB8A_ARplus1_beat)
n = len(listIB8A_ARplus1_beat)
o = m/n #AAR(1)
timeplus2_beat = df_beat[df_beat.window_beat_ECCPEMUY == 2]
listIB8A_ARplus2_beat = timeplus2_beat['IB8A_AR']
p = sum(listIB8A_ARplus2_beat)
r = len(listIB8A_ARplus2_beat)
s = p/r #AAR_beat(2)
timeplus3_beat = df_beat[df_beat.window_beat_ECCPEMUY == 3]
listIB8A_ARplus3_beat = timeplus3_beat['IB8A_AR']
t = sum(listIB8A_ARplus3_beat)
u = len(listIB8A_ARplus3_beat)
v = t/u #AAR(3)
CAARminus3_IB8A_beat = c
CAARminus2_IB8A_beat = c + f
CAARminus1_IB8A_beat = c + f + i
CAARzero_IB8A_beat = c + f + i + l
CAARplus1_IB8A_beat = c + f + i + l + o
CAARplus2_IB8A_beat = c + f + i + l + o + s
CAARplus3_IB8A_beat = c + f + i + l + o + s + v
CAAR_IB8A_beat = [CAARminus3_IB8A_beat, CAARminus2_IB8A_beat, CAARminus1_IB8A_beat, CAARzero_IB8A_beat, CAARplus1_IB8A_beat, CAARplus2_IB8A_beat, CAARplus3_IB8A_beat]
time = [-3, -2, -1, 0, 1, 2, 3]

import matplotlib.pyplot as plt

fig1 = plt.figure(); ax1=fig1.add_subplot(1,1,1)
ax1.plot(time,CAAR_IB8A_beat,'k--',color='blue',label=r'$CAAR$')
ax1.legend(loc='best')
ax1.set_xlabel(r'Time Horizon')
ax1.set_ylabel(r'CAAR IB8A ECCPEMUY beat')

#IB8A ECCPEMUY miss
timeminus3_miss = df_miss[df_miss.window_miss_ECCPEMUY == -3]
listIB8A_ARminus3_miss = timeminus3_miss['IB8A_AR']
aa = sum(listIB8A_ARminus3_miss)
bb = len(listIB8A_ARminus3_miss)
cc = aa/bb #AAR_miss(-3)
timeminus2_miss = df_miss[df_miss.window_miss_ECCPEMUY == -2]
listIB8A_ARminus2_miss = timeminus2_miss['IB8A_AR']
dd = sum(listIB8A_ARminus2_miss)
ee = len(listIB8A_ARminus2_miss)
ff = dd/ee #AAR_miss(-2)
timeminus1_miss = df_miss[df_miss.window_miss_ECCPEMUY == -1]
listIB8A_ARminus1_miss = timeminus1_miss['IB8A_AR']
gg = sum(listIB8A_ARminus1_miss)
hh = len(listIB8A_ARminus1_miss)
ii = gg/hh #AAR_miss(-1)
timezero_miss = df_miss[df_miss.window_miss_ECCPEMUY == 0]
listIB8A_ARzero_miss = timezero_miss['IB8A_AR']
jj = sum(listIB8A_ARzero_miss)
kk = len(listIB8A_ARzero_miss)
ll = jj/kk #AAR_miss(0)
timeplus1_miss = df_miss[df_miss.window_miss_ECCPEMUY == 1]
listIB8A_ARplus1_miss = timeplus1_miss['IB8A_AR']
mm = sum(listIB8A_ARplus1_miss)
nn = len(listIB8A_ARplus1_miss)
oo = mm/nn #AAR_miss(1)
timeplus2_miss = df_miss[df_miss.window_miss_ECCPEMUY == 2]
listIB8A_ARplus2_miss = timeplus2_miss['IB8A_AR']
pp = sum(listIB8A_ARplus2_miss)
rr = len(listIB8A_ARplus2_miss)
ss = pp/rr #AAR_miss(2)
timeplus3_miss = df_miss[df_miss.window_miss_ECCPEMUY == 3]
listIB8A_ARplus3_miss = timeplus3_miss['IB8A_AR']
tt = sum(listIB8A_ARplus3_miss)
uu = len(listIB8A_ARplus3_miss)
vv = tt/uu #AAR_miss(3)
CAARminus3_IB8A_miss = cc
CAARminus2_IB8A_miss = cc + ff
CAARminus1_IB8A_miss = cc + ff + ii
CAARzero_IB8A_miss = cc + ff + ii + ll
CAARplus1_IB8A_miss = cc + ff + ii + ll + oo
CAARplus2_IB8A_miss = cc + ff + ii + ll + oo + ss
CAARplus3_IB8A_miss = cc + ff + ii + ll + oo + ss + vv
CAAR_IB8A_miss = [CAARminus3_IB8A_miss, CAARminus2_IB8A_miss, CAARminus1_IB8A_miss, CAARzero_IB8A_miss, CAARplus1_IB8A_miss, CAARplus2_IB8A_miss, CAARplus3_IB8A_miss]

fig2 = plt.figure(); ax2=fig2.add_subplot(1,1,1)
ax2.plot(time,CAAR_IB8A_miss,'k--',color='blue',label=r'$CAAR$')
ax2.legend(loc='best')
ax2.set_xlabel(r'Time Horizon')
ax2.set_ylabel(r'CAAR IB8A ECCPEMUY miss')

#QW1A ECCPEMUY beat
listQW1A_ARminus3_beat = timeminus3_beat['QW1A_AR']
aaa = sum(listQW1A_ARminus3_beat)
bbb = len(listQW1A_ARminus3_beat)
ccc = aaa/bbb #AAR_beat(-3)
listQW1A_ARminus2_beat = timeminus2_beat['QW1A_AR']
ddd = sum(listQW1A_ARminus2_beat)
eee = len(listQW1A_ARminus2_beat)
fff = ddd/eee #AAR_beat(-2)
listQW1A_ARminus1_beat = timeminus1_beat['QW1A_AR']
ggg = sum(listQW1A_ARminus1_beat)
hhh = len(listQW1A_ARminus1_beat)
iii = ggg/hhh #AAR_beat(-1)
listQW1A_ARzero_beat = timezero_beat['QW1A_AR']
jjj = sum(listQW1A_ARzero_beat)
kkk = len(listQW1A_ARzero_beat)
lll = jjj/kkk #AAR_beat(0)
listQW1A_ARplus1_beat = timeplus1_beat['QW1A_AR']
mmm = sum(listQW1A_ARplus1_beat)
nnn = len(listQW1A_ARplus1_beat)
ooo = mmm/nnn #AAR(1)
listQW1A_ARplus2_beat = timeplus2_beat['QW1A_AR']
ppp = sum(listQW1A_ARplus2_beat)
rrr = len(listQW1A_ARplus2_beat)
sss = ppp/rrr #AAR_beat(2)
listQW1A_ARplus3_beat = timeplus3_beat['QW1A_AR']
ttt = sum(listQW1A_ARplus3_beat)
uuu = len(listQW1A_ARplus3_beat)
vvv = ttt/uuu #AAR(3)
CAARminus3_QW1A_beat = ccc
CAARminus2_QW1A_beat = ccc + fff
CAARminus1_QW1A_beat = ccc + fff + iii
CAARzero_QW1A_beat = ccc + fff + iii + lll
CAARplus1_QW1A_beat = ccc + fff + iii + lll + ooo
CAARplus2_QW1A_beat = ccc + fff + iii + lll + ooo + sss
CAARplus3_QW1A_beat = ccc + fff + iii + lll + ooo + sss + vvv
CAAR_QW1A_beat = [CAARminus3_QW1A_beat, CAARminus2_QW1A_beat, CAARminus1_QW1A_beat, CAARzero_QW1A_beat, CAARplus1_QW1A_beat, CAARplus2_QW1A_beat, CAARplus3_QW1A_beat]

fig3 = plt.figure(); ax3=fig3.add_subplot(1,1,1)
ax3.plot(time,CAAR_QW1A_beat,'k--',color='blue',label=r'$CAAR$')
ax3.legend(loc='best')
ax3.set_xlabel(r'Time Horizon')
ax3.set_ylabel(r'CAAR QW1A ECCPEMUY beat')

#QW1A CPEXEMUY miss
listQW1A_ARminus3_miss = timeminus3_miss['QW1A_AR']
aaaa = sum(listQW1A_ARminus3_miss)
bbbb = len(listQW1A_ARminus3_miss)
cccc = aaaa/bbbb #AAR_miss(-3)
listQW1A_ARminus2_miss = timeminus2_miss['QW1A_AR']
dddd = sum(listQW1A_ARminus2_miss)
eeee = len(listQW1A_ARminus2_miss)
ffff = dddd/eeee #AAR_miss(-2)
listQW1A_ARminus1_miss = timeminus1_miss['QW1A_AR']
gggg = sum(listQW1A_ARminus1_miss)
hhhh = len(listQW1A_ARminus1_miss)
iiii = gggg/hhhh #AAR_miss(-1)
listQW1A_ARzero_miss = timezero_miss['QW1A_AR']
jjjj = sum(listQW1A_ARzero_miss)
kkkk = len(listQW1A_ARzero_miss)
llll = jjjj/kkkk #AAR_miss(0)
listQW1A_ARplus1_miss = timeplus1_miss['QW1A_AR']
mmmm = sum(listQW1A_ARplus1_miss)
nnnn = len(listQW1A_ARplus1_miss)
oooo = mmmm/nnnn #AAR_miss(1)
listQW1A_ARplus2_miss = timeplus2_miss['QW1A_AR']
pppp = sum(listQW1A_ARplus2_miss)
rrrr = len(listQW1A_ARplus2_miss)
ssss = pppp/rrrr #AAR_miss(2)
listQW1A_ARplus3_miss = timeplus3_miss['QW1A_AR']
tttt = sum(listQW1A_ARplus3_miss)
uuuu = len(listQW1A_ARplus3_miss)
vvvv = tttt/uuuu #AAR_miss(3)
CAARminus3_QW1A_miss = cccc
CAARminus2_QW1A_miss = cccc + ffff
CAARminus1_QW1A_miss = cccc + ffff + iiii
CAARzero_QW1A_miss = cccc + ffff + iiii + llll
CAARplus1_QW1A_miss = cccc + ffff + iiii + llll + oooo
CAARplus2_QW1A_miss = cccc + ffff + iiii + llll + oooo + ssss
CAARplus3_QW1A_miss = cccc + ffff + iiii + llll + oooo + ssss + vvvv
CAAR_QW1A_miss = [CAARminus3_QW1A_miss, CAARminus2_QW1A_miss, CAARminus1_QW1A_miss, CAARzero_QW1A_miss, CAARplus1_QW1A_miss, CAARplus2_QW1A_miss, CAARplus3_QW1A_miss]

fig4 = plt.figure(); ax4=fig4.add_subplot(1,1,1)
ax4.plot(time,CAAR_QW1A_miss,'k--',color='blue',label=r'$CAAR$')
ax4.legend(loc='best')
ax4.set_xlabel(r'Time Horizon')
ax4.set_ylabel(r'CAAR QW1A ECCPEMUY miss')