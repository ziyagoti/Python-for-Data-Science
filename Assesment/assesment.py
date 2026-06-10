# Python For Data Science Assessment
# Name:- Ziya Goti

# ==========================================================
# SECTION A: CONCEPT APPLICATION
# ==========================================================

# 1. You open the Heart Disease dataset in Jupyter Notebook.
# What is the difference between a .py file and a .ipynb file?

# Answer:

# Both .py and .ipynb files are used for writing Python code,
# but they are used in different ways.

# Difference Between .py File and .ipynb File

# .py File
# - Python script file
# - Contains only Python code
# - Runs as a complete program
# - Used for software development

# .ipynb File
# - Jupyter Notebook file
# - Contains code, output, graphs and text
# - Runs cell by cell
# - Used for data analysis and machine learning

# Points:
# - A .py file is mainly used to write and execute Python programs.
# - A .ipynb file allows us to write code, view output and add explanations in the same file.
# - Jupyter Notebook is very useful for data analysis and machine learning projects.

# Example:

print("Hello World")

# Saved as: program.py

# In Jupyter Notebook (.ipynb), along with the code,
# it can also show outputs, charts and explanations in separate cells.


# ==========================================================
# 2. The dataset has columns like age, cholesterol, and sex.
# What is the difference between a numerical feature and a categorical feature?
# ==========================================================

# Answer:

# Features are the columns of a dataset that are used for analysis and prediction.

# Numerical Feature:
# A numerical feature contains measurable values and mathematical
# operations can be performed on it.

# Examples:
# - Age
# - Cholesterol
# - Blood Pressure

# Categorical Feature:
# A categorical feature contains categories or labels that represent different groups.

# Examples:
# - Sex
# - Chest Pain Type
# - Rest ECG

# Difference Between Numerical Feature and Categorical Feature

# Numerical Feature:
# - Contains numbers
# - Used in calculations

# Categorical Feature:
# - Contains categories
# - Used for grouping

# Example:

age = [45, 60]
cholesterol = [220, 280]

# These values are numerical because they can be measured and calculated.

sex = ["Male", "Female"]

# These values represent categories.

# Points:
# - Numerical features are used in calculations.
# - Categorical features are used for classification and grouping.
# - Understanding the feature type helps in data analysis.


# ==========================================================
# 3. You run type() on the target column and it returns int.
# Why does the data type of your target variable matter before framing a prediction problem?
# ==========================================================

# Answer:

# The data type of the target variable helps us understand
# what type of prediction problem we are solving.

# In the Heart Disease dataset:
# 0 = No Heart Disease
# 1 = Heart Disease

target = [0, 1, 0, 1]

print(type(target[0]))

# Output:
# <class 'int'>

# Although the values are integers, they represent categories.

# Points:
# - It helps identify the prediction problem.
# - It helps in choosing the correct machine learning algorithm.
# - It helps in proper data analysis.
# - It reduces the chances of selecting the wrong model.

# Example:
# target = [0,1,0,1]
# This represents categories, so it is a classification problem.

# target = [120.5,135.8,140.2]
# This represents continuous values, so it is a regression problem.


# ==========================================================
# 4. You compute the correlation between age and heart disease
# presence and get 0.23. What does a correlation value tell you
# about two variables?
# ==========================================================

# Answer:

# Correlation is a measure that shows the relationship between two variables.
# It tells us whether two variables move together and how strong that relationship is.

# Correlation Value Meaning:
# +1 = Perfect Positive Relationship
#  0 = No Relationship
# -1 = Perfect Negative Relationship

correlation = 0.23

# The correlation between age and heart disease is 0.23.
# This indicates a weak positive relationship.

# Points:
# - As age increases, the chance of heart disease may increase slightly.
# - The relationship exists but is not very strong.
# - Age alone cannot accurately predict heart disease.
# - Other factors also affect the disease.

# Example:
# Age   Heart Disease
# 35    No
# 45    No
# 55    Yes
# 65    Yes

# In this example, older individuals appear more likely to have heart disease,
# but there can be exceptions.


# ==========================================================
# 5. A hospital rule says:
# if cholesterol > 240, flag as high risk.
# What is the fundamental difference between a rule-based system
# and a data-driven approach?
# ==========================================================

# Answer:

# A rule-based system and a data-driven approach are two different
# ways of making decisions.

# Rule-Based System:
# A rule-based system follows predefined rules created by experts.

cholesterol = 250

if cholesterol > 240:
    print("High Risk")

# Points:
# - Uses fixed rules.
# - Easy to understand.
# - Gives the same result every time.
# - Cannot learn from new data.

# Data-Driven Approach:
# A data-driven approach learns patterns from data and makes predictions automatically.

# It may use:
# - Age
# - Cholesterol
# - Blood Pressure
# - Heart Rate

# to predict the risk of heart disease.

# Points:
# - Learns from previous data.
# - Can identify complex patterns.
# - Improves when more data is available.
# - Usually provides better predictions.

# Example:
# A patient may have cholesterol below 240 but still be at high risk
# because of age and blood pressure.
# A data-driven model can identify such cases using historical data.

# Difference Between Rule-Based System and Data-Driven Approach

# Rule-Based System:
# - Uses fixed rules
# - Created manually
# - Does not improve by itself
# - Easy to understand

# Data-Driven Approach:
# - Learns from data
# - Learns automatically
# - Improves with more data
# - More flexible