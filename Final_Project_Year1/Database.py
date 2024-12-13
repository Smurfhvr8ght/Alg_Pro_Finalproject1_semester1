import csv

path = 'Final_Project_Year1/scores.csv'

#rewrite the CSV from ground up with List of Dicts
def update(a):
    temp = a
    with open(path, 'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Username','Score'])
        for dict in temp:
            name = dict['Username']
            score = dict['Score']
            writer.writerow([name,score])
    f.close()

#CSV updater to update highscore data
class Data:
    #stored data
    def __init__(self):
        self.values = self.get_data()

    #get dict from csv
    def get_data(self):
        with open(path,'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            datas = []
            for row in csv_reader:
                datas.append(row)
        csv_file.close()
        return datas
    
    #Remove empty line in between for my eye (also update self.values)
    def update_list(self):
        #Update Class data
        self.values = self.get_data()
        #rewrite CSV
        update(self.values)
    
    #sort CSV from low to high
    def sort(self):
        #make temp list of location and score
        temp = []
        for i in range(len(self.values)):
            temp.append([i,self.values[i]['Score']])
        #sort the temp base on score
        for i in range(len(temp)-1):
            for j in range(i,len(temp)):
                if float(temp[i][1]) > float(temp[j][1]):
                    temp[i],temp[j] = temp[j],temp[i]
        #edit CSV
        temp1 = []
        for i in temp:
            temp1.append(self.values[i[0]])
        update(temp1)
        #fixing the original dict
        self.values = temp1

#the actualy used methods
    #add data to CSV file
    def append(self,name,score):
        data=[name,score]
        with open(path, 'a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow('')
            writer.writerow(data)
        f.close()
        self.update_list()
        self.sort()

    #edit score
    def change_score(self,name,score):
        y = 0
        for dict in self.values:
            if dict['Username'] == name:
                dict['Score'] = score
                break
        #rewrite the CSV with the edited data
        update(self.values)
        self.sort()

    #update CSV
    def update(self,name,score):
        edit=False
        for i in self.values:
            if i['Username'] == name:
                if float(i['Score']) > score:
                    edit=True
                    break
        if edit:
            self.change_score(name,score)
        else:
            self.append(name,score)
        self.sort()

    #delete data
    def del_user(self,name):
        for i in self.values:
            if i['Username'] == name:
                self.values.remove(i)
                #rewrite the CSV with the edited data
                update(self.values.copy())
    
    #get top 5 score in dict
    def get_top5(self):
        self.sort()
        temp = self.get_data()
        and_temp = []
        for i in range(5):
            try:
                and_temp.append(temp[i])
            except:
                break
        return and_temp