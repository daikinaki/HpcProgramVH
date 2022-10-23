import copy

#DPの計算
def DP(N,W,DataList):
  dp = [[0]*(W+1) for i in range(N+1)] # DPの配列作成
  BreakDP=[[[]for j in range(W+1)] for i in range(N+1)]
  for i in range(N):
      for j in range(W+1):
        tmp_list=[]
        if (j < DataList[i][1]): # この時点では許容量を超えていないので選択しない
          dp[i+1][j] = dp[i][j] # ただ選択はしていないが、今回の情報をそのままi+1の方へ移す
          BreakDP[i+1][j] = BreakDP[i][j].copy()
        else:
          if(dp[i][j]!=0):
            #最小比較が出来る時
            if(dp[i][j-DataList[i][1]]!=0):
              dp[i+1][j] = min(dp[i][j], dp[i][j-DataList[i][1]]+DataList[i][2])
              if(dp[i][j]>dp[i][j-DataList[i][1]]+DataList[i][2]):
                tmp_list=BreakDP[i][j-DataList[i][1]].copy()
                tmp_list.append(DataList[i][0])
                BreakDP[i+1][j]=tmp_list.copy()
              else:
                BreakDP[i+1][j] = BreakDP[i][j].copy()
            elif(j==DataList[i][1]):
              dp[i+1][j] = min(dp[i][j], dp[i][j-DataList[i][1]]+DataList[i][2])
              if(dp[i][j]>dp[i][j-DataList[i][1]]+DataList[i][2]):
                tmp_list=BreakDP[i][j-DataList[i][1]].copy()
                tmp_list.append(DataList[i][0])
                BreakDP[i+1][j]=tmp_list.copy()
              else:
                BreakDP[i+1][j] = BreakDP[i][j].copy()
            else:
              dp[i+1][j] = dp[i][j]
              BreakDP[i+1][j] = BreakDP[i][j].copy()
          else:
            if(dp[i][j-DataList[i][1]]!=0):
              dp[i+1][j] = dp[i][j-DataList[i][1]]+DataList[i][2]
              tmp_list=BreakDP[i][j-DataList[i][1]].copy()
              tmp_list.append(DataList[i][0])
              BreakDP[i+1][j]=tmp_list.copy()
            elif(j==DataList[i][1]):
              dp[i+1][j] = dp[i][j-DataList[i][1]]+DataList[i][2]
              tmp_list=BreakDP[i][j-DataList[i][1]].copy()
              tmp_list.append(DataList[i][0])
              BreakDP[i+1][j]=tmp_list.copy()
            else:
              BreakDP[i+1][j] = BreakDP[i][j].copy()
  BreakDataProposed=BreakDP[N].copy()
  BreakDataProposed.pop(0)
  DPData=dp[N].copy()
  return BreakDataProposed,DPData

def ProposedAlgorithm(Result,DeadLineData,DPData,ReadOverHead,WriteOverHead,TotalTime,DeadLine,W):
  BreakBool=True
  #測定 iはVE数
  for i in range(1,W+1):
    ReadOverHeadValue=ReadOverHead(DPData[i])
    WriteOverHeadValue=WriteOverHead(DPData[i])
    SumOverHead=ReadOverHeadValue+WriteOverHeadValue
    OnlyEtime=TotalTime(i)
    TotalTimeValue=SumOverHead+OnlyEtime
    FinishTime=OnlyEtime+WriteOverHeadValue
    Result.append([i,TotalTimeValue,SumOverHead,OnlyEtime,FinishTime])
    if(BreakBool and FinishTime<=DeadLine):
      DeadLineData.extend([i,TotalTimeValue,SumOverHead,OnlyEtime,FinishTime])
      BreakBool=False
  return Result,DeadLineData