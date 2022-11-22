default_height=100
rebound_times=10
rebound_ratio=0.5

def rebound_height(default_height, rebound_times):
    return default_height*(rebound_ratio**rebound_times)

all_rebound=0
for i in range(1, rebound_times+1):
    all_rebound+=rebound_height(default_height, i)

tenth_rebound=rebound_height(default_height, rebound_times)
all_traverse=all_rebound*(1+1/rebound_ratio)-tenth_rebound

print("All traverse height(except 10th rebound) is "+str(all_traverse)+" cm")
print("The 10th rebound height is "+str(tenth_rebound)+" cm")
#print("Sum of 10 times rebound height is "+str(all_rebound)+" cm")
