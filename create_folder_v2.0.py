#!/usr/local/bin/python3.13
import os

path = "/home/satyender/Documents/pythonScripts/WF_1007"
mode = 0o777
client_code = input("Enter client code: ").upper()
book_name = input("Enter book name: ").title()
prefix = client_code +"_"+ book_name +"_"
permanent_folders = ["cover","front_index","Back_Index","eplilogue"]

'''
chapter_num = [i for i in input("Enter chapter number: ").split(",")]
print(chapter_num)

chapter_name = ["Null Name" for x in chapter_num]
'''

n = int(input("Enter total number of chapters: "))
chapter_dict = {input(f"{i+1}). chapter number: "):input(f"{i+1}). chapter name: ") for i in range(n)}

chapter_dict.setdefault("Null","Null Name")
print(chapter_dict)

for x in permanent_folders:
    try:
        final_path = os.path.join(path,prefix+x.title())
        os.makedirs(final_path,mode)
        print("Directory Created")
    except OSError as err:
        print("Error in creating directory: "+str(err))

for x,y in zip(chapter_dict, chapter_dict.values()):
    try:
        final_path = os.path.join(path,prefix+"Chapter "+x.title()+"_"+y.title())
        os.makedirs(final_path,mode)
        print("Directory Created")
    except OSError as err:
        print("Error in creating directory: "+str(err))   

