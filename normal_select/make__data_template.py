import csv
import copy
import random
#元データ読み込み
with open("./normal_select/data_model.csv","r")as f:
  #２次元配列化
  line = f.readlines()
  s=[]
  for tmp in line:
    s.append(tmp.split(','))
#1番上を作る
top=s[0]
#data
data=[]
data.append(top)

#[jobnum,Ve,memory]のリスト作成
extractData=[]

#VE数の管理
RemainVE=8*72
#1/3以上をVE=1に
j=0
while RemainVE>0:
  #VE数の確定
  if(j%3==0):
    VENum=1
  elif(j%3==1):
    z=random.randint(1,8)
    VENum=z
    if(RemainVE<z):
      VENum=1
  else:
    z=random.randint(1,5)
    if(RemainVE<8):
      VENum=1
    elif(RemainVE<8*z):
      VENum=8
    else:
      VENum=8*z
  RemainVE-=VENum
  tmp_list=[]
  extractTmpList=[]
  for i in range(len(s[0])):
    #時刻を入力
    if(i==0 or i==9 or i==11 or i==12):
      tmp_list.append("2021/1/1 0:00:45")
    #job番号の記載
    elif(i==3):
      tmp_list.append(str(j+1))
    #que_name
    elif(i==4):
      tmp_list.append("normal")
    #elps_time
    elif(i==14):
      tmp_list.append("1100")
    #etime
    elif(i==15):
      tmp_list.append("1000")
    #njobs
    elif(i==17):
      if(VENum%8==0):
        njob=VENum//8
      else:
        njob=VENum//8+1
      tmp_list.append(str(njob))
    #VE
    elif(i==19 or i==20):
      tmp_list.append(str(VENum))
    #cpunum_req
    elif(i==22):
      tmp_list.append(str(njob*2))
    #メモリ
    elif(i==35):
      #(MB)
      MB=random.randint(1,1024*80)
      MB*=VENum
      KB=1024*MB
      tmp_list.append(str(1024))
    #一番最後は改行にする
    elif(i==len(s[0])-1):
      tmp_list.append("?NULL?\n")
    #その他
    else:
      tmp_list.append("?NULL?")
  #extractData
  extractTmpList.append(str(j+1))
  extractTmpList.append(str(VENum))
  extractTmpList.append(str(MB)+"\n")
  j+=1
  data.append(tmp_list)
  extractData.append(extractTmpList)

# print(data)


#保管ジョブの書き込み
with open('./main/data_template_before.csv', 'w') as file:
  writer = csv.writer(file, lineterminator='')
  writer.writerows(data)
with open('./main/extract_data.csv', 'w') as file:
  writer = csv.writer(file, lineterminator='')
  writer.writerows(extractData)
print("make_data_template.csv成功")  
