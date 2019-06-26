import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt
import math
import random
import matplotlib
scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials=ServiceAccountCredentials.from_json_keyfile_name('SampleSpreadSheets-89b6e7e56503.json',scope)
gc=gspread.authorize(credentials)
wks=gc.open('sample').sheet1
players=['RG Sharma','S Dhawan','V Kohli','SK Raina','MS Dhoni (c) †','RA Jadeja','AM Rahane','R Ashwin','Mohammed Shami','UT Yadav','MM Sharma']
val=[]
for i in players:
    sum=0
    cells=wks.findall(i)
    for j in cells:
        sum=sum+int(wks.cell(j.row,j.col+1).value)
    if(j!=0):
       sum=math.floor(sum/len(cells))
    else:
       sum=-1
    val.append(sum)
plt.figure(figsize=(20, 3))

plt.bar(players,val,align='edge',width=0.3,color=['black', 'red', 'green', 'blue', 'cyan','orange','deepskyblue','brown','darkgreen','deeppink','coral'])
plt.savefig('/home/ib_admin/sample2.png')

print(val)