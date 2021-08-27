# Importing needed libraries for generating data and render our plots inline
#%matplotlib inline
#%config InlineBackend.figure_format = 'retina'

# A simple request to gather students data
from pywebio.input import *
from pywebio.output import *


from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import math

import re
import numpy as np 
# Make the graphs a bit bigger
matplotlib.style.use(['seaborn-talk', 'seaborn-ticks', 'seaborn-whitegrid'])

df = pd.read_excel(r'cstcourses_grades.xlsx')

df.head()

#list of courses we have
def list_courses():
#     courses=set(df['Catalog'])
    courses=set(list(zip(df['Catalog'],df['Label']))) 
    return courses
def get_grade(x):
    if x==4:
        return 'A'
    elif x==3:
        return 'B'
    elif x==2:
        return 'C'
    else:
        return 'D'
def get_numberofhours(g):
    grade_hours={'A':'''You are more likely to be fine at this calss. You still need to 
                 study at least 3 hours per week for a grade A''',
                 'B':''' This class will require from you some attention. You need
                 to study at least 5 hours per week for a grade B''',
                 'C':''' This class is challenging. However, studying at least 
                  8 hours per week will save you and hope for a grade C''',
                 'D':'''You like to be challenged!!! This class required your full attention. At least 10 hours per 
                 week is required for this class for a grade D'''}
    result=grade_hours[g]
    return result

grade_numbers={'A':4,'B':3,'C':2,'D':1}
courses_performance={}
courses=list_courses()
for item,lab in courses:
    cond=(df['Catalog']==item)
    subset=df[cond]
    my_sum=0
    my_avg=0
    for grade in subset['Grade']:
        my_sum +=grade_numbers[grade]
    my_avg=int(my_sum/len(subset['Grade']))
    courses_performance[item]={}
    courses_performance[item]['Grade']=get_grade(my_avg)
    courses_performance[item]['Notes']=get_numberofhours(courses_performance[item]['Grade'])
    
def check_existant(c):
    if c not in courses_performance.keys():
        return False
    return True  


def check_classes():
    
    put_image('https://upload.wikimedia.org/wikipedia/en/3/30/City_Tech.png', width='350px')
    put_success('Welcome to StudyTime, This pseudo_app is mainly handling CST catagories classes')
    
    
    #student_name = input("Input your name：")

    selections = []
    for course in courses:
        selections.append(course[0])

    course_code = select("Which class do you want?", options=selections)
         
    student_grade = input("Which grade you are aiming for：")
    student_hours = int(input("How many hours do you study per week on average?"))
        

    top_status = {'A': 3, 'B': 5,
                  'C': 8, 'D': 10}
    grade_control={'A': 4, 'B': 3,
                  'C': 2, 'D': 1}
                  
    class_dificulty=courses_performance[course_code]['Grade']
    if student_grade==class_dificulty:
        if student_hours>=top_status[class_dificulty]:
            put_text(f"Since you are aiming for {student_grade},The class avereage grade from the previous semester was also {class_dificulty}, with the numbers of hours you specified, you are safe")
        else:
            put_text('''You need to study more hours per week to pass this class with the grade you want: Here is more information
                           ''',courses_performance[course_code]['Notes'])
        
    else:
        if grade_control[student_grade]<grade_control[class_dificulty]:
            put_text(f"This class average grade is {class_dificulty}. So, you should aim for at least {class_dificulty} or more")
        else:
            extra_hours=round(top_status[class_dificulty]*(1.3**(grade_control[class_dificulty])))
            if student_hours<extra_hours:
                put_text('''Your hours seem to be less than the average number of hours required to get this grade: You need at least''',extra_hours, 'hours')
                put_text('''Here is more information about the current class ''',courses_performance[course_code]['Notes'])
            else:
                put_text('With the hours you specified you are more likely going to get your aiming grade. Good Luck!!!')

courses=set(list(zip(df['Catalog'],df['Label'])))

if __name__ == '__main__':
    check_classes()