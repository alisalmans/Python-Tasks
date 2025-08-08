# import pandas as pd
# import numpy as np

# data=pd.DataFrame({
#     "age":[12,45,67,97,23,67],
#     "bp":[34.65,46.65,65.43,55,34,76.8]
# })

# print("mean")
# print(data.mean())

# print("standard deviation")
# print(data.std())
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Domain 1: Computing ---
computing_data = pd.DataFrame({
    "CPU_Usage": [30, 45, 70, 55, 60, 80, 40],
    "Memory_Usage": [4.2, 3.8, 6.0, 5.5, 6.1, 7.2, 4.9]
})

# --- Domain 2: Medical ---
medical_data = pd.DataFrame({
    "Age": [20, 22, 30, 35, 40, 28],
    "Heart_Rate": [72, 78, 90, 88, 76, 85]
})

# --- Domain 3: Social Science ---
social_data = pd.DataFrame({
    "Education_Years": [5, 10, 12, 16, 14, 8, 7],
    "Income_Thousands": [10, 20, 25, 35, 30, 15, 12]
})
def basic_stats(df):
    print("Mean:\n", df.mean())
    print("\nMedian:\n", df.median())
    print("\nStandard Deviation:\n", df.std())
print("Computing Domain:")
basic_stats(computing_data)

print("\nMedical Domain:")
basic_stats(medical_data)

print("\nSocial Science Domain:")
basic_stats(social_data)
# Computing Graph
computing_data.plot(kind="line", title="Computing Stats")
plt.xlabel("Record")
plt.ylabel("Usage")
plt.grid(True)
plt.show()

# Medical Graph
medical_data.plot(kind="bar", title="Medical Stats", colormap='viridis')
plt.show()

# Social Graph
social_data.plot(kind="scatter", x="Education_Years", y="Income_Thousands", title="Income vs Education")
plt.show()




# print("hello")