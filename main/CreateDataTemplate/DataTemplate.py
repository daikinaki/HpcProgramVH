import csv
import copy
import random

def Time(second):
  hour,r=divmod(second, 3600)
  minutes,second=divmod(r, 60)
  hour= str(hour).zfill(2)
  minutes= str(minutes).zfill(2)
  second= str(second).zfill(2)
  return hour,minutes,second


def Urgent(PreemtionData,ResultData,UrgentVH,jobNum,StartUrgentJob,DeadLine):
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
  UrgentJob[19]=str(UrgentVH*8)
  UrgentJob[20]=str(UrgentVH*8)
  #njobs
  njobs=UrgentVH
  UrgentJob[17]=str(njobs)
  #cpunum_req
  UrgentJob[22]=str(njobs*2)
  #memory
  UrgentJob[35]=str(1)  
  return UrgentJob

def DummyPreemtionData(data,num,etime):
  #job番号の記載
  data[3]=str(num)
  #elps_time
  data[14]=str(etime+100)
  # etime  
  data[15]=str(etime)
  #njobs
  data[17]=str(1)
  #VE
  data[19]=str(1*8)
  data[20]=str(1*8)
  #cpu_num_req
  data[22]=str(1*2)
  #memory
  data[35]=str(num)
  return data

#1VHのジョブを作る
def OneVHJobCreate(t,sumVH,data_before,jobnum,PreemtionData):
  for i in range(sumVH):
    Bool=True
    value=t
    while Bool:
      tmp_list=data_before[1].copy()
      #etimeの決定
      if(value<600):
        eTime=value
        Bool=False
      else:
        eTime=random.randint(400,600)
      DummyPreemtionData(tmp_list,jobnum,eTime)
      value-=eTime
      jobnum+=1
      PreemtionData.append(tmp_list)
  return jobnum

#中断用データ
def PreemtionDataCreate(OccupyVH,difVH,data_before,DeadLine,UrgentCount,DatasetTotalTime):
  PreemtionData=[]
  if(OccupyVH!=0):
    tmp_list=data_before[1].copy()
    urgentoccupyTime=DeadLine*UrgentCount
    etime=DatasetTotalTime-urgentoccupyTime
    #que名の変更
    tmp_list[4]="que"
    #job番号の記載
    tmp_list[3]=str(1)
    #elps_time
    tmp_list[14]=str(etime+100)
    # etime  
    tmp_list[15]=str(etime)
    #njobs
    tmp_list[17]=str(OccupyVH)
    #VE
    tmp_list[19]=str(OccupyVH*8)
    tmp_list[20]=str(OccupyVH*8)
    #cpu_num_req
    tmp_list[22]=str(OccupyVH*2)
    PreemtionData.append(tmp_list)
    jobnum=2
    jobnum=OneVHJobCreate(urgentoccupyTime, OccupyVH,data_before,jobnum,PreemtionData)
  else:
    jobnum=2
  OneVHJobCreate(DatasetTotalTime, difVH,data_before,jobnum,PreemtionData)
  return PreemtionData




#(選ばれた番号,ResultData,BreakData,出力先,slurm_list)
def WriteDataTemplate(ProposedResult,ExpectedResult,data_before,DatasetTotalTime,DeadLine,UrgentCount):
  #出力先
  ProposedData=[]
  ExpectedData=[]
  DefaultData=[]
  #先頭を追加
  ProposedData.append(data_before[0])
  ExpectedData.append(data_before[0])
  DefaultData.append(data_before[0])
  #VH数の確認と差分の用意
  ProposedVH=ProposedResult[0]
  ExpectedVH=ExpectedResult[0]
  VHdif=ExpectedVH-ProposedVH
  #中断用の占有データ作る
  #Proposed&Default
  Preemtiondata=PreemtionDataCreate(ProposedVH,VHdif,data_before,DeadLine,UrgentCount,DatasetTotalTime)
  ProposedData.extend(Preemtiondata)
  DefaultData.extend(Preemtiondata) 
  #Expected
  Preemtiondata=PreemtionDataCreate(ExpectedVH,0,data_before,DeadLine,UrgentCount,DatasetTotalTime)
  ExpectedData.extend(Preemtiondata) 
  #共通の通常ジョブ作る
  #UrgentJob作り

  return ProposedData,ExpectedData,DefaultData
