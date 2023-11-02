# -*- coding: UTF-8 -*-
import numpy as np
from matplotlib import pyplot as plt

plt.figure(figsize=(5.5, 3))
n = 12
X = np.arange(n)

Y = [1.001164512,0.468909554,0.597346401,1.535209344,2.669928096,0.817526594,2.6325783,3.97537975,2.734271341,0.966686682,0.249248846,0.043017806]

Y2 = [0.04480073,1.416282341,0.267547086,0.030212455,2.916243963,1.189752059,0.922893815,0.205446547,1.937517616,3.07659355,2.406150742,1.207956988]

Y3 = [0.952997812,0.683430464,0.326065913,2.696801796,1.668358553,1.748588353,1.51596328,0.287675147,0.305855036,2.595155947,4.808433786,1.511461095]

Y4 = [1.050016005,0.018685137,1.274683248,0.140718198,2.282393007,0.976908201,3.295572835,3.395952899,2.253470716,3.553046698,3.471936687,1.819184737]


#Y2 = np.random.uniform(0.5, 1.0, n)
plt.bar(X - 0.3, Y, width=0.2, facecolor='#130074',edgecolor='black',label='BiMode',lw=.5)
plt.bar(12-0.3, 1.474272269, width=0.2, facecolor='#130074',edgecolor='black',lw=.5)

plt.bar(X - 0.1, Y2, width=0.2, facecolor='#CB181B', edgecolor='black',label='Tournament',lw=.5)
plt.bar(12- 0.1, 1.301783158, width=0.2, facecolor='#CB181B',edgecolor='black',lw=.5)

plt.bar(X + 0.1, Y3, width=0.2, facecolor='white', edgecolor='black',label='TAGE',lw=.5)
plt.bar(12+0.1, 1.591732265, width=0.2, facecolor='white',edgecolor='black',lw=.5)

plt.bar(X + 0.3, Y4, width=0.2, facecolor='#008B45', edgecolor='black',label='TAGE_SC_L',lw=.5)
plt.bar(12+0.3, 1.961047364, width=0.2, facecolor='#008B45',edgecolor='black',lw=.5)

plt.legend(
    loc = "upper left",
    ncol = 1,
    prop={'family':'Times New Roman', 'size':7}
)

plt.grid(ls=":",c='grey',axis='y')

bench= ['gcc+cal','mil+pov','bzi+sop','nam+les','hmm+lbm','gob+h26','gro+lbm','mcf+sje','sop+hmm','sje+gcc','mcf+pre','cal+nam','average']

my_x_ticks = np.arange(0, 13, 1)#原始数据有13个点，故此处为设置从0开始，间隔为1
#plt.xticks(my_x_ticks)
plt.xticks(my_x_ticks,bench,rotation=60,size=10,fontproperties='Times New Roman')
#plt.tick_params(direction='out')
#plt.xticks(fontproperties='Times New Roman',size=6)
pent = ['0.0%','1.0%','2.0%','3.0%','4.0%','5.0']
my_y_ticks = [0,1,2,3,4,5]
plt.yticks(my_y_ticks,pent,size=10,fontproperties='Times New Roman')
plt.ylim(0, 5.1)
plt.xlim(-0.8, +12.8)
plt.ylabel("Performance Overhead",fontdict={'family':'Times New Roman', 'size':10}, labelpad=1)   #'family':'Times New Roman'

plt.savefig('C:\\Users\\rain\\Desktop\\ASPDAC2022\\PHT.pdf', dpi=300, bbox_inches='tight', pad_inches=0.01)
plt.show()