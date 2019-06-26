from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json
#opts = Options()
#opts.set_headless()
#assert opts.headless  # Operating in headless mode

driver = webdriver.Firefox()
driver.get("http://www.espncricinfo.com/icc-cricket-world-cup-2015/content/series/509587.html?template=fixtures")
elem= Select(driver.find_element_by_xpath('//*[@id="team"]'))
elem.select_by_visible_text("India")
match=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[4]/div/div[1]/div[3]/ul/li[4]/div[2]/span[1]/a")
#print(match)
wait = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div[4]/div/div[1]/div[3]/ul/li[4]/div[2]/span[1]/a"))
    )
#element = wait.until(EC.element_to_be_clickable())
match.click()
e=driver.find_element_by_xpath("/html/body/div[6]/section/div/section/section/div/div[3]/div[1]/div[1]/div[2]/nav/div/ul/li[1]")
e.click()
scores=driver.find_element_by_xpath("/html/body/div[6]/section/div/section/section/div/div[3]/div[1]/div[3]/div/div[2]/article[1]")
s=scores.text
#print(s)
s=s.split("\n")
team1_batsmen=[]
team2_batsmen=[]
team1_bowlers=[]
team2_bowlers=[]
top_bat_team1={}
top_bowl_team1={}
top_bat_team2={}
top_bowl_team2={}
for i in range(2,5,2):
    top_bat_team1["player_name"]=s[i]
    top_bat_team1["score"]=s[i+1]
    team1_batsmen.append(top_bat_team1)
    top_bat_team1={}
for i in range(6,9,2):
    top_bowl_team1["player_name"]=s[i]
    temp=s[i+1].split("/")
    top_bowl_team1["wickets"]=temp[0]
    temp=temp[1].split(" ")
    top_bowl_team1["runs_conceded"]=temp[0]
    team1_bowlers.append(top_bowl_team1)
    top_bowl_team1={}
for i in range(11,14,2):
    top_bat_team2["player_name"] = s[i]
    top_bat_team2["score"] = s[i + 1]
    team2_batsmen.append(top_bat_team2)
    top_bat_team2 = {}
for i in range(15,18,2):
    top_bowl_team2["player_name"] = s[i]
    temp = s[i + 1].split("/")
    top_bowl_team2["wickets"] = temp[0]
    temp = temp[1].split(" ")
    top_bowl_team2["runs_conceded"] = temp[0]
    team2_bowlers.append(top_bowl_team2)
    top_bowl_team2 = {}
team1={}
team2={}
team1["team_name"]=s[1].split(" ")[0]
team1["top_batsmen"]=team1_batsmen
team1["top_bowlers"]=team2_bowlers
team2["team_name"]=s[10].split(" ")[0]
team2["top_batsmen"]=team2_batsmen
team2["top_bowlers"]=team1_bowlers
final=[]
final.append(team1)
final.append(team2)
with open('/home/ib_admin/worldcup/first.json', 'w') as fout:
    json.dump(final , fout)
with open('/home/ib_admin/worldcup/first.json', 'w', encoding='utf-8') as outfile:
    json.dump(final, outfile, ensure_ascii=False, indent=2)
print(final)
