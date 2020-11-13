import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
group_size=[10,10,10,10,10,50]
labels=['AAAA','BBBB','CCCC','DDDD','EEEE','']
fig, ax = plt.subplots()
ax.axis('equal')
pie = ax.pie(group_size, radius=2.2, colors=['k'] ,startangle=180,counterclock=False)
pie2 = ax.pie([10,10,10,10,10,50], radius=2,  labeldistance=0.9, labels=labels,
              rotatelabels =True, startangle=180,counterclock=False)

plt.setp(pie2[1], rotation_mode="anchor", ha="center", va="center")
for tx in pie2[1]:
    rot = tx.get_rotation()
    tx.set_rotation(rot+90+(1-rot//180)*180)

plt.show()