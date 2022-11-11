# what is a csv file. comma seperate values.
# way of storing tabular data. csv is common spreadsheet form.

#collin, 23, archer

import pandas as p
import csv

#reading csv file contents on a file directory pathway
with open('D://Coding Projects/100 Days of Code/OHDC_25/weather_data.csv') as data_file:
    data = data_file.readlines()
    print(data)
#reading csv files
with open('D://Coding Projects/100 Days of Code/OHDC_25/weather_data.csv') as data_file:
    #utilizing the csv library
    data = csv.reader(data_file)
    #skipping first row of data.
    next(data_file)
    #temperature list to append to.
    temperatures = []
    
    #appending the contents of temp > column 2 > index 1
    for row in data:
        temperatures.append(row[1])

    # printing contents of temp list. 
    print(temperatures)

#using pandas
#pandas offeres a lot of different tools to manipulate the data and make it into different data types or formats
data = p.read_csv('D://Coding Projects/100 Days of Code/OHDC_25/weather_data.csv')

temp =data['temp'].tolist()
print(sum(temp)/len(temp))

#you can even access statistical methods within panda
#within the data frame you have to be careful which name you implement. 
#If your column name doesn't match it will throw an error.  
print(data['temp'].mean())

#return the row where the data = to monday
print(data[data.day == "Monday"])

#returning the row where the temp value is the max amount in the table. 
print(data[data.temp == data.temp.max()])

#data.to_csv makes a new csv file from data that we've manipulated in the dataframe. 