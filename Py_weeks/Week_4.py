import numpy as np
# read data from csv file into 2d numpy array
#1 to 3:
filename = '../data/befkbhalderstatkode.csv'

bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

dataMask = (bef_stats_df[:,0] == 2015)

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
          10: 'Amager Vest', 99: 'Udenfor'}

def number_of_people_per_neighbourhood(n, mask):
    all_people_in_given_n = bef_stats_df[mask & (bef_stats_df[:,1] == n)]
    sum_of_people = all_people_in_given_n[:,4].sum() # index 4 is no of 'PERSONER'
    return sum_of_people

dataInfo = np.array([number_of_people_per_neighbourhood(n, dataMask) for n in neighb.keys()])

count = 1
for people in dataInfo:
    print(neighb.get(count), "has:", people, "people")
    count += 1

print(dataInfo)
dataInfo[::-1].sort()
print(dataInfo)
# 4. Make a bar plot to show the size of each city area from the smallest to the largest
#%matplotlib notebook
#import matplotlib.pyplot as plt
#np.where(dataInfo)
#plt.bar(dataInfo, dataInfo, width=0.5, align='center')
#plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')
