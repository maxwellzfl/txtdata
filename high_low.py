
# result=[]
# with open('/Users/zhangfangli/Documents/overdue_train.txt','r') as f:
#     for line in f:
#         result.append(list(map(int,line.split(','))))
# overdue_flags=[]
#
# for value in range(0,len(result)):
#     overdue_flags.append(result[value][1])
#
# print(overdue_flags.count(0))
# print(overdue_flags.count(1))

import csv
filename = '/Users/zhangfangli/Documents/cmmt.csv'
with open(filename,'r') as f:
    reader= csv.reader(f)
    header_row= next(reader)
   # print(header_row)
    for index,column_header in enumerate(header_row):
        print(index,column_header)
    cmmt_months= []
    for row in reader:
        cmmt_months.append(float(row[1]))

  #  print(cmmt_months)
import random
max_cmmt= []
for value in range(0,len(cmmt_months)):
    max_cmmt.append(cmmt_months[value]+30*random.random())

print(max_cmmt)
print(cmmt_months)
from matplotlib import pyplot as plt

fig= plt.figure(dpi=128,figsize=(6,3))
plt.plot(cmmt_months[1:20],c='red')
plt.plot(max_cmmt[1:20],c='blue')
plt.fill_between(range(0,19),cmmt_months[1:20],max_cmmt[1:20],alpha=0.5)
plt.title("the reviews of MT's customers about company",fontsize=10)
plt.xlabel('',fontsize= 10)
plt.ylabel("months",fontsize=10)

plt.show()

