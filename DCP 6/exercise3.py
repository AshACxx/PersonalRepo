import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
sns.set_style("whitegrid")

plt.figure(figsize = (12,5))
sns.countplot(data=tips, x='day', hue = 'day',
              palette='viridis', legend=False)
plt.title('Number of Meals by Day')
plt.xlabel('Day of Week')
plt.ylabel('Number of Meals')

plt.show()
#2


              
            