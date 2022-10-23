#初期値を記入
#待機幅(MB)
LocalRead=13000
LocalWrite=13000
RemoteRead=8000
RemoteWrite=3000
MaxVE=120

#測定によって変更する値
Tseq=7800
alpha=0.9999
DeadLine=800
#試行回数
TraialNumer=10
CopyNumber=5
#UrgentJobの発生時間
StartUrgentJob=500
ExpectedMemory=1024*40

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

def TotalTime(VE):
  y=Tseq*(1-alpha)+(Tseq*alpha)/VE
  return y

