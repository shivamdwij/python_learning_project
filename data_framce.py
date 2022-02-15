from ast import Index
from pandas import DataFrame
data_frame={'Name':["Shivam","Mrity","Suvidha"],'Age':[30,26,39],'Salary': [9,6,2]}  # inthe IDE it will throw an error but works well with in the shell
frame=DataFrame(data_frame)
print(frame)    

from pandas import Series
s1 = Series(['Apple','Banana','Manago'], index=['a','b','c'])
print(s1)