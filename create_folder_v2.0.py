#!/usr/local/bin/python3.13
import os

ch_no_counter = 0
ch_name_counter = 0

folder_path = input("Enter folder path: ")
mode = 0o777
client_code = input("Enter client code: ").upper()
book_name = input("Enter your book name: ").title()
path = folder_path+"/"+client_code+"_"+book_name
prefix = client_code +"_"+ book_name +"_"
permanent_folders = ["Cover","Front Index","Back Index","Eplilogue","Prologue","Acknowledgements"]

no_add_permanent_folder = int(input("Enter no of extra folders: "))
n_permanent_folders = []
n_permanent_folders = [input(f"{i+1}). Enter additional folder name: ") for i in range(no_add_permanent_folder)]

permanent_folders.extend(n_permanent_folders)

n = int(input("Enter total number of chapters in book: "))
chapter_dict = [[input(f"{i+1}). Chapter Number: "),input(f"{i+1}). Chapter's Name: ")] for i in range(n)]

chapter_no_dict = {}

print(chapter_dict)

for x in permanent_folders:
    try:
        final_path = os.path.join(path,prefix+x.title())
        os.makedirs(final_path,mode)
        print("Directory Created")
    except OSError as err:
        print("Error in creating directory: "+str(err))

for x in chapter_dict:

    try:
        chapter_no_dict.setdefault(x[0],0)
        chapter_no_dict[x[0]] = chapter_no_dict[x[0]] + 1

        if x[1] == "":
            x[1] = "Null Name"
            if ch_name_counter>0  and x[0] == "":
                x[1] = f"Null Name {chapter_no_dict[x[0]]}"
            ch_name_counter = ch_name_counter + 1
        
        if x[0] == "":
            x[0] = "Null"
            # if ch_no_counter>0:
            #     x[0] = f"Null {ch_no_counter}"
            # ch_no_counter = ch_no_counter + 1
        
        print
        if x[0].find("-"):
            x[0] = x[0].replace("-","  ")
     
        if x[0].find("#"):
            x[0] = x[0].replace("#","  ")
     
        if x[0].find("$"):
            x[0] = x[0].replace("$","  ")

        if x[0].find("@"):
            x[0] = x[0].replace("@","  ")

        if x[0].find(","):
            x[0] = x[0].replace(",","  ")



        if x[1].find("-") :
            x[1] = x[1].replace("-","  ")

        if x[1].find("#"):
            x[1] = x[1].replace("#","  ")
     
        if x[1].find("$"):
            x[1] = x[1].replace("$","  ")

        if x[1].find("@"):
            x[1] = x[1].replace("@","  ")

        if x[1].find(","):
            x[1] = x[1].replace(",","  ")

        final_path = os.path.join(path,prefix+"Chapter "+x[0].title()+"_"+x[1].title())
        os.makedirs(final_path,mode)
        print("Directory Created")
    
    except OSError as err:
        print("Error in creating directory: "+str(err))   
print(chapter_no_dict)
