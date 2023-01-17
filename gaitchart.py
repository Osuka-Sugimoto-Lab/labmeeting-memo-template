from cmath import phase
import numpy as np
import matplotlib.pyplot as plt

degree = 40 #指定回転角
pich = 0.6 #ピッチ[s]
phase_df = 0.1 #位相差[s]

set_time = 2*degree*0.1/60 #接地時間[s]

rf = [0] #右前脚
lf = [set_time] #左前脚
rh = [0] #右後脚
lh = [0] #左後脚

num_list = 50


for n_rf in range(num_list):#右前足の接地時間配列
    if n_rf % 2 == 0:
        rf.append(rf[n_rf] + set_time + pich)
    else:
        rf.append(rf[n_rf] + set_time)
    #print(rf[n_rf])

for n_lf in range(num_list):#左前足の接地時間配列
    if n_lf % 2 == 0:
        lf.append(lf[n_lf] + set_time + pich)
    else:
        lf.append(lf[n_lf] + set_time)
    #print(lf[n_lf])

for n_rh in range(num_list):#左前足の接地時間配列
    if n_rh == 0:
        rh.append(rh[n_rh] + phase_df)
    elif n_rh % 2 == 0:
        rh.append(rh[n_rh] + phase_df + pich + set_time)
    else:
        rh.append(rh[n_rh] + set_time)
    #print(rh[n_rh])

for n_lh in range(num_list):#左前足の接地時間配列
    if n_lh == 0:
        lh.append(lh[n_lh] + phase_df + set_time)
    elif n_lh % 2 == 0:
        lh.append(lh[n_lh] + phase_df + pich + set_time)
    else:
        lh.append(lh[n_lh] + set_time)
    #print(lh[n_lh])



# FigureとAxesを作成
fig = plt.figure(figsize = (6, 6))
ax = fig.add_subplot(111)

ax.set_xlabel("time[s]")

# 軸範囲を設定
ax.set_xlim(0, 5)
ax.set_ylim(0, 8)
ax.axes.yaxis.set_visible(False)


for plot_rf in range(len(rf)):
    if plot_rf % 2 == 0 and plot_rf != num_list:
        ax.axvspan(rf[plot_rf],rf[plot_rf + 1] ,0.75,1 ,color = "black")
        #print(rf[plot_rf],rf[plot_rf + 1])

for plot_lf in range(len(lf)):
    if plot_lf % 2 == 0 and plot_lf != num_list:
        ax.axvspan(lf[plot_lf],lf[plot_lf + 1] ,0.25,0.5 ,color = "black")
        #print(lf[plot_lf],lf[plot_lf + 1])

for plot_rh in range(len(rh)):
    if plot_rh % 2 == 0 and plot_rh != num_list:
        ax.axvspan(rh[plot_rh],rh[plot_rh + 1] ,0.5,0.75 ,color = "black")
        #print(rh[plot_rh],rh[plot_rh + 1])

for plot_lh in range(len(lh)):
    if plot_lh % 2 == 0 and plot_lh != num_list:
        ax.axvspan(lh[plot_lh],lh[plot_lh + 1] ,0.,0.25 ,color = "black")
        #print(lh[plot_lh],lh[plot_lh + 1])

ax.text(-0.04, 0.875, "RF", va='center', transform=ax.transAxes, rotation=90)
ax.text(-0.04, 0.625, "RH", va='center', transform=ax.transAxes, rotation=90)
ax.text(-0.04, 0.375, "LF", va='center', transform=ax.transAxes, rotation=90)
ax.text(-0.04, 0.125, "LH", va='center', transform=ax.transAxes, rotation=90)

#ax.axvspan(0, 2.05,0.25,0.5 ,color = "black")
#ax.axvspan(0, 3.05,0.5,0.75 ,color = "black")
#ax.axvspan(0, 4.05,0.75,1 ,color = "black")

plt.show()