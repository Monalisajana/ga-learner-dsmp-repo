# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#print (data)
data['Gender'].replace('-','Agender',inplace=True)
#print(data)
gender_count = data['Gender'].value_counts()
print(gender_count)
plt.hist(gender_count)
plt.show()
#Code starts here 




# --------------
#Code starts here
alignment = data.Alignment.value_counts()
print(alignment)
colors = ['b', 'g', 'r']
labels = ['good', 'bad', 'neutral']
explode = (0, 0, 0)
plt.pie(alignment, colors=colors, labels=labels,explode=explode, autopct='%1.1f%%',
counterclock=False, shadow=True)
plt.title('Character Alignment')
plt.legend(labels,loc=3)
plt.show()


# --------------
#Code starts here
# correlation between strenght and combat
sc_df = data[['Strength','Combat']].copy()
sc_covariance = sc_df.cov().iloc[0,1]
print(sc_covariance)
sc_strength = data.Strength.std()
sc_combat = data.Combat.std()
sc_pearson = sc_covariance / (sc_strength * sc_combat)
print (sc_pearson)

# correlation between Interlligence & Combat

ic_df = data[['Intelligence','Combat']].copy()
ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence = data.Intelligence.std()
ic_combat = data.Combat.std()
ic_pearson = ic_covariance / (ic_intelligence * ic_combat)
print (ic_pearson)



# --------------
#Code starts here
# calculation of quantile for total column
total_high = data.Total.quantile(0.99)
#print(total_high)
super_best = data[data.Total > total_high]
print(super_best.Total)
super_best_names = []
for i in super_best.Name:
  super_best_names.append(i)
print(super_best_names)  


# --------------
#Code starts here

fig, ax_1 = plt.subplots(figsize=(10, 6))
ax_1.boxplot(data.Intelligence)
plt.xlabel('ax_1')
ax_1.set_title('Intelligence')
fig, ax_2 = plt.subplots(figsize=(10,6))
ax_2.boxplot(data.Speed)
ax_2.set_title('Speed')
fig, ax_3 = plt.subplots(figsize=(10,6))
ax_3.boxplot(data.Power)
ax_3.set_title('Power')
plt.show()


