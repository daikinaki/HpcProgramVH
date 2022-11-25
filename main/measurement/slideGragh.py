import matplotlib.pyplot as plt
def slideGragh(name,ProposedResult,W):
  #データの用意
  ExecuteTime=[]
  ResouceTime=[]
  #データの変更
  for i in range(W):
    ExecuteTime.append(ProposedResult[i][3])
    ResouceTime.append(ProposedResult[i][2])
  x=[i+1 for i in range(W)]
  plt.plot(x,ExecuteTime)
  plt.xlabel("並列数",fontname="MS Gothic")
  plt.ylabel("実行時間",fontname="MS Gothic")
  # plt.title(name+'Storage',fontname="MS Gothic")
  plt.rcParams["font.size"] = 18
  plt.tight_layout()
  plt.show()
  plt.plot(x,ResouceTime)
  plt.xlabel("並列数",fontname="MS Gothic")
  plt.ylabel("中断と再開に要する時間",fontname="MS Gothic")
  # plt.title(name+'Storage',fontname="MS Gothic")
  plt.rcParams["font.size"] = 18
  plt.tight_layout()
  plt.show()