# coding: utf-8
# @Author: boyac
# @Date:   2018-06-09 20:00:27
# @Last Modified by:   boyac
# @Last Modified time: 2018-06-11 23:07:27


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Data Feeding
maindf = pd.read_csv("NEISS2014.csv")
bodydf = pd.read_csv("BodyParts.csv")
diagdf = pd.read_csv("DiagnosisCodes.csv")
dispdf = pd.read_csv("Disposition.csv")



# Question 1
"""
1_1. What are the top three body parts most frequently represented in this dataset?
1_2. What are the top three body parts that are least frequently represented?

Answer:
1_1. Head, Face, Finger
1_2. 25-50% of body, Pubic region, Internal
"""

# Join BodyParts data to our main data
tbl01 = pd.merge(maindf, bodydf, how="left", left_on="body_part", right_on="Code")

# Data clean and drop unwanted records
tbl01 = tbl01[(tbl01["BodyPart"]!="Not Recorded")]
tbl01 = tbl01.groupby("BodyPart")["BodyPart"].agg(["count"])
top3 = tbl01.sort_values(["count"], ascending=False).head(3)
bottom3 = tbl01.sort_values(["count"], ascending=False).tail(3)



# Question 2
"""
2_1. How many injuries in this dataset involve a skateboard?
2_2. Of those injuries, what percentage were male and what percentage were female?
2_3. What was the average age of someone injured in an incident involving a skateboard?

Answer:
2_1. 495 of injuries involve a skateboard.
2_2. 0.82% of those injuries were male.
2_3. 0.18% of those injuries were female.
2_4. 17.89 was the average age of someone injured in an incident involving a skateboard

"""

skateboard = 1333
tbl02 = maindf[(maindf['prod1'] == skateboard)|(maindf['prod2'] == skateboard)]
tbl02_m = tbl02["sex"] == "Male"
tbl02_f = tbl02["sex"] == "Female"
tbl02_m = tbl02[tbl02_m]
tbl02_f = tbl02[tbl02_f]

m1333 = round(len(tbl02_m))/len(tbl02)
f1333 = round(len(tbl02_f))/len(tbl02)

print "{} of injuries involve a skateboard.".format(len(tbl02))
print "{0:.2f}% of those injuries were male.".format(m1333)
print "{0:.2f}% of those injuries were female.".format(f1333)
print "{0:.2f} was the average age of someone injured in an incident involving a skateboard.".format(tbl02['age'].mean())



# Question 3
"""
3_1. What diagnosis had the highest hospitalization rate? 
3_2. What diagnosis most often concluded with the individual leaving without being seen?
3_3. Briefly discuss your findings and any caveats you'd mention when discussing this data.

Answer:
3_1.
3_2.
3_3.
"""

# Join Diagnosis data to our main data
tbl03 = pd.merge(maindf, diagdf, how="left", left_on="diag", right_on="Code")

# Code: 4 = hospitalization
# Filter data with disposition = 4 for hispitalization and count its frequencies
tbl04 = tbl03[(tbl03["disposition"] == 4)]
tbl04= tbl04.groupby("Diagnosis")["Diagnosis"].agg(["count"])
topdiag04 = tbl04.sort_values(["count"], ascending=False).head(3)
topdiag04


# Code:6 = left without being seen
# Filter data with disposition = 6 for left without being seen and count its frequencies
tbl06 = tbl03[(tbl03["disposition"]==6)]
tbl06= tbl06.groupby("Diagnosis")["Diagnosis"].agg(["count"])
topdiag06 = tbl06.sort_values(["count"], ascending=False).head(3)
topdiag06


# Question 4
"""
4_1. Visualize any existing relationship between age and reported injuries
"""

# Extract age and reported injuries from tbl03
tbl07 = tbl03[['age','Diagnosis']]

# Creating a new age group, if coded as 0 = age 1, coded >= 200 age 1, others remains the same
tbl07.loc[tbl07['age'] == 0, 'age_group'] = 1
tbl07.loc[tbl07['age'] >= 200, 'age_group'] = 1
tbl07.loc[tbl07['age'] < 200, 'age_group'] = tbl07['age']
tbl07

# ranges = [2, 12, 18, 65, 150]
# age_groups = ['Infant', 'Children', 'Adolescents', 'Adults', 'Older Adults']

tbl08 = tbl07[['Diagnosis', 'age_group']]

tbl08.plot.bar()
