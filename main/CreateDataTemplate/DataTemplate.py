import csv
import copy

def Time(second):
  hour,r=divmod(second, 3600)
  minutes,second=divmod(r, 60)
  hour= str(hour).zfill(2)
  minutes= str(minutes).zfill(2)
  second= str(second).zfill(2)
  return hour,minutes,second

def VHNum(VENum):
  if(VENum%8==0):
    njob=VENum//8
  else:
    njob=VENum//8+1
  return njob

def Urgent(PreemtionData,ResultData,UrgentVE,jobNum,StartUrgentJob,DeadLine):
  UrgentJob=PreemtionData[0].copy()
  #job番号の記載
  UrgentJob[3]=str(jobNum)
  #que_name
  UrgentJob[4]=str("urgent")
  hour,minutes,second=Time(StartUrgentJob)
  t=[0,9,11,12]
  #時刻を入力
  for z in range(4):
    if(t[z]==12):
      UrgentJob[t[z]]="2021/1/1"+" "+hour+":"+minutes+":"+second
    else:
      UrgentJob[t[z]]="2021/1/1 0:00:00"
  #elpstime
  UrgentJob[14]=str(DeadLine+100)
  #etime
  UrgentJob[15]=ResultData[1]
  #VE
  UrgentJob[19]=str(UrgentVE)
  UrgentJob[20]=str(UrgentVE)
  #njobs
  njobs=VHNum(UrgentVE)
  UrgentJob[17]=str(njobs)
  #cpunum_req
  UrgentJob[22]=str(njobs*2)
  #memory
  UrgentJob[35]=str(1)  
  return UrgentJob


def CopyData(num,CopyData,endTime,data_before,etime):
  for i in range(num):
    for j in range(1,len(data_before)):
      tmp_list=[]
      tmp_list=data_before[j].copy()
      #job番号の記載
      tmp_list[3]=str(2000+1000*i+int(tmp_list[3]))   
      #elpstimeとetime
      tmp_list[15]=str(int(etime*(1+0.1*i)+j))
      tmp_list[14]=str(int(tmp_list[15])+100)
      #時刻を入力
      t=[0,9,11,12]
      for z in range(len(t)):
        hour,minutes,second=Time(endTime)
        tmp_list[t[z]]="2021/1/1"+" "+hour+":"+minutes+":"+second 
      CopyData.append(tmp_list)

