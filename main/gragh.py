from measurement.DeadLineCompare import DeadLineCompare
from measurement.FinishTimeCompare import FinishTimeCompare
from measurement.ResouceTime import ResouceTime
import main
import make_Model as mM

#データ読み込み
RemoteExpectedResult=main.RemoteExpectedResult
RemoteExpectedDeadLine=main.RemoteExpectedDeadLine
LocalExpectedResult=main.LocalExpectedResult
LocalExpectedDeadLine=main.LocalExpectedDeadLine
RemoteRandomResult=main.RemoteRandomResult
LocalRandomResult=main.LocalRandomResult
RemoteProposedResult=main.RemoteProposedResult
RemoteProposedDeadLine=main.RemoteProposedDeadLine
LocalProposedResult=main.LocalProposedResult
LocalProposedDeadLine=main.LocalProposedDeadLine


# #DeadLineの比較
DeadLineCompare("Remote",RemoteProposedDeadLine,RemoteRandomResult,RemoteExpectedDeadLine,mM.TraialNumer)
DeadLineCompare("Local",LocalProposedDeadLine,LocalRandomResult,LocalExpectedDeadLine,mM.TraialNumer)

# #TotalTime
# FinishTimeCompare("Remote",RemoteProposedResult,RemoteExpectedResult,mM.MaxVE)
# FinishTimeCompare("Local",LocalProposedResult,LocalExpectedResult,mM.MaxVE)
# #ResouceTime
# ResouceTime("Remote",RemoteProposedResult,RemoteExpectedResult,mM.MaxVE)
# ResouceTime("Local",LocalProposedResult,LocalExpectedResult,mM.MaxVE)