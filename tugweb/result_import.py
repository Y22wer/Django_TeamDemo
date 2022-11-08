"""
請把 results_v30.csv 該檔案 連同 本檔案放在根目錄~

請把 results_v40.csv 該檔案 連同 本檔案放在根目錄~

"""
import pandas as pd
#import models
import django, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tugweb.settings')
django.setup()
from mysite.models import Weight, Loss


csv_files=["results20.csv","results_v30.csv","results_v40.csv"]
#csv_files=["results_v30.csv","results_v40.csv"]
id_num=1
for file in csv_files:
    df=pd.read_csv(file)

    col_item=[]
    for i in df.columns:
        col_item.append(i)
    col_item=col_item[1:]

    c = Weight.objects.get(id=id_num)
    
    for i in range(0,len(df)):
        lossInstance=Loss()
        lossInstance.weight=c
        
        lossInstance.box_train_loss=df[col_item[0]][i]
        lossInstance.box_value_loss=df[col_item[1]][i]
        
        lossInstance.obj_train_loss=df[col_item[2]][i]
        lossInstance.obj_value_loss=df[col_item[3]][i]
        
        lossInstance.cls_train_loss=df[col_item[4]][i]
        lossInstance.cls_value_loss=df[col_item[5]][i]
        
        lossInstance.precision=df[col_item[6]][i]
        lossInstance.recall=df[col_item[7]][i]
        
        lossInstance.mAP_05=df[col_item[8]][i]
        lossInstance.mAP_05_095=df[col_item[9]][i]
        
        lossInstance.x_lr0=df[col_item[10]][i]
        lossInstance.x_lr1=df[col_item[11]][i]
        lossInstance.x_lr2=df[col_item[12]][i]
        
        lossInstance.save()
    id_num=id_num+1
        