import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_style("whitegrid")

styles = ["darkgrid", "whitegrid"]
data = np.random.randn(1000)

fig, axes = plt.subplots(1,5, figsize=(20, 4))

for ax, style in zip(axes, styles):
    with sns.axes_style(style):
        sns.histplot(data, ax=ax, color="blue")
        ax.set_title(f"Style: {style}")