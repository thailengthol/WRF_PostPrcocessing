# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:23:18 2020

@author: Thaileng_GIC
"""

#import csv
import pandas as pd
#import numpy as np

season = ['-dry-2017', '-wet-2017', '-dry-2018', '-wet-2018']

for b in season: 
    for a in range (1,2):
        data1=pd.read_csv('../Extract_CSV/Parameterization Results/wrf-para-'+str(a)+'/wrf-para-'+str(a)+str(b)+'-rainc.csv', sep=',')
        data2=pd.read_csv('../Extract_CSV/Parameterization Results/wrf-para-'+str(a)+'/wrf-para-'+str(a)+str(b)+'-rainnc.csv', sep=',')
        #print(data2.head())
        
        #stations
        Attapeu=[]
        Borkeo=[]
        Louangnumtha=[]
        Louangphabang=[]
        Mkham=[]
        Oudomxai=[]
        Pakse=[]
        Paksong=[]
        Paksan=[]
        Phonhong=[]
        Salavanh=[]
        Savannakhet=[]
        Sayabouli=[]
        Thakhek=[]
        Sekong=[]
        Phongsaly=[]
        Samnuea=[]
        Vientiane=[]
        Xiengkhouang=[]
        
        #rainfall
        rainc=data1['RAINNC (mm)']
        rainnc=data2['RAINNC (mm)']
        rainfall = data1['RAINNC (mm)'] + data2['RAINNC (mm)']
        utc=data1['TIME']
        
        #number of days
        days=int(len(utc)/19)
        
        #get timestamps
        timestamps=[]
        for x in range (days):
            timestamp=utc[19*x]
            timestamps.append(timestamp)
            
        #get accumulation data
        for x in range (days):
            Attapeu.append(rainfall[0+(x*19)])
            Borkeo.append(rainfall[1+(x*19)])
            Louangnumtha.append(rainfall[2+(x*19)])
            Louangphabang.append(rainfall[3+(x*19)])
            Mkham.append(rainfall[4+(x*19)])
            Oudomxai.append(rainfall[5+(x*19)])
            Pakse.append(rainfall[6+(x*19)])
            Paksong.append(rainfall[7+(x*19)])
            Paksan.append(rainfall[8+(x*19)])
            Phonhong.append(rainfall[9+(x*19)])
            Salavanh.append(rainfall[10+(x*19)])
            Savannakhet.append(rainfall[11+(x*19)])
            Sayabouli.append(rainfall[12+(x*19)])
            Thakhek.append(rainfall[13+(x*19)])
            Sekong.append(rainfall[14+(x*19)])
            Phongsaly.append(rainfall[15+(x*19)])
            Samnuea.append(rainfall[16+(x*19)])
            Vientiane.append(rainfall[17+(x*19)])
            Xiengkhouang.append(rainfall[18+(x*19)])
        
        #define variables for each station
        rainfall_daily_Attapeu=[]
        rainfall_daily_Borkeo=[]
        rainfall_daily_Louangnumtha=[]
        rainfall_daily_Louangphabang=[]
        rainfall_daily_Mkham=[]
        rainfall_daily_Oudomxai=[]
        rainfall_daily_Pakse=[]
        rainfall_daily_Paksong=[]
        rainfall_daily_Paksan=[]
        rainfall_daily_Phonhong=[]
        rainfall_daily_Salavanh=[]
        rainfall_daily_Savannakhet=[]
        rainfall_daily_Sayabouli=[]
        rainfall_daily_Thakhek=[]
        rainfall_daily_Sekong=[]
        rainfall_daily_Phongsaly=[]
        rainfall_daily_Samnuea=[]
        rainfall_daily_Vientiane=[]
        rainfall_daily_Xiengkhouang=[]
    
        #calculate daily rainfall values for each station
        for y in range (len(Attapeu)):
            if y==0:
                rainfall_daily=(Attapeu[y])
                rainfall_daily_Attapeu.append(rainfall_daily)
            else:
                rainfall_daily=(Attapeu[y]- Attapeu[y-1])
                rainfall_daily_Attapeu.append(rainfall_daily)
        
        for y in range (len(Borkeo)):
            if y==0:
                rainfall_daily=(Borkeo[y])
                rainfall_daily_Borkeo.append(rainfall_daily)
            else:
                rainfall_daily=(Borkeo[y]- Borkeo[y-1])
                rainfall_daily_Borkeo.append(rainfall_daily)
                
        for y in range (len(Louangnumtha)):
            if y==0:
                rainfall_daily=(Louangnumtha[y])
                rainfall_daily_Louangnumtha.append(rainfall_daily)
            else:
                rainfall_daily=(Louangnumtha[y]- Louangnumtha[y-1])
                rainfall_daily_Louangnumtha.append(rainfall_daily)
                
        for y in range (len(Louangphabang)):
            if y==0:
                rainfall_daily=(Louangphabang[y])
                rainfall_daily_Louangphabang.append(rainfall_daily)
            else:
                rainfall_daily=(Louangphabang[y]- Louangphabang[y-1])
                rainfall_daily_Louangphabang.append(rainfall_daily)
        
        for y in range (len(Mkham)):
            if y==0:
                rainfall_daily=(Mkham[y])
                rainfall_daily_Mkham.append(rainfall_daily)
            else:
                rainfall_daily=(Mkham[y]- Mkham[y-1])
                rainfall_daily_Mkham.append(rainfall_daily)
                
        for y in range (len(Oudomxai)):
            if y==0:
                rainfall_daily=(Oudomxai[y])
                rainfall_daily_Oudomxai.append(rainfall_daily)
            else:
                rainfall_daily=(Oudomxai[y]- Oudomxai[y-1])
                rainfall_daily_Oudomxai.append(rainfall_daily)
         
        for y in range (len(Pakse)):
            if y==0:
                rainfall_daily=(Pakse[y])
                rainfall_daily_Pakse.append(rainfall_daily)
            else:
                rainfall_daily=(Pakse[y]- Pakse[y-1])
                rainfall_daily_Pakse.append(rainfall_daily)
        
        for y in range (len(Paksong)):
            if y==0:
                rainfall_daily=(Paksong[y])
                rainfall_daily_Paksong.append(rainfall_daily)
            else:
                rainfall_daily=(Paksong[y]- Paksong[y-1])
                rainfall_daily_Paksong.append(rainfall_daily)
                
        for y in range (len(Paksan)):
            if y==0:
                rainfall_daily=(Paksan[y])
                rainfall_daily_Paksan.append(rainfall_daily)
            else:
                rainfall_daily=(Paksan[y]- Paksan[y-1])
                rainfall_daily_Paksan.append(rainfall_daily)
                
        for y in range (len(Phonhong)):
            if y==0:
                rainfall_daily=(Phonhong[y])
                rainfall_daily_Phonhong.append(rainfall_daily)
            else:
                rainfall_daily=(Phonhong[y]- Phonhong[y-1])
                rainfall_daily_Phonhong.append(rainfall_daily)
        
        for y in range (len(Salavanh)):
            if y==0:
                rainfall_daily=(Salavanh[y])
                rainfall_daily_Salavanh.append(rainfall_daily)
            else:
                rainfall_daily=(Salavanh[y]- Salavanh[y-1])
                rainfall_daily_Salavanh.append(rainfall_daily)
                
        for y in range (len(Savannakhet)):
            if y==0:
                rainfall_daily=(Savannakhet[y])
                rainfall_daily_Savannakhet.append(rainfall_daily)
            else:
                rainfall_daily=(Savannakhet[y]- Savannakhet[y-1])
                rainfall_daily_Savannakhet.append(rainfall_daily)  
                
        for y in range (len(Sayabouli)):
            if y==0:
                rainfall_daily=(Sayabouli[y])
                rainfall_daily_Sayabouli.append(rainfall_daily)
            else:
                rainfall_daily=(Sayabouli[y]- Sayabouli[y-1])
                rainfall_daily_Sayabouli.append(rainfall_daily)
        
        for y in range (len(Thakhek)):
            if y==0:
                rainfall_daily=(Thakhek[y])
                rainfall_daily_Thakhek.append(rainfall_daily)
            else:
                rainfall_daily=(Thakhek[y]- Thakhek[y-1])
                rainfall_daily_Thakhek.append(rainfall_daily)
                
        for y in range (len(Sekong)):
            if y==0:
                rainfall_daily=(Sekong[y])
                rainfall_daily_Sekong.append(rainfall_daily)
            else:
                rainfall_daily=(Sekong[y]- Sekong[y-1])
                rainfall_daily_Sekong.append(rainfall_daily)
                
        for y in range (len(Phongsaly)):
            if y==0:
                rainfall_daily=(Phongsaly[y])
                rainfall_daily_Phongsaly.append(rainfall_daily)
            else:
                rainfall_daily=(Phongsaly[y]- Phongsaly[y-1])
                rainfall_daily_Phongsaly.append(rainfall_daily)
        
        for y in range (len(Samnuea)):
            if y==0:
                rainfall_daily=(Samnuea[y])
                rainfall_daily_Samnuea.append(rainfall_daily)
            else:
                rainfall_daily=(Samnuea[y]- Samnuea[y-1])
                rainfall_daily_Samnuea.append(rainfall_daily)
                
        for y in range (len(Vientiane)):
            if y==0:
                rainfall_daily=(Vientiane[y])
                rainfall_daily_Vientiane.append(rainfall_daily)
            else:
                rainfall_daily=(Vientiane[y]- Vientiane[y-1])
                rainfall_daily_Vientiane.append(rainfall_daily)
                
        for y in range (len(Xiengkhouang)):
            if y==0:
                rainfall_daily=(Xiengkhouang[y])
                rainfall_daily_Xiengkhouang.append(rainfall_daily)
            else:
                rainfall_daily=(Xiengkhouang[y]- Xiengkhouang[y-1])
                rainfall_daily_Xiengkhouang.append(rainfall_daily)
        
         #setup the final data frame to print csv
        df=pd.DataFrame(list(zip(*[timestamps,rainfall_daily_Attapeu,rainfall_daily_Borkeo,rainfall_daily_Louangnumtha,rainfall_daily_Louangphabang,rainfall_daily_Mkham,rainfall_daily_Oudomxai,rainfall_daily_Pakse,rainfall_daily_Paksong,rainfall_daily_Paksan,rainfall_daily_Phonhong,rainfall_daily_Salavanh,rainfall_daily_Savannakhet,rainfall_daily_Sayabouli,rainfall_daily_Thakhek,rainfall_daily_Sekong,rainfall_daily_Phongsaly,rainfall_daily_Samnuea,rainfall_daily_Vientiane,rainfall_daily_Xiengkhouang])),columns=['Date','Attapeu','Borkeo','Louangnumtha','Louangphabang','Mkham','Oudomxai','Pakse','Paksong','Paksan','Phonhong','Salavanh','Savannakhet','Sayabouli','Thakhek','Sekong','Phongsaly','Samnuea','Vientiane','Xiengkhouang'])
        #df.to_csv('../Extract_CSV/wrf_para_'+str(a)+str(b)+'.csv')
        
    station = ['Attapeu','Borkeo','Louangnumtha','Louangphabang','Mkham','Oudomxai','Pakse','Paksong','Paksan','Phonhong','Salavanh','Savannakhet','Sayabouli','Thakhek','Sekong','Phongsaly','Samnuea','Vientiane','Xiengkhouang']
    for st in station:
        df.append(df[st])
    dfs = ['Attapeu':df['Attapeu'],'Borkeo':df'Borkeo'omxai','Pakse','Paksong','Paksan','Phonhong','Salavanh','Savannakhet','Sayabouli','Thakhek','Sekong','Phongsaly','Samnuea','Vientiane','Xiengkhouang']
    
        
        
        
