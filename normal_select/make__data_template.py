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
extract_data=[]

def MakeDataBefore(MaxVH,MaxGB,etime,dummyMemory,Output):
  #VE数の管理
  RemainVH=MaxVH
  #1/3以上をVE=1に
  j=0
  while RemainVH>0:
    #VE数の確定
    if(j%3==0):
      VHNum=1
    elif(j%3==1):
      VHNum=1
    else:
      z=random.randint(1,8)
      if(RemainVH<8):
        VHNum=1
      else:
        VHNum=z
    RemainVH-=VHNum
    tmp_list=[]
    extractTmpList=[]
    for i in range(len(s[0])):
      #時刻を入力
      if(i==0 or i==9 or i==11 or i==12):
        tmp_list.append("2021/1/1 0:00:00")
      #job番号の記載
      elif(i==3):
        tmp_list.append(str(j+1))
      #que_name
      elif(i==4):
        tmp_list.append("normal")
      #elps_time
      elif(i==14):
        tmp_list.append(str(etime+50))
      #etime
      elif(i==15):
        tmp_list.append(str(etime))
      #njobs
      elif(i==17):
        njob=VHNum
        tmp_list.append(str(njob))
      #VE
      elif(i==19 or i==20):
        VENum=VHNum*8
        tmp_list.append(str(VENum))
      #cpunum_req
      elif(i==22):
        tmp_list.append(str(njob*2))
      #メモリ
      elif(i==35):
        #(MB)
        MB=random.randint(1,1024*MaxGB)
        MB*=VENum
        KB=1024*MB
        tmp_list.append(str(dummyMemory))
      #一番最後は改行にする
      elif(i==len(s[0])-1):
        tmp_list.append("?NULL?\n")
      #その他
      else:
        tmp_list.append("?NULL?")
    #Output
    extractTmpList.append(str(j+1))
    extractTmpList.append(str(VHNum))
    extractTmpList.append(str(MB)+"\n")
    j+=1
    data.append(tmp_list)
    Output.append(extractTmpList)
  return Output
# print(data)

#実行
#MakeDataBefore(MaxVH,MaxGB,etime,dummyMemory,Output):
MakeDataBefore(72,40,600,100,extract_data)


#保管ジョブの書き込み
with open('./main/data_template_before.csv', 'w') as file:
  writer = csv.writer(file, lineterminator='')
  writer.writerows(data)
with open('./main/extract_data.csv', 'w') as file:
  writer = csv.writer(file, lineterminator='')
  writer.writerows(extract_data)
print("make_data_template.csv成功")  
