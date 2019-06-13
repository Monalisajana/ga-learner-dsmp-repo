# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Code starts here
data = pd.read_csv(path)
#plt.hist('Rating' , bins = 10)
data = data[data['Rating']<= 5]
plt.hist('Rating' , bins = 10)

#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
print(total_null)
print(data.isnull().count())
percent_null = total_null/data.isnull().count()
missing_data = pd.concat([total_null,percent_null],axis=1,keys=['Total','Percent'])
print(missing_data)
data = data.dropna(subset=['Current Ver'])
data = data.dropna(subset=['Android Ver'])
total_null_1 = data.isnull().sum()
percent_null_1 = total_null_1 / data.isnull().count()
missing_data_1 = pd.concat([total_null_1,percent_null_1],axis=1,keys=['Total','Percent'])
print(missing_data_1)

# code ends here


# --------------

#Code starts here
sns.catplot(x="Category",y="Rating",data=data, kind="box",height = 10)
plt.xticks(rotation=90)
plt.title('Rating vs Category [BoxPlot]')
plt.show()


#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data.Installs.value_counts())

data['Installs'] = data['Installs'].map(lambda x: x.replace(',', ''))
data['Installs'] = data['Installs'].map(lambda x: x.replace('+', ''))
data['Installs'] = pd.to_numeric(data['Installs']).astype(int)
print(data['Installs'])

le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])
print(data['Installs'])
sns.regplot(x="Installs", y="Rating", data=data)
plt.title("Rating vs Installs [RegPlot]")


#Code ends here



# --------------
#Code starts here
print(data['Price'].value_counts())
data['Price'] = data['Price'].str.replace('$','')
data['Price'] = data['Price'].astype(float)
sns.regplot(x="Price",y="Rating",data=data)
plt.title('Rating vs Price [RegPlot]')


#Code ends her


# --------------

#Code starts here

#print(data['Genres'].unique())
tempG = data['Genres'].str.split(';').apply(pd.Series)
data['Genres']=tempG.iloc[:,0]
gr_mean = data.groupby('Genres',as_index=False)['Rating'].mean()
print(gr_mean.describe())
gr_mean=gr_mean.sort_values(by='Rating')
print(gr_mean)
print(gr_mean.iloc[0,:],gr_mean.iloc[-1,:])



#Code ends here


# --------------

#Code starts here
print(data['Last Updated'])
data['Last Updated']=pd.to_datetime(data['Last Updated'])
print(data['Last Updated'])
max_date = data['Last Updated'].max()

Diff_dates = max_date - data['Last Updated']
data['Last Updated Days'] = Diff_dates.dt.days
sns.regplot(x="Last Updated Days", y="Rating", data=data)
plt.title('Rating vs Last Updated [RegPlot]')
#Code ends here


