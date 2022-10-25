#初期値を記入
#待機幅(MB)
LocalRead=13000
LocalWrite=13000
RemoteRead=3000
RemoteWrite=7000
MaxVH=50

#測定によって変更する値
Tseq=7800
alpha=0.999999
DeadLine=650
#試行回数
TraialNumer=10
#1VHあたりの期待値となるメモリ使用量
ExpectedMemory=1024*10*8

#UrgentJobの発生回数
UrgentCount=2
#UrgentJobの発生頻度(何分に一回か)
UrgentJobStart=30
#ジョブの総時間
DatasetTotalTime=60*30*(UrgentCount+1)

#モデル化の関数
def LocalReadOverHead(memory):
  y=memory/LocalRead
  return y

def LocalWriteOverHead(memory):
  y=memory/LocalWrite
  return y

def RemoteReadOverHead(memory):
  y=memory/RemoteRead
  return y

def RemoteWriteOverHead(memory):
  y=memory/RemoteWrite
  return y

def TotalTime(VH):
  y=Tseq*(1-alpha)+(Tseq*alpha)/VH
  return y

