import random
import copy

def RandomAlgorithm(Result,BreakData,TraialNumer,DataList,ReadOverHead,WriteOverHead,TotalTime,DeadLine):
  for i in range(TraialNumer):
    #ループが戻ったため、初期状態に戻す
    DummyData=DataList.copy()
    sumVE=0
    sumMemory=0
    BreakTmp=[]
    Bool=True
    while Bool:
      DataListNum=len(DummyData)-1
      n=random.randint(0,DataListNum)
      sumVE+=DummyData[n][1]
      sumMemory+=DummyData[n][2]
      BreakTmp.append(str(DummyData[n][0]))
      #選んだジョブをlistから削除
      DummyData.pop(n)
      ReadOverHeadValue=ReadOverHead(sumMemory)
      WriteOverHeadValue=WriteOverHead(sumMemory)
      SumOverHead=ReadOverHeadValue+WriteOverHeadValue
      OnlyEtime=TotalTime(sumVE)
      TotalTimeValue=SumOverHead+OnlyEtime
      FinishTime=OnlyEtime+WriteOverHeadValue
      if(DataListNum==0):
        Bool=False
        BreakTmp[-1]=BreakTmp[-1]+"\n"
        BreakData.append(BreakTmp)
        Result.append([sumVE,TotalTimeValue,SumOverHead,OnlyEtime,FinishTime])
      if(DeadLine>=FinishTime):
        Bool=False
        BreakTmp[-1]=BreakTmp[-1]+"\n"
        BreakData.append(BreakTmp)
        Result.append([sumVE,TotalTimeValue,SumOverHead,OnlyEtime,FinishTime])
  return Result,BreakData
