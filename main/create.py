import csv
from CreateDataTemplate.DataTemplate import WriteDataTemplate
import main
import make_Model as mM
import make_DataList as mD

#データの読み込み
DataList=mD.DataList
endTime=main.endTime
jobcomp_before=mD.jobcomp_before
data_before=mD.data_before
BreakDataProposed=main.BreakDataProposed
RemoteProposedDeadLine=main.RemoteProposedDeadLine
# LocalProposedDeadLine=main.LocalProposedDeadLine
RemoteExpectedDeadLine=main.RemoteExpectedDeadLine
# LocalExpectedDeadLine=main.LocalExpectedDeadLine


#結果
RemoteProposedDatatemplate=[]
# LocalProposedDatatemplate=[]
RemoteExpectedDatatemplate=[]
# LocalExpectedDatatemplate=[]
DefaultDataTemplate=[]

def WriteData(data,name):
  #書き込み
  with open('./main/Dataset/'+name+'.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='')
    writer.writerows(data)

#実行
RemoteProposedDatatemplate,RemoteExpectedDatatemplate,DefaultDataTemplate=WriteDataTemplate(RemoteProposedDeadLine,RemoteExpectedDeadLine,data_before,mM.DatasetTotalTime,mM.DeadLine,mM.UrgentCount,mM.UrgentJobStart)
#書き込み
WriteData(RemoteProposedDatatemplate,"RemoteProposedDatatemplate")
WriteData(RemoteExpectedDatatemplate,"RemoteExpectedDatatemplate")
WriteData(DefaultDataTemplate,"DefaultDataTemplate")