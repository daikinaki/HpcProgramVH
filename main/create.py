import csv
from CreateDataTemplate.DataTemplate import WriteDataTemplate,DefaultWriteDataTemplate
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
LocalProposedDeadLine=main.LocalProposedDeadLine
RemoteExpectedDeadLine=main.RemoteExpectedDeadLine
LocalExpectedDeadLine=main.LocalExpectedDeadLine


#結果
RemoteProposedDatatemplate=[]
LocalProposedDatatemplate=[]
RemoteExpectedDatatemplate=[]
LocalExpectedDatatemplate=[]
DefaultDataTemplate=[]

def WriteData(data,name):
  #書き込み
  with open('./Dataset/'+name+'.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='')
    writer.writerows(data)

#実行
WriteDataTemplate("提案手法 (Remote)",RemoteProposedDeadLine,BreakDataProposed,RemoteProposedDatatemplate,endTime,data_before,jobcomp_before,mM.StartUrgentJob,mM.DeadLine,mM.CopyNumber)
WriteData(RemoteProposedDatatemplate,"RemoteProposedDatatemplate")
WriteDataTemplate("提案手法 (Local)",LocalProposedDeadLine,BreakDataProposed,LocalProposedDatatemplate,endTime,data_before,jobcomp_before,mM.StartUrgentJob,mM.DeadLine,mM.CopyNumber)
WriteData(LocalProposedDatatemplate,"LocalProposedDatatemplate")
WriteDataTemplate("期待値 (Remote)",RemoteExpectedDeadLine,BreakDataProposed,RemoteExpectedDatatemplate,endTime,data_before,jobcomp_before,mM.StartUrgentJob,mM.DeadLine,mM.CopyNumber)
WriteData(RemoteExpectedDatatemplate,"RemoteExpectedDatatemplate")
WriteDataTemplate("期待値 (Local)",LocalExpectedDeadLine,BreakDataProposed,LocalExpectedDatatemplate,endTime,data_before,jobcomp_before,mM.StartUrgentJob,mM.DeadLine,mM.CopyNumber)
WriteData(LocalExpectedDatatemplate,"LocalExpectedDatatemplate")
DefaultWriteDataTemplate(DefaultDataTemplate, endTime, data_before, jobcomp_before, mM.StartUrgentJob, mM.CopyNumber)
WriteData(DefaultDataTemplate,"DefaultDataTemplate")