#dictionaries
#allow you to group and tag pieces of related information
#key:value pairs that provide context for that value.

#syntax = {
# key1:value1,
# key2:value2,...
# keyn:valuen
# }
programming_dict = {
"bug":"an error in a program",
"function": "A piece of code that you can easily call over and over again"
}

#we can find the value for a given key by setting it within an index slice.
#Key must be spelled correctly. key must have the correct data type. str > str, int> int etc.  
print(programming_dict["bug"])

#adding data to the dictionary.
programming_dict["Loop"] = 'The action of doing something repeatedly based on criteria.'

print(programming_dict)

#it can be useful to start with an empty dictionary.
empty_dict = {}

#wipe an existing dictionary by setting the variable equal to empty curly brackets. 
#useful to reset progress or remove user information. 

#editing an item in a dictionary 
#programming_dict["bug"] = 'a moth in your computer'
#print(programming_dict)

#looping through a dictionary. 
for key in programming_dict:
    print(key)
    print(programming_dict[key])

#excercise 1
#create a new dictionary that assigns a value based on an int score from another dictionary
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
#loop through > get key > assign value based on score. 
for key in student_scores:
    if 91 <= student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif 81 <= student_scores[key] <=90:
        student_grades[key] = "Exceeds Expectations"
    elif 71 <= student_scores[key] <=80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
    
print(student_grades)

#nested dictionaries.
#single values are not the only things that can be stored in a dictionary. Lists and other dicts are storage capable. 

new_dict = {
    "Fruit":['apple','banana','cherry'],
     "Bob": {
        "job": "Data Analyst",
        "salary": 65000,
        "favorite animal": "Koala"
     }
}

