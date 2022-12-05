import random
import copy

def ExpectedValue(Result,DeadLineData,ExpectedMemory,ReadOverHead,WriteOverHead,TotalTime,DeadLine,W):
  BreakBool=True
  for i in range(1,W+1):
    ReadOverHeadValue=ReadOverHead(ExpectedMemory*i)
    WriteOverHeadValue=WriteOverHead(ExpectedMemory*i)
    SumOverHead=ReadOverHeadValue+WriteOverHeadValue
    OnlyEtime=TotalTime(i)
    TotalTimeValue=SumOverHead+OnlyEtime
    FinishTime=OnlyEtime+WriteOverHeadValue
    Result.append([i,TotalTimeValue,SumOverHead,OnlyEtime,FinishTime])
    if(BreakBool and FinishTime<=DeadLine):
      DeadLineData.extend([i,TotalTimeValue,SumOverHead,OnlyEtime,FinishTime])
      BreakBool=False
  if(len(DeadLineData)==0):
    tmp=copy.deepcopy(Result)
    tmp=sorted(tmp, key=lambda x: x[4])
    DeadLineData.extend(tmp[0])
  return Result,DeadLineData



