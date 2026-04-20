import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')

print(penguins.head())
print(penguins.describe())
print(penguins['species'].value_counts())

sns.set_style("whitegrid")

sns.scatterplot(data=penguins,
                x='bill_length_mm',
                y ='bill_depth_mm',)
plt.title('My first seaborn plot!')
plt.show()
