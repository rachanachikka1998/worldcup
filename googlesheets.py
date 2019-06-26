import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.support.select import Select
import datetime

scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials=ServiceAccountCredentials.from_json_keyfile_name('SampleSpreadSheets-89b6e7e56503.json',scope)
gc=gspread.authorize(credentials)
wks=gc.open('sample').sheet1
driver = webdriver.Firefox()
x1=datetime.datetime.now()
driver.get("http://www.espncricinfo.com/icc-cricket-world-cup-2015/content/series/509587.html?template=fixtures")
x2=datetime.datetime.now()
elem= Select(driver.find_element_by_xpath('//*[@id="team"]'))
elem.select_by_visible_text("India")
match = driver.find_elements_by_partial_link_text("India")
sum=x2-x1
for j in range(len(match)):
    elem = Select(driver.find_element_by_xpath('//*[@id="team"]'))
    elem.select_by_visible_text("India")
    match = driver.find_elements_by_partial_link_text("India")
    x1 = datetime.datetime.now()
    match[j].click()
    x2 = datetime.datetime.now()
    scores= driver.find_elements_by_class_name("scorecard-section.batsmen")
    names = driver.find_elements_by_class_name("gp__cricket__gameHeader")
    n1=""
    for i in names:
        n1=n1+i.text
    n1=n1.split("\n")
    print(n1)
    s=scores[0].text
    print(s)
    s=s.split("\n")
    string=n1[2]+" vs "+n1[4]
    d=[]
    d.append(string)
    d.append("RESPONSE TIME=" + str(x2 - x1))
    wks.append_row(d)
    d=[]
    d.append(n1[2])
    d.append(n1[3])
    wks.append_row(d)
    for i in range(7,len(s)-6,8):
        l=[]
        l.append(s[i])
        l.append(s[i+2])
        wks.append_row(l)


    s=scores[1].text
    s = s.split("\n")
    d = []
    d.append(n1[4])
    d.append(n1[5])
    wks.append_row(d)
    for i in range(7, len(s) - 6, 8):
        l = []
        l.append(s[i])
        l.append(s[i + 2])
        wks.append_row(l)
    print(d)
    sum=sum+x2-x1
    driver.execute_script("window.history.go(-1)")
    driver.refresh()
d=[]
denom=len(match)+1
i=sum/denom
d.append("AVERAGE RESPONSE TIME")
d.append(str(i))
wks.append_row(d)
#print("AVERAGE RESPONSE TIME:", sum/(len(match)+1))