#(選ばれた番号,ResultData,BreakData,出力先,slurm_list)
def WriteDataTemplate(name,ResultData,BreakData,OutputData,endTime,data_before,jobcomp_before,StartUrgentJob,DeadLine,CopyNumber):
  num=int(ResultData[0])-1
  #slurm.conf用
  slurm_list=[]
  deafault=["PartitionName=","Nodes=","Default=Yes", "DefMemPerCPU=2800","MaxTime=INFINITE","State=UP"]
  BreakVH=[]
  PreemtionData=[]
  #中断ジョブをPreemtionDataに入れる
  for i in range(len(data_before)):
    tmp_list=[]
    if(i==0):
      tmp_list=data_before[i].copy()
      OutputData.append(tmp_list)
    else:
      if(i in BreakData[num]):
        tmp_list=data_before[i].copy()
        PreemtionData.append(tmp_list)
      else:
        tmp_list=data_before[i].copy()
        OutputData.append(tmp_list)
  #緊急ジョブと中断されたジョブを追加
  Premption=[]
  UrgentJob=[]
  queNum=0
  for i in range((len(PreemtionData))+1):
    tmp_list=[]
    # tmp_list_2=[]
    if(i==len(PreemtionData)):
      #緊急ジョブのVE数の判断
      if(int(ResultData[0])%8==0):
        Urgent_tmp=Urgent(PreemtionData,ResultData,int(ResultData[0]),1000,StartUrgentJob,DeadLine)
        UrgentJob.append(Urgent_tmp)
      else:
        q,mod= divmod(int(ResultData[0]), 8)
        Urgent_tmp=Urgent(PreemtionData,ResultData,8*q,1000,StartUrgentJob,DeadLine)
        UrgentJob.append(Urgent_tmp)
        Urgent_tmp=Urgent(PreemtionData,ResultData,mod,2000,StartUrgentJob,DeadLine)
        UrgentJob.append(Urgent_tmp)
    else:
      queNum+=1
      tmp_list=PreemtionData[i].copy()
      # tmp_list_2=PreemtionData[i].copy()
      # #job番号の記載
      # tmp_list_2[3]=str(1000+int(tmp_list_2[3]))
      #que_name
      tmp_list[4]=str("que"+str(queNum))
      # tmp_list_2[4]=str("que"+str(queNum))
      for j in range(1,len(jobcomp_before)):
        if(jobcomp_before[j][0]==tmp_list[3]):
          default=["PartitionName="+str("que"+str(queNum)),"Nodes="+jobcomp_before[j][21],"Default=Yes", "DefMemPerCPU=2800","MaxTime=INFINITE","State=UP"]
          if("[" in jobcomp_before[j][21][4:]):
            str_list1=[]
            VHStr=jobcomp_before[j][21][4:]
            VHStr=VHStr[1:-1]
            if("," in VHStr):
              str_list1=VHStr.split(",")
              for tmp in str_list1:
                if("-" in tmp):
                  str_list2=[]
                  str_list2=VHStr.split("-")
                  for i in range(int(str_list2[0]),(int(str_list2[-1])+1)):
                    BreakVH.append(i)
                else:
                  BreakVH.append(int(tmp))
            else:
              str_list2=[]
              str_list2=VHStr.split("-")
              for i in range(int(str_list2[0]),(int(str_list2[-1])+1)):
                BreakVH.append(i)
          else:
            BreakVH.append(int(jobcomp_before[j][21][4:]))
          slurm_list.append(default)
          break
      # #etime
      # tmp_list_2[15]=str(int(tmp_list[15])-StartUrgentJob)  
      # tmp_list[15]=str(StartUrgentJob)  
      #elapsTime
      tmp_list[14]=str(int(tmp_list[15])+100)    
      hour,minutes,second=Time(int(float(ResultData[1])))
      #時刻を入力
      t=[0,9,11,12]
      for z in range(4):
        if(t[z]==12):
          tmp_list[t[z]]="2021/1/1"+" "+hour+":"+minutes+":"+second  
        else:
          tmp_list[t[z]]="2021/1/1 0:01:00"
      #データを追加
      OutputData.append(tmp_list)
  #書き込み
  OutputData.extend(UrgentJob)
  copydata=[]
  CopyData(CopyNumber, copydata,endTime,data_before,300)
  OutputData.extend(copydata)

  #urgentJobのSlurm_list作り
  BreakVH.sort()
  tmp_num=BreakVH[0]
  tmp_list=[]
  nodes="sxat["
  for i in range(1,len(BreakVH)):
    if(BreakVH[i]==tmp_num):
      pass
    elif(BreakVH[i]!=tmp_num+1):
      if(len(tmp_list)<=1):
        nodes+=str(tmp_num)+","
        tmp_num=BreakVH[i]
      else:
        nodes+=str(tmp_list[0])+"-"+str(tmp_list[-1])+","
        tmp_list=[]
        tmp_num=BreakVH[i]
    else:
      if(len(tmp_list)==0):
        tmp_list.append(tmp_num)
        tmp_list.append(BreakVH[i])
      else:
        tmp_list.append(BreakVH[i])
      tmp_num=BreakVH[i]
    if(i==len(BreakVH)-1):
      if(len(tmp_list)<=1):
        nodes+=str(tmp_num)+"]"
        tmp_num=BreakVH[i]
      else:
        nodes+=str(tmp_list[0])+"-"+str(tmp_list[-1])+"]"
  deafault[0]+="urgent"
  deafault[1]+=nodes
  slurm_list.append(deafault)
  print(name)
  #slurm_listを出力
  for tmp in slurm_list:
    print(*tmp)
  
  return OutputData


def DefaultWriteDataTemplate(OutputData,endTime,data_before,jobcomp_before,StartUrgentJob,CopyNumber):
  OutputData.extend(data_before)
  copydata=[]
  CopyData(CopyNumber, copydata,endTime,data_before,300)
  OutputData.extend(copydata)
  return OutputData