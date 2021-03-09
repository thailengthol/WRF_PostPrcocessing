# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:06:47 2020

@author: Rajitha
"""
import csv
import pandas as pd
import numpy as np

data=pd.read_csv('wrf-para-1-dry-2017-rainc.csv', sep=',')
print(data.head())

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
rainc=data['RAINNC (mm)']
utc=data['TIME']

#number of days
days=int(len(column_a)/19)

#get timestamps
timestamps=[]
for x in range (days):
    timestamp=utc[19*x]
    timestamps.append(timestamp)

#get accumulation data
for x in range (days):
    Attapeu.append(rainc[0+(x*19)])
    Borkeo.append(rainc[1+(x*19)])
    Louangnumtha.append(rainc[2+(x*19)])
    Louangphabang.append(rainc[3+(x*19)])
    Mkham.append(rainc[4+(x*19)])
    Oudomxai.append(rainc[5+(x*19)])
    Pakse.append(rainc[6+(x*19)])
    Paksong.append(rainc[7+(x*19)])
    Paksan.append(rainc[8+(x*19)])
    Phonhong.append(rainc[9+(x*19)])
    Salavanh.append(rainc[10+(x*19)])
    Savannakhet.append(rainc[11+(x*19)])
    Sayabouli.append(rainc[12+(x*19)])
    Thakhek.append(rainc[13+(x*19)])
    Sekong.append(rainc[14+(x*19)])
    Phongsaly.append(rainc[15+(x*19)])
    Samnuea.append(rainc[16+(x*19)])
    Vientiane.append(rainc[17+(x*19)])
    Xiengkhouang.append(rainc[18+(x*19)])
 
#define variables for each station
rainc_daily_Attapeu=[]
rainc_daily_Borkeo=[]
rainc_daily_Louangnumtha=[]
rainc_daily_Louangphabang=[]
rainc_daily_Mkham=[]
rainc_daily_Oudomxai=[]
rainc_daily_Pakse=[]
rainc_daily_Paksong=[]
rainc_daily_Paksan=[]
rainc_daily_Phonhong=[]
rainc_daily_Salavanh=[]
rainc_daily_Savannakhet=[]
rainc_daily_Sayabouli=[]
rainc_daily_Thakhek=[]
rainc_daily_Sekong=[]
rainc_daily_Phongsaly=[]
rainc_daily_Samnuea=[]
rainc_daily_Vientiane=[]
rainc_daily_Xiengkhouang=[]


#calculate daily rainfall values for each station
for y in range (len(Attapeu)):
    if y==0:
        rainc_daily=(Attapeu[y])
        rainc_daily_Attapeu.append(rainc_daily)
    else:
        rainc_daily=(Attapeu[y]- Attapeu[y-1])
        rainc_daily_Attapeu.append(rainc_daily)

for y in range (len(Borkeo)):
    if y==0:
        rainc_daily=(Borkeo[y])
        rainc_daily_Borkeo.append(rainc_daily)
    else:
        rainc_daily=(Borkeo[y]- Borkeo[y-1])
        rainc_daily_Borkeo.append(rainc_daily)
        
for y in range (len(Louangnumtha)):
    if y==0:
        rainc_daily=(Louangnumtha[y])
        rainc_daily_Louangnumtha.append(rainc_daily)
    else:
        rainc_daily=(Louangnumtha[y]- Louangnumtha[y-1])
        rainc_daily_Louangnumtha.append(rainc_daily)
        
for y in range (len(Louangphabang)):
    if y==0:
        rainc_daily=(Louangphabang[y])
        rainc_daily_Louangphabang.append(rainc_daily)
    else:
        rainc_daily=(Louangphabang[y]- Louangphabang[y-1])
        rainc_daily_Louangphabang.append(rainc_daily)

for y in range (len(Mkham)):
    if y==0:
        rainc_daily=(Mkham[y])
        rainc_daily_Mkham.append(rainc_daily)
    else:
        rainc_daily=(Mkham[y]- Mkham[y-1])
        rainc_daily_Mkham.append(rainc_daily)
        
for y in range (len(Oudomxai)):
    if y==0:
        rainc_daily=(Oudomxai[y])
        rainc_daily_Oudomxai.append(rainc_daily)
    else:
        rainc_daily=(Oudomxai[y]- Oudomxai[y-1])
        rainc_daily_Oudomxai.append(rainc_daily)
 
for y in range (len(Pakse)):
    if y==0:
        rainc_daily=(Pakse[y])
        rainc_daily_Pakse.append(rainc_daily)
    else:
        rainc_daily=(Pakse[y]- Pakse[y-1])
        rainc_daily_Pakse.append(rainc_daily)

for y in range (len(Paksong)):
    if y==0:
        rainc_daily=(Paksong[y])
        rainc_daily_Paksong.append(rainc_daily)
    else:
        rainc_daily=(Paksong[y]- Paksong[y-1])
        rainc_daily_Paksong.append(rainc_daily)
        
for y in range (len(Paksan)):
    if y==0:
        rainc_daily=(Paksan[y])
        rainc_daily_Paksan.append(rainc_daily)
    else:
        rainc_daily=(Paksan[y]- Paksan[y-1])
        rainc_daily_Paksan.append(rainc_daily)
        
for y in range (len(Phonhong)):
    if y==0:
        rainc_daily=(Phonhong[y])
        rainc_daily_Phonhong.append(rainc_daily)
    else:
        rainc_daily=(Phonhong[y]- Phonhong[y-1])
        rainc_daily_Phonhong.append(rainc_daily)

for y in range (len(Salavanh)):
    if y==0:
        rainc_daily=(Salavanh[y])
        rainc_daily_Salavanh.append(rainc_daily)
    else:
        rainc_daily=(Salavanh[y]- Salavanh[y-1])
        rainc_daily_Salavanh.append(rainc_daily)
        
for y in range (len(Savannakhet)):
    if y==0:
        rainc_daily=(Savannakhet[y])
        rainc_daily_Savannakhet.append(rainc_daily)
    else:
        rainc_daily=(Savannakhet[y]- Oudomxai[y-1])
        rainc_daily_Savannakhet.append(rainc_daily)  
        
for y in range (len(Sayabouli)):
    if y==0:
        rainc_daily=(Sayabouli[y])
        rainc_daily_Sayabouli.append(rainc_daily)
    else:
        rainc_daily=(Sayabouli[y]- Sayabouli[y-1])
        rainc_daily_Sayabouli.append(rainc_daily)

for y in range (len(Thakhek)):
    if y==0:
        rainc_daily=(Thakhek[y])
        rainc_daily_Thakhek.append(rainc_daily)
    else:
        rainc_daily=(Thakhek[y]- Thakhek[y-1])
        rainc_daily_Thakhek.append(rainc_daily)
        
for y in range (len(Sekong)):
    if y==0:
        rainc_daily=(Sekong[y])
        rainc_daily_Sekong.append(rainc_daily)
    else:
        rainc_daily=(Sekong[y]- Sekong[y-1])
        rainc_daily_Sekong.append(rainc_daily)
        
for y in range (len(Phongsaly)):
    if y==0:
        rainc_daily=(Phongsaly[y])
        rainc_daily_Phongsaly.append(rainc_daily)
    else:
        rainc_daily=(Phongsaly[y]- Phongsaly[y-1])
        rainc_daily_Phongsaly.append(rainc_daily)

for y in range (len(Samnuea)):
    if y==0:
        rainc_daily=(Samnuea[y])
        rainc_daily_Samnuea.append(rainc_daily)
    else:
        rainc_daily=(Samnuea[y]- Samnuea[y-1])
        rainc_daily_Samnuea.append(rainc_daily)
        
for y in range (len(Vientiane)):
    if y==0:
        rainc_daily=(Vientiane[y])
        rainc_daily_Vientiane.append(rainc_daily)
    else:
        rainc_daily=(Vientiane[y]- Vientiane[y-1])
        rainc_daily_Vientiane.append(rainc_daily)
        
for y in range (len(Xiengkhouang)):
    if y==0:
        rainc_daily=(Xiengkhouang[y])
        rainc_daily_Xiengkhouang.append(rainc_daily)
    else:
        rainc_daily=(Xiengkhouang[y]- Xiengkhouang[y-1])
        rainc_daily_Xiengkhouang.append(rainc_daily)
        
#setup the final data frame to print csv
df=pd.DataFrame(list(zip(*[timestamps,rainc_daily_Attapeu,rainc_daily_Borkeo,rainc_daily_Louangnumtha,rainc_daily_Louangphabang,rainc_daily_Mkham,rainc_daily_Oudomxai,rainc_daily_Pakse,rainc_daily_Paksong,rainc_daily_Paksan,rainc_daily_Phonhong,rainc_daily_Salavanh,rainc_daily_Savannakhet,rainc_daily_Sayabouli,rainc_daily_Thakhek,rainc_daily_Sekong,rainc_daily_Phongsaly,rainc_daily_Samnuea,rainc_daily_Vientiane,rainc_daily_Xiengkhouang])),columns=['Date','Attapeu','Borkeo','Louangnumtha','Louangphabang','Mkham','Oudomxai','Pakse','Paksong','Paksan','Phonhong','Salavanh','Savannakhet','Sayabouli','Thakhek','Sekong','Phongsaly','Samnuea','Vientiane','Xiengkhouang'])
df.to_csv('wrf-para-1-dry-2017-rainc-allstations.csv')
print(df)
