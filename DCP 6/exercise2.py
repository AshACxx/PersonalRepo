import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
# Method 1: Multiple histograms (overlapping)
sns.histplot(data=tips, x='total_bill', hue='time',
kde=True, ax=axes[0], alpha=0.6)
axes[0].set_title('Distribution by Time (Overlapping)')
# Method 2: Normalized (density)

sns.histplot(data=tips, x='total_bill', hue='time',
kde=True, ax=axes[1],
element='step', stat='density',
common_norm=False)
axes[1].set_title('Distribution by Time (Normalized)')
plt.tight_layout()
plt.show()