import csv

def DataRead(name,OutPut):
  with open("./jobcomp/jobcomp_"+name+".log","r")as f:
    #２次元配列化
    line = f.readlines()
    for tmp in line:
      OutPut.append(tmp.split('|'))
  return OutPut


