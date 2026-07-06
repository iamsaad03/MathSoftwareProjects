import pandas as pd
import matplotlib.pyplot as plt

# --- Part A: Reading the Excel file and plotting charts ---

# Excel File Name
file_name = 'data.xlsx' 

# Read all the data
df = pd.read_excel(file_name)

# Extract the first column name (likely Data size) for the X-axis
x_col = df.columns[0]
# Extract algorithm column names for plotting and calculations
alg_cols = df.columns[1:]

print("Data read from the Excel file:")
print(df)
print("-" * 50)

# 1. Draw Line Plot
df.plot(x=x_col, y=alg_cols, kind='line', marker='o', figsize=(8, 5))
plt.title('Line Chart: Algorithm Execution Times')
plt.ylabel('Execution Time')
plt.xlabel(x_col)
plt.grid(True)
plt.savefig("lin_chart.png", dpi=300)
plt.show()

# 2. Draw Bar Plot
df.plot(x=x_col, y=alg_cols, kind='bar', figsize=(8, 5))
plt.title('Bar Chart: Algorithm Execution Times')
plt.ylabel('Execution Time')
plt.xlabel(x_col)
# Keep X-axis labels horizontal
plt.xticks(rotation=0) 
plt.grid(axis='y')
plt.savefig("Bar_chart.png", dpi=300)
plt.show()

# 3. Draw Box Plot
# Provide only numerical columns (algorithms) for the box plot
df[alg_cols].plot(kind='box', figsize=(8, 5))
plt.title('Box Plot: Algorithm Execution Times')
plt.ylabel('Execution Time')
plt.grid(axis='y')
plt.savefig("Box_chart.png", dpi=300)
plt.show()


# --- Part C: Calculate the average execution time of Algorithm 2 ---

# To ensure the average is calculated only for 100 to 600 KB data,
# we filter out any rows containing "700".
# This ensures that even after adding new data in Part B, 
# the average for Part C remains constant and correct for 100-600 KB.

# Convert the first column values to string to ensure safe searching
df_filtered = df[~df[x_col].astype(str).str.contains('700')]

# Check if 'Alg.2' column exists
if 'Alg.2' in df_filtered.columns:
    avg_alg2 = df_filtered['Alg.2'].mean()
    print("--- Output for Part C ---")
    print(f"Average execution time of Algorithm 2 (for 100-600 KB data): {avg_alg2}")
else:
    print("Column named 'Alg.2' not found in the Excel file. Please check the column names.")

input()