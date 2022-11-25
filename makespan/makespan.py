from DataRead import DataRead
import matplotlib.pyplot as plt

# def CalEndTime(endTime):
#   endTime=endTime[11:]
#   endTimeList=list(map(int,endTime.split(":")))
#   Time=str(endTimeList[0]).zfill(2)+":"+str(endTimeList[1]).zfill(2)+":"+str(endTimeList[2]).zfill(2)
#   return Time
def CalEndTime(endTime):
  endTime=endTime[11:]
  endTimeList=list(map(int,endTime.split(":")))
  Time=endTimeList[0]*3600+endTimeList[1]*60+endTimeList[2]
  return Time

# def gragh(name,Default,Expected,Proposed):
#   # plt.plot(x,Default,'.',label="実行完了のジョブ個数 (平常時)")
#   plt.plot(x,Expected,label="実行完了のジョブ個数 (ランダム時の期待値)")
#   plt.plot(x,Proposed,label="実行完了のジョブ個数  (提案手法)")
#   plt.xlabel("時間 (m) ",fontname="MS Gothic")
#   plt.ylabel("実行完了のジョブ個数",fontname="MS Gothic")
#   plt.title(name+'Storage',fontname="MS Gothic")
#   plt.legend(prop={"family":"MS Gothic"})
#   plt.show()

#読み込み先
Default=[]
Expected=[]
Proposed=[]
#データ読み込み
DataRead("Default", Default)
DataRead("Expected", Expected)
DataRead("Proposed",Proposed)

print("Default")
DefaultEndTime=CalEndTime(Default[-1][12])
print(DefaultEndTime)
print("Proposed")
ProposedEndTime=CalEndTime(Proposed[-1][12])
print(ProposedEndTime)
print("Expected")
ExpectedEndTime=CalEndTime(Expected[-1][12])
print(ExpectedEndTime)
