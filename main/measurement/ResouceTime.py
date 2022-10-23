import matplotlib.pyplot as plt
def ResouceTime(name,ProposedResult,ExpectedResult,W):
  #データの用意
  Expected=[]
  Proposed=[]
  #データの変更
  for i in range(W):
    Proposed.append(ProposedResult[i][1]*(i+1))
    Expected.append(ExpectedResult[i][1]*(i+1))
  x=[i+1 for i in range(W)]
  plt.plot(x,Expected,label="ResouceTime (ランダム時の期待値)")
  plt.plot(x,Proposed,label="ResouceTime (提案手法)")
  plt.xlabel("VE")
  plt.ylabel("time(s)")
  plt.title(name+'Storage',fontname="MS Gothic")
  plt.legend(prop={"family":"MS Gothic"})
  plt.show()