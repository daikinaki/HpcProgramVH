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

#値を上に挿入する用
def add_value_label(x_list,y_list):
    for i in range(1, len(x_list)+1):
        plt.text(i,y_list[i-1],y_list[i-1], ha="center")

#読み込み先
Default=[]
Expected=[]
Proposed=[]
#データ読み込み
DataRead("Default", Default)
DataRead("Expected", Expected)
DataRead("Proposed",Proposed)

label=["平常時","提案手法","ランダム手法の期待値"]
DefaultEndTime=CalEndTime(Default[-1][12])
ProposedEndTime=CalEndTime(Proposed[-1][12])
ExpectedEndTime=CalEndTime(Expected[-1][12])
left=[1,2,3]
value=[DefaultEndTime,ProposedEndTime,ExpectedEndTime]
plt.bar(left,value,color="blue", linewidth=1, align="center",tick_label=label,width=0.3)
plt.xticks(fontname="MS Gothic")
add_value_label(left,value)
plt.ylabel("メイクスパン (s)",fontname="MS Gothic")
plt.ylim(6000)
plt.show()