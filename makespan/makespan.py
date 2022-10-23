from DataRead import DataRead
import matplotlib.pyplot as plt
def CalEndTime(endTime):
  endTime=endTime[11:]
  endTimeList=list(map(int,endTime.split(":")))
  Time=3600*endTimeList[0]+60*endTimeList[1]+endTimeList[2]
  return Time

#時刻あたりの個数
def CountJob(Input):
  result=[]
  count=0
  i=1
  for t in range(1,60*70):  
    Bool=True
    if(len(Input)-1==i):
      result.append(count)
    else:
      for j in range(i,len(Input)):
        Time=CalEndTime(Input[j][12])
        if(Time>t):
          result.append(count)
          i=j
          Bool=False
          break
        else:
          if(Input[j][3]!="urgent"):
            count+=1
      if(Bool):
        result.append(count)
        i=j
  return result

# #個数あたりの時刻
# def CountJob(Input):
#   result=[]
#   count=0
#   for j in range(1,len(Input)):
#       Time=CalEndTime(Input[j][12])
#       if(Input[j][3]!="urgent"):
#         count+=1
#         result.append(Time)
#   return result



def gragh(name,Default,Expected,Proposed):
  x=[i+1 for i in range(len(Default))]
  # plt.plot(x,Default,'.',label="実行完了のジョブ個数 (平常時)")
  plt.plot(x,Expected,label="実行完了のジョブ個数 (ランダム時の期待値)")
  plt.plot(x,Proposed,label="実行完了のジョブ個数  (提案手法)")
  plt.xlabel("時間 (m) ",fontname="MS Gothic")
  plt.ylabel("実行完了のジョブ個数",fontname="MS Gothic")
  plt.title(name+'Storage',fontname="MS Gothic")
  plt.legend(prop={"family":"MS Gothic"})
  plt.show()


#読み込み先
default=[]
ExpectedRemote=[]
ExpectedLocal=[]
ProposedRemote=[]
ProposedLocal=[]
#データ読み込み
DataRead("default", default)
DataRead("ExpectedRemote", ExpectedRemote)
DataRead("ExpectedLocal",ExpectedLocal)
DataRead("ProposedRemote",ProposedRemote)
DataRead("ProposedLocal",ProposedLocal)
#結果用用
defaultResult= CountJob(default)
ExpectedRemoteResult=CountJob(ExpectedRemote)
ExpectedLocalResult=CountJob(ExpectedLocal)
ProposedRemoteResult=CountJob(ProposedRemote)
ProposedLocalResult=CountJob(ProposedLocal)
#結果
gragh("Remote", defaultResult, ExpectedRemoteResult, ProposedRemoteResult)
gragh("Local", defaultResult, ExpectedLocalResult, ProposedLocalResult)
