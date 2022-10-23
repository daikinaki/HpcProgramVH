import pandas as pd
import matplotlib.pyplot as plt

def DeadLineCompare(name,Minimum,Random,Expected,TraialNumer):
  print(name)
  data=[]
  data.extend(["name","VE","ResouceTime","TotalTime","FinishTime"])
  print(*data,sep=',')
  for i in range(TraialNumer+2):
    data=[]
    if(i==0):
      data.extend(['{}'.format("提案手法"),Minimum[0],Minimum[0]*Minimum[1],Minimum[1],Minimum[4]])
    elif(i==TraialNumer+1):
      data.extend(['{}'.format("期待値"),Expected[0],Expected[0]*Expected[1],Expected[1],Expected[4]])
    else:
      data.extend(['{}:({})'.format("ランダム",i),Random[i-1][0],Random[i-1][0]*Random[i-1][1],Random[i-1][1],Random[i-1][4]])
    print(*data,sep=',')
