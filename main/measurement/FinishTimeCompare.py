import matplotlib.pyplot as plt

def FinishTimeCompare(name,ProposedResult,ExpectedResult,W):
  #データの用意
  Expected=[]
  Proposed=[]
  #データの変更
  for i in range(W):
    Proposed.append(ProposedResult[i][4])
    Expected.append(ExpectedResult[i][4])
  x=[i+1 for i in range(W)]
  plt.plot(x,Expected,label="FinishTime (ランダム時の期待値)")
  plt.plot(x,Proposed,label="FinishTime (提案手法)")
  plt.xlabel("VE")
  plt.ylabel("time(s)")
  plt.title(name+'Storage',fontname="MS Gothic")
  plt.legend(prop={"family":"MS Gothic"})
  plt.show()
