import pandas as pd 
import numpy as np

#1) IMPORT Data set ----------------------------------------------
data = pd.read_csv('../data-sets/car_fleet_sample.csv')

#2) IDENTIFY MISSING DATA ------------------------------------------
# ISNULL is a powerful method used to help you FIND empty values in a table.

print(data) #OUTPUT- data in table format with Keys:Values 

print(data.isnull()) #OUTPUT- data with Key:BooleanValue- if Value == UNDEFINED/NaN then Value=TRUE.   
print(data.isnull().sum())#OUTPUT- returns all data columns and specifies which ones have UNDEFINED/NaN values

# you have TWO choices when cleaning data 1) we DROP the Data 2) INPUT missing data

#3) DROP Data Columns ----------------------------------------------------
removeColumns = ['vin'] #Specify columns to remove
data.drop(removeColumns, inplace =True, axis =1)#OUTPUT data without specified columns 
# print(data)

#4 CUSTOM INPUT missing Data ---------------------------------------------
data['zeroSixty'] = data['zeroSixty'].fillna('Em9Ty')
print(data['zeroSixty'])
# print(data)

#5 identify DUPLICATES --------------------------------------------------
print(data.duplicated())

#6 DROP_DUPLICATES() ---------------------------------------------------
print(data.drop_duplicates())

#7 Detect outliers -----------------------------------------------------
# this is data that is so far out that it is possibly a "misread"
print(data['year'].describe())

data

