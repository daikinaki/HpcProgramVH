from algorithm.AlgorithmMinimum  import DP,ProposedAlgorithm 
from algorithm.AlgorithmRandom import RandomAlgorithm
from algorithm.AlgorithmExpectedValue import ExpectedValue
import make_Model as mM
import make_DataList as mD

DataList=mD.DataList
jobcomp_before=mD.jobcomp_before
endTime=jobcomp_before[-1][12]
endTime=endTime[11:]
endTimeList=list(map(int,endTime.split(":")))
endTime=3600*endTimeList[0]+60*endTimeList[1]+endTimeList[2]-mM.DeadLine
N=len(DataList)
W=mM.MaxVH


#DP作成
BreakDataProposed,DPData=DP(N,W,DataList)
# print(BreakDataProposed)

#提案手法の結果
RemoteProposedResult=[]
RemoteProposedDeadLine=[]
# LocalProposedResult=[]
# LocalProposedDeadLine=[]
#提案手法実行
ProposedAlgorithm(RemoteProposedResult,RemoteProposedDeadLine,DPData,mM.RemoteReadOverHead,mM.RemoteWriteOverHead,mM.TotalTime,mM.DeadLine,W)
# ProposedAlgorithm(LocalProposedResult,LocalProposedDeadLine,DPData,mM.LocalReadOverHead,mM.LocalWriteOverHead,mM.TotalTime,mM.DeadLine,W)

#ランダムの結果
RemoteRandomResult=[]
RemoteRandomBreakData=[]
# LocalRandomResult=[]
# LocalRandomBreakData=[]
#ランダム実行
RandomAlgorithm(RemoteRandomResult,RemoteRandomBreakData,mM.TraialNumer,DataList,mM.RemoteReadOverHead,mM.RemoteWriteOverHead,mM.TotalTime,mM.DeadLine)
# RandomAlgorithm(LocalRandomResult,LocalRandomBreakData,mM.TraialNumer,DataList,mM.LocalReadOverHead,mM.LocalWriteOverHead,mM.TotalTime,mM.DeadLine)

#期待値の結果
RemoteExpectedResult=[]
RemoteExpectedDeadLine=[]
# LocalExpectedResult=[]
# LocalExpectedDeadLine=[]
#期待値実行
ExpectedValue(RemoteExpectedResult,RemoteExpectedDeadLine,mM.ExpectedMemory,mM.RemoteReadOverHead,mM.RemoteWriteOverHead,mM.TotalTime,mM.DeadLine,W)
# ExpectedValue(LocalExpectedResult,LocalExpectedDeadLine,mM.ExpectedMemory,mM.LocalReadOverHead,mM.LocalWriteOverHead,mM.TotalTime,mM.DeadLine,W)

