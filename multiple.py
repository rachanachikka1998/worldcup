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
match = driver.find_elements_by_partial_link_text("India")

for j in range(len(match)):
    elem = Select(driver.find_element_by_xpath('//*[@id="team"]'))
    elem.select_by_visible_text("India")
    match = driver.find_elements_by_partial_link_text("India")
    match[j].click()
    summary= driver.find_element_by_partial_link_text("Summary")
    summary.click()
    score=driver.find_element_by_class_name("scorecard-summary")
    s=score.text
    print(s)
    s = s.split("\n")
    team1_batsmen = []
    team2_batsmen = []
    team1_bowlers = []
    team2_bowlers = []
    top_bat_team1 = {}
    top_bowl_team1 = {}
    top_bat_team2 = {}
    top_bowl_team2 = {}
    for i in range(2, 5, 2):
        top_bat_team1["player_name"] = s[i]
        top_bat_team1["score"] = int(s[i + 1].split(" ")[0])
        team1_batsmen.append(top_bat_team1)
        top_bat_team1 = {}
    for i in range(6, 9, 2):
        top_bowl_team1["player_name"] = s[i]
        temp = s[i + 1].split("/")
        top_bowl_team1["wickets"] = int(temp[0])
        temp = temp[1].split(" ")
        top_bowl_team1["runs_conceded"] = int(temp[0])
        team1_bowlers.append(top_bowl_team1)
        top_bowl_team1 = {}
    for i in range(11, 14, 2):
        top_bat_team2["player_name"] = s[i]
        top_bat_team2["score"] = int(s[i + 1].split(" ")[0])
        team2_batsmen.append(top_bat_team2)
        top_bat_team2 = {}
    for i in range(15, 18, 2):
        top_bowl_team2["player_name"] = s[i]
        temp = s[i + 1].split("/")
        top_bowl_team2["wickets"] = int(temp[0])
        temp = temp[1].split(" ")
        top_bowl_team2["runs_conceded"] = int(temp[0])
        team2_bowlers.append(top_bowl_team2)
        top_bowl_team2 = {}
    team1 = {}
    team2 = {}
    name1=s[1].split(" ")
    name2=s[10].split(" ")
    strname1=""
    strname2=""
    for k in name1[0:len(name1)-2]:
        strname1=strname1+k+" "
    for k in name2[0:len(name2) - 2]:
        strname2 = strname2 +k+" "
    team1["team_name"] = strname1
    team1["top_batsmen"] = team1_batsmen
    team1["top_bowlers"] = team2_bowlers
    team2["team_name"] = strname2
    team2["top_batsmen"] = team2_batsmen
    team2["top_bowlers"] = team1_bowlers
    final = []
    final.append(team1)
    final.append(team2)
    name=strname1+" vs "+strname2
    with open('/home/ib_admin/worldcup/'+name+'.json', 'w') as fout:
        json.dump(final, fout)
    with open('/home/ib_admin/worldcup/'+name+'.json', 'w', encoding='utf-8') as outfile:
        json.dump(final, outfile, ensure_ascii=False, indent=2)
    print(final)

    driver.execute_script("window.history.go(-2)")
    driver.refresh()
