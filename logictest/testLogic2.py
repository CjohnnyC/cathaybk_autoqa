default_height=100
rebound_times=10

def rebound_height(default_height, rebound_times):
    return default_height*(0.5**rebound_times)

sum=0
for i in range(1, rebound_times+1):
    sum+=rebound_height(default_height, i)

tenth_rebound=rebound_height(default_height, rebound_times)
all_traverse=sum*3-tenth_rebound
#all_rebound=sum

print("所有落下和反彈高度總和為 "+str(all_traverse)+" 公分")
print("第十次反彈高度為 "+str(tenth_rebound)+" 公分")
#print("只計算共反彈十次的高度為 "+str(all_rebound)+" 公分")