# -----Weather Anomly Detector-----
import numpy as np
days=50

# Generate random data
temprature=np.random.randint(25,40,days)
humidity=np.random.randint(50,90,days)
rainfall=np.random.randint(0,20,days)

# Combining into a dataset
data=np.column_stack((temprature,humidity,rainfall))

# Choose random days to modify
anomly_indices=np.random.choice(days,3,replace=False)
for idx in anomly_indices:
    data[idx]=[50,95,50] # Extreme values
print("Data\n",data)

# Mean & STD
mean=np.mean(data,axis=0)
std=np.std(data,axis=0)

# Z Scores
z_scores=(data-mean)/std 

# Absolute values
abs_z=np.abs(z_scores)
day_scores=np.sum(abs_z,axis=1)
threshold=5

# Detect anomalous days
features=["Temprature","Humidity","Rainfall"]
print("Detected Anomlies\n")
for i in range(days):
    if day_scores[i] > threshold:
        print(f"Day {i+1} is anomalous (Score: {day_scores[i]:.2f})")
        for j in range(data.shape[1]):
            if abs_z[i][j] > 2:
                print(f" {features[j]}: {data[i][j]}")
        print()
# Total anomalies
total_anomalies=np.sum(day_scores>threshold)

# Summary
print("Summary\n")
print("Total days:",days)
print("Total Anomalies:",total_anomalies)
print("Percentage:",(total_anomalies/days)*100)

# Top 3 Anomalies
top_indices=np.argsort(day_scores)[-3:]
print("Top 3 anomalous days :\n")
for idx in top_indices[::-1]:
    print(f"Day {idx+1} , Score:{day_scores[idx]:.2f}")
