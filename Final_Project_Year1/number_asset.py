import os

#making the number
def num_array_list():
    num_path = r'Final_Project_Year1/Asset/numbers'
    dict = {}
    c = 1

    for files in os.listdir(num_path):
        dict[c] = num_path + '/' + files
        c+=1
    return dict
