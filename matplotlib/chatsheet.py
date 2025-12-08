import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------
# MATPLOTLIB EXAMPLES
# -----------------------------------------

# Line Plot
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

# Scatter Plot
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

# Bar Plot
labels = ["A", "B", "C"]
values = [30, 50, 40]
plt.bar(labels, values)
plt.title("Bar Chart")
plt.show()

# Horizontal Bar Plot
plt.barh(labels, values)
plt.title("Horizontal Bar Chart")
plt.show()

# Histogram
data = [1,2,2,3,3,3,4,4,5,6]
plt.hist(data, bins=5)
plt.title("Histogram")
plt.show()

# Pie Chart
sizes = [40, 30, 20, 10]
labels = ["A", "B", "C", "D"]
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()

# Multiple Lines
plt.plot([1,2,3], [2,4,6], label="Line 1")
plt.plot([1,2,3], [1,3,2], label="Line 2")
plt.legend()
plt.show()

# Figure Size
plt.figure(figsize=(6,4))
plt.plot(x, y)
plt.title("Figure Size Example")
plt.show()

# Subplots
fig, ax = plt.subplots(1, 2, figsize=(10,4))
ax[0].plot(x, y)
ax[0].set_title("Plot 1")
ax[1].bar(labels, values)
ax[1].set_title("Plot 2")
plt.show()

# Save Plot
plt.plot(x, y)
plt.title("Saved Plot")
plt.savefig("plot.png")
plt.close()

# -----------------------------------------
# SEABORN EXAMPLES
# -----------------------------------------

df = sns.load_dataset("tips")

# Line Plot
sns.lineplot(x="total_bill", y="tip", data=df)
plt.show()

# Scatter Plot
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df)
plt.show()

# Bar Plot
sns.barplot(x="day", y="total_bill", data=df)
plt.show()

# Count Plot
sns.countplot(x="day", data=df)
plt.show()

# Box Plot
sns.boxplot(x="day", y="total_bill", data=df)
plt.show()

# Violin Plot
sns.violinplot(x="day", y="tip", data=df)
plt.show()

# Histogram / Distribution Plot
sns.histplot(df["total_bill"], kde=True)
plt.show()

# Heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()

# Pair Plot
sns.pairplot(df)
plt.show()

# Style Theme
sns.set_style("darkgrid")
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.show()

# Joint Plot
sns.jointplot(x="total_bill", y="tip", data=df, kind="scatter")

# Swarm Plot
sns.swarmplot(x="day", y="tip", data=df)
plt.show()