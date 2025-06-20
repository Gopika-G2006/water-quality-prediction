from sklearn. model = LinearRegression() #building a linear model
from sklearn. metrics import confusion_matrix, classification_report
from scipy import stats
import pandas as pd
import matplotlib. pyplot as plt
import seaborn as sns
# Manually uploaded your CSV file to this when this runs.
For Colab users, you can use the following cell to upload files:
from google. colab import files
uploaded = files.upload()
df = pd. read_csv("water_quality. csv") # Make sure this file is uploaded in your Colab or local directory.
print('Shape of the Dataset:', df. shape)
print("Null data:\n", df. isnull(). sum())
Drop missing values
df.dropna(inplace=True)
#Confirm missing values are handled
print("After dropping missing values:\n",df.isnull().sum())
