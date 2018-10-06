# Required Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import re

database = {}
user_query = True
while user_query:
    email_query=True
    while email_query:
        email_address = input("Email address: ")
        if '@' and '.' not in email_address:
            print(" ------------------------------")
            print("| Enter correct email address! |")
            print(" ------------------------------")
        else:
            email_query=False
    tv_series = list(map(str, input("TV Series: ").strip().split(',')))
    database.update({email_address:tv_series})
    query = input("More inputs(Y/N): ")
    if user_query== 'n' or query == 'n':
        user_query=False

===============PANDAS DATAFRAME==============#
obj=pd.DataFrame(database)
print(ovj)

#==============CSV================#
inputfile = csv.reader(open('database.csv', 'r'), delimiter='\t')

values=['gotham','suit']

for row in inputfile:
    # for key, value in database.items():
    for tvshow in values:
        if tvshow.title() in row:
            print(row[0])

# for key,value in database.items():
#     for tvshow in value:
#         print(tvshow)

