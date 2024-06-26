# -*- coding: utf-8 -*-
"""ML TASK 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wuxvtOWSsAI4yvWcip1asFZKUO9QdfBF

IMPORTING NECESSARY LIBRARIES
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay

"""LOAD AND READ THE DATA"""

df = pd.read_csv("/content/spam.csv",encoding = "latin1")
df.head()

"""DELECTING UNNECESSARY COLLUMNS AND RENAME "V1" AND "V2"
"""

columns_to_drop =["Unnamed: 2","Unnamed: 3","Unnamed: 4"]
df.drop(columns_to_drop,inplace=True,axis = 1)
df.columns = ["Category","Message"]

df.columns

"""CHECKING IF THERE IS ANY MISSING VALUES"""

df.isna().sum()

"""CHECKING IF THERE IS ANY DUPLICATE SAMPLES IN THE DATA SET"""

df.duplicated().sum()

#Drop the duplicate samples
df = df.drop_duplicates(keep ="first")
df.duplicated().sum()

"""VISUAL DISTRIBUTION OF EMAIL CATEGORIES"""

number_of_spam = df[df["Category"] == "spam"].shape[0]
number_of_ham = df[df["Category"] == "ham"].shape[0]
plt.figure(figsize=(7,6))
mail_categories = [number_of_ham, number_of_spam]
labels = [f"Ham = {number_of_ham}", f"Spam = {number_of_spam}"]
explode = [.2, 0]

plt.pie(mail_categories, labels=labels, explode=explode, autopct="%.2f %%")
plt.title("Ham vs Spam")

plt.show()

"""MAKE COLUMN FOR SPAM AND REPLACE SPAMS WITH 1 AND HAMS WITH 0"""

encoder = LabelEncoder()
df['spam'] = encoder.fit_transform(df['Category'])
df.head()

df.drop('Category', inplace =True, axis =1)

"""TRAIN AND TEST"""

x = df['Message']
y = df['spam']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2 , random_state = 42)

"""CREATING A BAG OF WORDS REPRESSENTATION USING COUNTER VECTORIZER FOR THE TRAINING DATA X_TRAIN"""

vectorizer = CountVectorizer()
x_train_counts = vectorizer.fit_transform(x_train)

"""TRAIN NAIVE BAYES MODEL"""

classifier = MultinomialNB()
classifier.fit(x_train_counts, y_train)

x_test_counts = vectorizer.transform(x_test)

y_pred = classifier.predict(x_test_counts)

"""DISPLAY CONFUSION MATRIX"""

confusion_matrix = confusion_matrix(y_test, y_pred)
cm_display = ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = ["Ham", "Spam"])
cm_display.plot()
plt.show()

print(classification_report(y_test, y_pred))

df.head()

