import gspread
from oauth2client.service_account import ServiceAccountCredentials
import matplotlib.pyplot as plt
import matplotlib
scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials=ServiceAccountCredentials.from_json_keyfile_name('SampleSpreadSheets-89b6e7e56503.json',scope)
gc=gspread.authorize(credentials)
wks=gc.open('sample').sheet1
cells=wks.findall("India")
l=[]
# matplotlib.use('tkAgg')
for cell in cells:
    string=wks.cell(cell.row,cell.col+1).value
    arr=string.split(" ")
    if len(arr)==1:
        a=arr[0].split("/")
        l.append(int(a[0]))
l1=[]
for i in range(len(l)):
    l1.append("match-"+str(i+1))
plt.plot(l1,l)
plt.savefig('/home/ib_admin/sample.png')
print(l)
print(l1)