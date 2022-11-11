import pandas as p

'''
create new csv with fur color, and count
'''

data = p.read_csv('D://Coding Projects/100 Days of Code/OHDC_25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey = data['Primary Fur Color'].value_counts()['Gray']
red = data['Primary Fur Color'].value_counts()['Cinnamon']
black = data['Primary Fur Color'].value_counts()['Black']

dict = {
'Fur Color': ["Grey","Cinnamon","Black"]
, 'Count': [grey, red, black]

}
df = p.DataFrame(dict)

df.to_csv('Squirrel_Population_Counts.csv')