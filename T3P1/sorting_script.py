import os
import shutil
import time


def sort_by_year(route, year_start, year_end):
    print("Sort by Age")
    os.chdir(route)
    if os.path.exists(route) and os.path.isdir(route):
        files = os.listdir(route)
        for files in files:
            date = time.ctime(os.path.getmtime(files))
            year = int(date.replace("  ", " ").split(" ")[4])
            absolute_path = os.path.abspath(files)
            if year_start <= year <= year_end:
                new_folder = str(route) + '/' + str(year)
                if not os.path.exists(new_folder):
                    os.mkdir(os.path.abspath(new_folder))
                    shutil.move(absolute_path, os.path.abspath(new_folder))
                else:
                    shutil.move(absolute_path, new_folder)


def sort_by_month(path, age1, age2):
    os.chdir(path)
    if os.path.exists(path) and os.path.isdir(path):
        files = os.listdir(path)
        for files in files:
            date = time.ctime(os.path.getmtime(files))
            year = int(date.replace("  ", " ").split(" ")[4])
            month = date.replace("  ", " ").split(" ")[1]
            absolute_path = os.path.abspath(files)
            if age1 <= year <= age2:
                new_folder = str(path) + '/' + str(year)
                new_subfolder = str(path) + '/' + str(year) + '/' + str(month)
                if not os.path.exists(new_folder):
                    os.mkdir(os.path.abspath(new_folder))
                    new_subfolder = str(path) + '/' + str(year) + '/' + str(month)
                    os.mkdir(os.path.abspath(new_subfolder))
                    shutil.move(absolute_path, os.path.abspath(new_subfolder))
                else:
                    if not os.path.exists(new_subfolder):
                        os.mkdir(os.path.abspath(new_subfolder))
                        shutil.move(absolute_path, os.path.abspath(new_subfolder))
                    else:
                        shutil.move(absolute_path, os.path.abspath(new_subfolder))


path = input("Add the path to the folder you want to sort: ")
year_start = int(input("Sort from year: "))
year_end = int(input("Sort to year ->"))
print("Do you want to sort by year or by month and year?")
print("1. Sort by year")
print("2. Sort by month and year")
selection = int()

sort_by_year(path, year_start, year_end) if selection == 1 else sort_by_month(path, year_start, year_end)

print("Your files have been correctly sorted")
