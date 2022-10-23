import csv
import random
#元データ読み込み
with open("./main/extract_data.csv","r")as f:
  #２次元配列化
  line = f.readlines()
  s=[]
  for tmp in line:
    s.append(tmp.split(','))

DataList=[]

#整数に直す
for tmp in s:
  tmp_list=[]
  for i in range(len(tmp)):
    tmp_list.append(int(tmp[i]))
  DataList.append(tmp_list)

with open("./main/data_template_before.csv","r")as f:
  #２次元配列化
  line = f.readlines()
  data_before=[]
  for tmp in line:
    data_before.append(tmp.split(','))

with open("./main/jobcomp_before.log","r")as f:
  #２次元配列化
  line = f.readlines()
  jobcomp_before=[]
  for tmp in line:
    jobcomp_before.append(tmp.split('|'))
