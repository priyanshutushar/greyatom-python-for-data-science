# --------------
import numpy as np

new_record = [[50,4,4,1,1200,0,40,0]]
new_record1 = np.asarray(new_record)

data = np.genfromtxt(path,delimiter=",",skip_header=1)

census = np.concatenate((data,new_record1))

age = np.array(census[:,0])

max_age = np.max(age)
min_age = np.min(age)
age_mean = round(age.mean(),2)
age_std = round(np.std(age),2)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)

race = census[:,2]
row = -1
race_0 = []
race_1 = []
race_2 = []
race_3 = []
race_4 = []

for i in race:
    row+=1
    if i==0:
        race_0.append(list(census[row,:]))
    if i==1:
        race_1.append(list(census[row,:]))
    if i==2:
        race_2.append(list(census[row,:]))
    if i==3:
        race_3.append(list(census[row,:]))
    if i==4:
        race_4.append(list(census[row,:]))

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minority_race = min(len_0,len_1,len_2,len_3,len_4)
print(minority_race)

senior_citizens = list(filter(lambda age: age[0]>60,census))
senior_citizens = np.array(senior_citizens)
working_hours_sum = senior_citizens.sum(axis=0)[6]
senior_citizens_len = len(senior_citizens)
avg_working_hours = round(working_hours_sum/senior_citizens_len,2)
print(avg_working_hours)

high = list(filter(lambda education_num: education_num[1]>10,census))
low = list(filter(lambda education_num: education_num[1]<=10,census))

high = np.array(high)
high_sum = high.sum(axis=0)[7]
high_len = len(high)
avg_pay_high = round(high_sum/high_len,2)

low = np.array(low)
low_sum = low.sum(axis=0)[7]
low_len = len(low)
avg_pay_low = round(low_sum/low_len,2)

print(avg_pay_high)
print(avg_pay_low)


