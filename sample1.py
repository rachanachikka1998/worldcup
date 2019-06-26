from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Firefox()

driver.get("http://www.espncricinfo.com/icc-cricket-world-cup-2015/content/series/509587.html?template=fixtures")
elem= Select(driver.find_element_by_xpath('//*[@id="team"]'))
elem.select_by_visible_text("India")
match = driver.find_elements_by_partial_link_text("India")

elem = Select(driver.find_element_by_xpath('//*[@id="team"]'))
elem.select_by_visible_text("India")
match = driver.find_elements_by_partial_link_text("India")
match[0].click()
names=driver.find_elements_by_class_name("gp__cricket__gameHeader")
for i in names:
    print(i.text)