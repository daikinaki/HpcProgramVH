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
  plt.plot(x,Expected,label="ランダム選択手法の期待値")
  plt.plot(x,Proposed,label="提案手法")
  plt.xlabel("VH数",fontname="MS Gothic")
  plt.ylabel("$T_{\mathrm{finish}}$ (s)")
  # plt.title(name+'Storage',fontname="MS Gothic")
  plt.legend(prop={"family":"MS Gothic"})
  plt.yscale('log')
  plt.show()
